// Données globales du site : fusion des sources et simulations précalculées au build.
// Les chiffres affichés dans les pages statiques sortent du même moteur que le simulateur.
import fs from "node:fs";
import { preparer, parametres, simuler, cascade, paquetSuffisant, ANNEES } from "../assets/js/moteur.js";

const lire = (f) => JSON.parse(fs.readFileSync(`data/${f}`, "utf8"));

export default function () {
  const bfp = lire("mesures-bfp.json");
  const ed = lire("editorial.json");
  const base = lire("base.json");
  const hyp = lire("hypotheses.json");
  const sources = lire("sources.json");
  const liens = lire("liens.json");
  const d = preparer(bfp, ed, base, hyp);

  const run = (sc, extra = {}) => simuler(d, parametres(sc, extra));
  const pmc = run("pmc");
  const med = run("med");
  const bfpS = run("bfp");
  const lit = run("litteral");
  // fourchettes : budget (bas = défavorable au solde) et activité (sévère = plus de récession)
  const budgetBas = run("pmc", { niveau: "bas", macro: "severe", fuite: "severe", erosion: "severe" });
  const budgetHaut = run("pmc", { niveau: "haut", macro: "doux", fuite: "doux", erosion: "doux" });
  const pibPire = run("pmc", { niveau: "haut", macro: "severe", fuite: "doux", erosion: "doux" });
  const pibDoux = run("pmc", { niveau: "bas", macro: "doux", fuite: "severe", erosion: "severe" });
  const sansRegions = run("pmc", { inclureRegions: false });
  const sansCouts = run("pmc", { inclureCouts: false });
  const gradeA = run("pmc", { gradeMax: "B" });
  const instruments = run("pmc", { instrumentsSante: true });
  const defiance = run("pmc", { reactionMarches: -6 });

  const cascade2028 = cascade(d, parametres("pmc"), 2028);
  const cascade2029 = cascade(d, parametres("pmc"), 2029);
  const suffisantRecessif = paquetSuffisant(d, parametres("pmc"), { seuil: -3, annee: 2028, critere: "recessif" });
  const suffisantRendement = paquetSuffisant(d, parametres("pmc"), { seuil: -3, annee: 2028, critere: "rendement" });

  // Fiches : fusion BFP + éditorial + contributions simulées
  const contrib = new Map(pmc.lignes.map((l) => [l.id, l]));
  const contribMed = new Map(med.lignes.map((l) => [l.id, l]));
  const famLabel = new Map(ed.familles.map((f) => [f.code, f]));
  const contradictionsPar = new Map();
  for (const c of ed.contradictions) for (const i of [...c.a, ...c.b]) { if (!contradictionsPar.has(i)) contradictionsPar.set(i, []); contradictionsPar.get(i).push(c); }
  const tensionsPar = new Map();
  for (const t of ed.tensions) for (const i of t.ids) { if (!tensionsPar.has(i)) tensionsPar.set(i, []); tensionsPar.get(i).push(t); }

  const mesures = bfp.mesures.map((b) => {
    const e = d.parId.get(b.id);
    const l = contrib.get(b.id);
    return {
      ...b, ...e, bfp: b.montant2029,
      slug: b.ref.toLowerCase(),
      conclave: liens.conclave[b.id],
      famille: famLabel.get(e.fam),
      statutPmc: l ? "retenue" : (pmc.selection.exclus.get(b.id) || "sans effet"),
      statutMed: contribMed.has(b.id) ? "retenue" : (med.selection.exclus.get(b.id) || "sans effet"),
      poids: l ? l.poids : 0,
      perception: l ? { 2027: l.brut[2027], 2028: l.brut[2028], 2029: l.brut[2029] } : null,
      contradictions: contradictionsPar.get(b.id) || [],
      tensions: tensionsPar.get(b.id) || [],
    };
  });
  const parId = Object.fromEntries(mesures.map((m) => [m.id, m]));
  for (const m of mesures) {
    m.autres = ed.familles.find((f) => f.code === m.fam).membres.filter((i) => i !== m.id)
      .map((i) => ({ slug: parId[i].slug, ref: parId[i].ref, t: parId[i].t, bfp: parId[i].bfp }));
  }
  const familles = ed.familles.map((f) => {
    const r = pmc.familles.find((x) => x.code === f.code);
    const rm = med.familles.find((x) => x.code === f.code);
    return { ...f, slug: f.code.toLowerCase(), pmc: r || null, med: rm || null, choixPmc: pmc.selection.choixEffectifs[f.code], choixMed: med.selection.choixEffectifs[f.code] };
  });

  const resume = (r) => ({
    brut: r.brut, net: r.net, solde: r.solde, soldeRef: r.soldeRef, dette: r.dette, detteRef: r.detteRef,
    ecartPib: r.ecartPib, croissance: r.croissance, croissanceRef: r.croissanceRef, emploi: r.emploi, chomage: r.chomage,
    soldePrimaire: r.soldePrimaire, interets: r.interets, indicateurs: r.indicateurs, actives: r.selection.actifs.size,
    stabilisateurs: r.stabilisateurs, economieInterets: r.economieInterets, spread: r.spread, erosion: r.erosionEffective,
  });

  // Faisabilité : d'où vient le rendement du paquet maximal (niveau 2029 et 2028) ?
  const grouper = (cle) => {
    const o = {};
    for (const l of pmc.lignes) {
      const m = d.parId.get(l.id);
      const k = cle(m);
      o[k] ??= { 2028: 0, 2029: 0, n: 0 };
      o[k][2028] += l.brut[2028]; o[k][2029] += l.brut[2029]; o[k].n += 1;
    }
    return o;
  };
  const faisabilite = {
    competence: grouper((m) => m.comp), vehicule: grouper((m) => m.veh), delai: grouper((m) => m.dl),
    horsPortee: grouper((m) => (m.comp !== "F" || ["LS", "REF", "-", "UE"].includes(m.veh) || m.dl >= 2) ? "difficile" : "accessible"),
    type: grouper((m) => m.typ),
    grade: grouper((m) => m.gr),
  };
  // Partis à l'origine des 39 montants (chiffrage DC2024)
  const partis = {};
  for (const m of bfp.mesures) {
    const x = /DC Maatregel ([A-Za-zÀ-ÿ&\- ]+?) \d/.exec(m.sourceChiffrage || "");
    if (!x) continue;
    const p = x[1].trim();
    partis[p] ??= { parti: p, n: 0, montant: 0, ids: [] };
    partis[p].n += 1; partis[p].montant += m.montant2029 || 0; partis[p].ids.push(m.id);
  }
  // Estimations « analyse » du projet Fumée blanche, comparées à celles du site (page Projets liés)
  const parRef = Object.fromEntries(mesures.map((m) => [m.ref, m]));
  const ca = lire("conclave-analyse.json");
  const conclaveAnalyse = ca.estimations.map((x) => {
    const m = parRef[x.ref];
    return { ...x, slug: m.slug, t: m.t, typ: m.typ, gr: m.gr, est: m.est, statutPmc: m.statutPmc, ecart: x.montant - (m.est?.central || 0) };
  });
  const naif = bfp.mesures.reduce((s, m) => s + (m.montant2029 || 0), 0);
  const stats = {
    total: bfp.mesures.length,
    chiffrees: bfp.mesures.filter((m) => m.montant2029 !== null).length,
    naif,
    financieres: ed.mesures.filter((m) => m.typ === "F").reduce((s, m) => s + (parId[m.id].bfp || 0), 0),
    parType: Object.fromEntries(["R", "D", "C", "T", "P", "F", "N", "X"].map((t) => [t, ed.mesures.filter((m) => m.typ === t).length])),
    parGrade: Object.fromEntries(["A", "B", "C", "D", "E", "—"].map((g) => [g, ed.mesures.filter((m) => m.gr === g).length])),
    parLangue: bfp.mesures.reduce((o, m) => ((o[m.langue] = (o[m.langue] || 0) + 1), o), {}),
    parCategorie: Object.entries(bfp.mesures.reduce((o, m) => ((o[m.categorie.trim()] = (o[m.categorie.trim()] || 0) + 1), o), {})).sort((a, b) => b[1] - a[1]),
    familles: ed.familles.length,
    contradictions: ed.contradictions.length,
    pmcActives: pmc.selection.actifs.size,
    medActives: med.selection.actifs.size,
  };

  return {
    annees: ANNEES, base, hyp, sources, sourcesParCle: Object.fromEntries(sources.map((s) => [s.cle, s])), liens,
    mesures, parId, familles, contradictions: ed.contradictions, tensions: ed.tensions, stats,
    pmc: { ...resume(pmc), familles: pmc.familles, incidence: pmc.incidence, choix: pmc.selection.choixEffectifs },
    med: { ...resume(med), familles: med.familles, incidence: med.incidence },
    bfp: resume(bfpS), litteral: resume(lit),
    budgetBas: resume(budgetBas), budgetHaut: resume(budgetHaut), pibPire: resume(pibPire), pibDoux: resume(pibDoux),
    sansRegions: resume(sansRegions), sansCouts: resume(sansCouts), gradeA: resume(gradeA), instruments: resume(instruments), defiance: resume(defiance),
    cascade2028: cascade2028.etapes, cascade2029: cascade2029.etapes,
    suffisant: {
      recessif: { familles: suffisantRecessif.familles, r: resume(suffisantRecessif.resultat), atteint: suffisantRecessif.atteint },
      rendement: { familles: suffisantRendement.familles, r: resume(suffisantRendement.resultat), atteint: suffisantRendement.atteint },
    },
    refPib: d.ref.pib, faisabilite, conclaveAnalyse, conclaveAnalyseMeta: ca.meta, metaBfp: bfp.meta, partis: Object.values(partis).sort((x, y) => y.n - x.n || y.montant - x.montant),
  };
}
