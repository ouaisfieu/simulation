// Moteur de simulation « Et si la Belgique adoptait les 263 mesures ? »
// Module ES sans dépendance, exécuté à l'identique au build (Node) et dans le navigateur.
// Unités : millions d'euros (M€) pour les mesures, milliards (Md€) pour les agrégats, % du PIB pour les ratios.

export const ANNEES = [2026, 2027, 2028, 2029, 2030, 2031];
const ORDRE_GRADE = { A: 1, B: 2, C: 3, D: 4, E: 5, "—": 0 };

/** Prépare les données brutes (JSON) pour la simulation. */
export function preparer(bfp, editorial, base, hyp) {
  const ed = new Map(editorial.mesures.map((m) => [m.id, m]));
  const mesures = bfp.mesures.map((b) => ({ ...ed.get(b.id), id: b.id, ref: b.ref, bfp: b.montant2029, langue: b.langue }));
  const parId = new Map(mesures.map((m) => [m.id, m]));
  const familles = new Map(editorial.familles.map((f) => [f.code, f]));
  // PIB nominal de référence (Md€)
  const pib = { 2025: base.pib2025 };
  base.annees.forEach((a, i) => {
    if (i === 0) return;
    pib[a] = pib[a - 1] * (1 + base.croissanceReelle[i] / 100) * (1 + base.deflateur[i] / 100);
  });
  const serie = (k) => Object.fromEntries(base.annees.map((a, i) => [a, base[k][i]]));
  return {
    mesures, parId, familles, contradictions: editorial.contradictions, hyp, base,
    ref: { pib, solde: serie("solde"), soldePrimaire: serie("soldePrimaire"), dette: serie("dette"), emploi: serie("emploi"), chomage: serie("chomage") },
  };
}

/** Paramètres par défaut d'un scénario. */
export function parametres(scenario = "pmc", surcharge = {}) {
  return {
    scenario, choix: {}, desactives: [],
    niveau: "central", macro: "central", fuite: "central", erosion: "central",
    gradeMax: "E", instrumentsSante: false, inclureRegions: true, inclureCouts: true,
    repercussion: null, tauxMarche: null, reactionMarches: null, dividendes: null, privatisations: true,
    ...surcharge,
  };
}

const ids = (v) => (v === undefined || v === null || v === "aucune" ? [] : Array.isArray(v) ? v : [v]);

/** Détermine quelles mesures sont en vigueur, avec quel poids et pourquoi les autres ne le sont pas. */
export function selectionner(d, p) {
  const actifs = new Map(); // id -> poids
  const exclus = new Map(); // id -> raison
  const choixEffectifs = {};
  const sc = p.scenario === "perso" ? (p.base || "pmc") : p.scenario;
  const modeBfp = sc === "bfp";
  const litteral = sc === "litteral";

  const eligible = (m) => {
    if (modeBfp) return m.bfp !== null && m.bfp !== undefined;
    return true;
  };

  // 1. choix par famille
  const absorbees = new Map(); // code famille -> id de la variante qui l'absorbe
  if (!litteral) {
    for (const f of d.familles.values()) {
      if (f.mode !== "exclusif") continue;
      let v = p.choix[f.code];
      if (v === undefined) {
        v = f.choix[sc];
        if (v === undefined && modeBfp) {
          const cands = f.membres.map((i) => d.parId.get(i)).filter((m) => m.bfp != null);
          if (cands.length) v = cands.sort((a, b) => b.bfp - a.bfp)[0].id;
        }
      }
      choixEffectifs[f.code] = v === undefined ? "aucune" : v;
      for (const i of ids(v)) {
        const abs = f.absorbe[String(i)] || [];
        for (const c of abs) absorbees.set(c, i);
      }
    }
  }

  // 2. statut de chaque mesure
  for (const m of d.mesures) {
    const f = d.familles.get(m.fam);
    if (!eligible(m)) { exclus.set(m.id, "non chiffrée par le BFP"); continue; }
    if (p.desactives.includes(m.id)) { exclus.set(m.id, "désactivée"); continue; }
    if (litteral) { actifs.set(m.id, 1); continue; }
    if (absorbees.has(m.fam)) { exclus.set(m.id, `incluse dans la variante BFP-${String(absorbees.get(m.fam) + 1).padStart(3, "0")}`); continue; }
    if (f.mode === "exclusif") {
      if (!ids(choixEffectifs[f.code]).includes(m.id)) { exclus.set(m.id, "autre variante retenue"); continue; }
    }
    if (f.mode === "instruments" && !p.instrumentsSante) { exclus.set(m.id, "instrument de la norme santé"); continue; }
    if (!modeBfp && ORDRE_GRADE[m.gr] > ORDRE_GRADE[p.gradeMax]) { exclus.set(m.id, `confiance inférieure à ${p.gradeMax}`); continue; }
    if (!p.inclureCouts && m.typ === "C") { exclus.set(m.id, "mesure coûteuse exclue"); continue; }
    if (!p.inclureRegions && (m.fam === "F21a" || m.fam === "F21b")) { exclus.set(m.id, "entités fédérées exclues"); continue; }
    actifs.set(m.id, 1);
  }

  // 3. contradictions : le camp minoritaire est écarté
  if (!litteral && !modeBfp) {
    for (const c of d.contradictions) {
      const enJeu = [...(c.a || []), ...(c.b || [])].filter((i) => actifs.has(i));
      if (enJeu.length < 2) continue;
      for (const i of c.perdants || []) {
        if (actifs.has(i)) { actifs.delete(i); exclus.set(i, `contradiction : ${c.sujet}`); }
      }
    }
  }

  // 4. recouvrements dans les familles cumulatives
  if (!litteral) {
    for (const f of d.familles.values()) {
      if (f.mode !== "cumul" || f.recouvrement >= 1) continue;
      const membres = f.membres.filter((i) => actifs.has(i))
        .sort((a, b) => Math.abs(valeur(d, p, b, modeBfp)) - Math.abs(valeur(d, p, a, modeBfp)));
      membres.forEach((i, k) => actifs.set(i, k === 0 ? 1 : f.recouvrement));
    }
  }
  return { actifs, exclus, choixEffectifs, modeBfp, litteral };
}

function valeur(d, p, id, modeBfp) {
  const m = d.parId.get(id);
  if (modeBfp) return m.typ === "F" ? 0 : m.bfp || 0;
  if (["P", "N", "X", "F"].includes(m.typ)) return 0;
  return m.est[p.niveau] ?? m.est.central;
}

const phase = (m, a) => (a <= 2026 ? 0 : a === 2027 ? m.ph[0] : a === 2028 ? m.ph[1] : 1);

/** Simulation complète. */
export function simuler(d, p) {
  const h = d.hyp;
  const sel = selectionner(d, p);
  const mult = (c) => h.multiplicateurs.classes[c]?.[p.macro] ?? 0;
  const lambda = h.fuiteIndexation[p.fuite];
  // Érosion des impôts sur le capital, aggravée quand plusieurs impôts frappent la même assiette
  const famCap = new Set(h.erosionCapital.famillesCapital || []);
  const famCapActives = new Set();
  for (const [id] of sel.actifs) { const m = d.parId.get(id); if (famCap.has(m.fam) && valeur(d, p, id, sel.modeBfp) > 0) famCapActives.add(m.fam); }
  const eta = Math.min(h.erosionCapital.plafond ?? 0.5, h.erosionCapital[p.erosion] + (h.erosionCapital.cumul ?? 0) * Math.max(0, famCapActives.size - 1));
  const phi = p.repercussion ?? h.repercussionRegions.valeur;
  const r = (p.tauxMarche ?? h.tauxMarche.valeur) / 100;
  const kappa = p.reactionMarches ?? h.reactionMarches.valeur;
  const delta = (p.dividendes ?? h.dividendes.valeur) / 100;
  const eps = h.semiElasticite.valeur;
  const w = h.multiplicateurs.persistance;
  const pib = d.ref.pib;

  const lignes = []; // contributions par mesure (M€)
  const brutClasse = {}; const netClasse = {};
  const par = (o, c, a, v) => { o[c] ??= {}; o[c][a] = (o[c][a] || 0) + v; };

  for (const [id, poids] of sel.actifs) {
    const m = d.parId.get(id);
    const v = valeur(d, p, id, sel.modeBfp);
    if (!v) continue;
    const parAn = {}; const netAn = {};
    for (const a of ANNEES) {
      let y = v * phase(m, a) * (pib[a] / pib[2029]) * poids;
      if (m.typ === "T" && !sel.modeBfp) y *= phi;
      let n = y;
      if (m.mc === "conso") n = y * (1 - lambda);
      else if (m.mc === "capital") n = y * (1 - eta);
      parAn[a] = y; netAn[a] = n;
      par(brutClasse, m.mc, a, y); par(netClasse, m.mc, a, n);
    }
    lignes.push({ id, poids, mc: m.mc, inc: m.inc, fam: m.fam, typ: m.typ, brut: parAn, net: netAn, bfp: m.bfp });
  }

  // Opérations financières (ventes de participations)
  const fin = { ventes: {}, reinvest: {}, dividendes: {} };
  if (p.privatisations && !sel.litteral) {
    for (const [id] of sel.actifs) {
      const op = h.operationsFinancieres[String(id)];
      if (!op) continue;
      fin.ventes[op.annee] = (fin.ventes[op.annee] || 0) + op.montant;
      for (const a of ANNEES) {
        if (a === op.annee) fin.dividendes[a] = (fin.dividendes[a] || 0) + 0.5 * delta * op.montant;
        if (a > op.annee) fin.dividendes[a] = (fin.dividendes[a] || 0) + delta * op.montant * (pib[a] / pib[op.annee]);
        if (op.reinvesti && (a === op.annee || a === op.annee + 1)) {
          const x = op.reinvesti * op.montant / 2;
          fin.reinvest[a] = (fin.reinvest[a] || 0) + x;
          par(netClasse, "consopub", a, -x); // dépense supplémentaire : impulsion négative
        }
      }
    }
  }

  // Écart de PIB (fraction) par rapport à la référence
  const ecart = {};
  for (const t of ANNEES) {
    let g = 0;
    for (const c of Object.keys(netClasse)) {
      const m = mult(c);
      if (!m) continue;
      for (const s of ANNEES) {
        if (s > t) break;
        const niv = (netClasse[c][s] || 0) / 1000 / pib[s];
        const prec = s === ANNEES[0] ? 0 : (netClasse[c][s - 1] || 0) / 1000 / pib[s - 1];
        g -= m * (w[t - s] ?? w[w.length - 1]) * (niv - prec);
      }
    }
    ecart[t] = g;
  }

  // Finances publiques
  const res = { annees: ANNEES, pibRef: {}, pib: {}, ecartPib: {}, croissance: {}, croissanceRef: {}, solde: {}, soldeRef: {}, soldePrimaire: {}, dette: {}, detteRef: {}, interets: {}, emploi: {}, chomage: {},
    brut: {}, net: {}, stabilisateurs: {}, economieInterets: {}, spread: {}, dividendesPerdus: {}, reinvestissements: {}, ventes: {}, ameliorationSolde: {} };
  let dPrec = d.ref.dette[2025] / 100 * pib[2025];
  let dRefPrec = dPrec;
  let amelPrec = 0;
  for (const t of ANNEES) {
    const brut = sum(lignes.map((l) => l.brut[t])) / 1000;
    const net = sum(Object.values(netClasse).map((o) => o[t] || 0)) / 1000; // inclut les réinvestissements (négatifs)
    const pibS = pib[t] * (1 + ecart[t]);
    const bRef = d.ref.solde[t] / 100 * pib[t];
    const dRef = d.ref.dette[t] / 100 * pib[t];
    const sfa = dRef - dRefPrec + bRef; // ajustement stock-flux implicite de la référence
    const auto = eps * ecart[t] * pib[t];
    const ecoInt = r * (dRefPrec - dPrec);
    const part = Math.min(1, h.refinancement.valeur * (t - 2026));
    const dSpread = Math.max(-h.reactionMarches.plafond, Math.min(h.reactionMarches.plafond, kappa * amelPrec)) / 10000;
    const spread = dSpread * part * dRefPrec;
    const div = (fin.dividendes[t] || 0) / 1000;
    const bS = bRef + net + auto + ecoInt + spread - div;
    const vente = (fin.ventes[t] || 0) / 1000;
    const dS = dPrec - bS + sfa - vente;
    const intRef = (d.ref.soldePrimaire[t] - d.ref.solde[t]) / 100 * pib[t];
    const intS = intRef - ecoInt - spread;
    res.pibRef[t] = pib[t]; res.pib[t] = pibS; res.ecartPib[t] = ecart[t] * 100;
    res.solde[t] = bS / pibS * 100; res.soldeRef[t] = d.ref.solde[t];
    res.soldePrimaire[t] = (bS + intS) / pibS * 100;
    res.dette[t] = dS / pibS * 100; res.detteRef[t] = d.ref.dette[t];
    res.interets[t] = intS / pibS * 100;
    res.brut[t] = brut; res.net[t] = net; res.stabilisateurs[t] = auto; res.economieInterets[t] = ecoInt; res.spread[t] = spread;
    res.dividendesPerdus[t] = div; res.reinvestissements[t] = (fin.reinvest[t] || 0) / 1000; res.ventes[t] = vente;
    res.ameliorationSolde[t] = res.solde[t] - d.ref.solde[t];
    const eRef = d.ref.emploi[t];
    res.emploi[t] = h.okun.valeur * ecart[t] * eRef; // milliers
    const pop = eRef / (1 - d.ref.chomage[t] / 100);
    res.chomage[t] = d.ref.chomage[t] - res.emploi[t] / pop * 100;
    amelPrec = res.ameliorationSolde[t];
    dPrec = dS; dRefPrec = dRef;
  }
  for (const t of ANNEES) {
    const prec = t === 2026 ? null : t - 1;
    const croissRef = d.base.croissanceReelle[d.base.annees.indexOf(t)];
    res.croissanceRef[t] = croissRef;
    res.croissance[t] = prec === null ? croissRef + res.ecartPib[t] : ((1 + croissRef / 100) * (1 + res.ecartPib[t] / 100) / (1 + res.ecartPib[prec] / 100) - 1) * 100;
  }
  res.lignes = lignes;
  res.selection = sel;
  res.erosionEffective = eta;
  res.famillesCapitalActives = [...famCapActives];
  res.incidence = incidence(d, lignes, res);
  res.familles = parFamille(d, lignes);
  res.classes = { brut: brutClasse, net: netClasse };
  res.indicateurs = indicateurs(res);
  return res;
}

const sum = (a) => a.reduce((x, y) => x + (y || 0), 0);

function incidence(d, lignes, res) {
  const h = d.hyp; const groupes = {};
  const annees = [2027, 2028, 2029];
  for (const l of lignes) {
    const prof = h.profils[l.inc] || {};
    const nature = prof.nature === "services" ? "services" : "monetaire";
    for (const [g, part] of Object.entries(prof)) {
      if (g === "label" || g === "nature") continue;
      groupes[g] ??= { monetaire: {}, services: {} };
      for (const a of annees) groupes[g][nature][a] = (groupes[g][nature][a] || 0) + l.net[a] * part;
    }
  }
  const sortie = {};
  for (const [g, v] of Object.entries(groupes)) {
    const info = h.menages.groupes[g];
    const total = Object.fromEntries(annees.map((a) => [a, (v.monetaire[a] || 0) + (v.services[a] || 0)]));
    sortie[g] = { label: info?.label || h.menages.autres[g] || g, total, monetaire: v.monetaire, services: v.services };
    if (info) {
      sortie[g].parMenage = {}; sortie[g].pctRevenu = {}; sortie[g].pctRevenuMonetaire = {}; sortie[g].parMenageMonetaire = {};
      for (const a of annees) {
        const revenu = h.menages.partRevenuPib * res.pibRef[a] * 1e3 * info.partRevenu; // M€
        sortie[g].parMenage[a] = total[a] / info.menages; // € par ménage et par an (M€ / millions de ménages)
        sortie[g].parMenageMonetaire[a] = (v.monetaire[a] || 0) / info.menages;
        sortie[g].pctRevenu[a] = total[a] / revenu * 100;
        sortie[g].pctRevenuMonetaire[a] = (v.monetaire[a] || 0) / revenu * 100;
      }
    }
  }
  return sortie;
}

/** Cherche, famille par famille, le plus petit sous-ensemble du paquet qui ramène le déficit
 * sous un seuil une année donnée. Critère : rendement net par point de PIB perdu (le moins récessif d'abord). */
export function paquetSuffisant(d, p, { seuil = -3, annee = 2028, critere = "recessif" } = {}) {
  const complet = simuler(d, p);
  const cands = complet.familles.filter((f) => f.net[annee] > 0).map((f) => {
    const lignesF = complet.lignes.filter((l) => l.fam === f.code);
    const choc = lignesF.reduce((s, l) => s + l.net[annee] * (d.hyp.multiplicateurs.classes[l.mc]?.[p.macro] ?? 0), 0);
    return { code: f.code, label: f.label, net: f.net[annee], ratio: f.net[annee] / Math.max(choc, 1e-6), ids: lignesF.map((l) => l.id) };
  });
  if (critere === "recessif") cands.sort((a, b) => b.ratio - a.ratio);
  else cands.sort((a, b) => b.net - a.net);
  const retenues = [];
  const tousIds = new Set(complet.lignes.map((l) => l.id));
  let r = null;
  for (const c of cands) {
    retenues.push(c);
    const garde = new Set(retenues.flatMap((x) => x.ids));
    const desactives = [...p.desactives, ...[...tousIds].filter((i) => !garde.has(i))];
    r = simuler(d, { ...p, desactives });
    if (r.solde[annee] >= seuil) break;
  }
  return { familles: retenues, resultat: r, atteint: r ? r.solde[annee] >= seuil : false };
}

function parFamille(d, lignes) {
  const o = {};
  for (const l of lignes) {
    o[l.fam] ??= { code: l.fam, label: d.familles.get(l.fam).label, groupe: d.familles.get(l.fam).groupe, brut: {}, net: {}, n: 0 };
    o[l.fam].n += 1;
    for (const a of ANNEES) { o[l.fam].brut[a] = (o[l.fam].brut[a] || 0) + l.brut[a]; o[l.fam].net[a] = (o[l.fam].net[a] || 0) + l.net[a]; }
  }
  return Object.values(o).sort((a, b) => Math.abs(b.brut[2029]) - Math.abs(a.brut[2029]));
}

function indicateurs(res) {
  const sous3 = ANNEES.find((a) => res.solde[a] >= -3);
  let pic = ANNEES[0];
  for (const a of ANNEES) if (res.dette[a] >= res.dette[pic]) pic = a;
  const detteBaisse = ANNEES.find((a, i) => i > 0 && res.dette[a] < res.dette[ANNEES[i - 1]]);
  return {
    soldeSous3: sous3 ?? null, piqueDette: pic, detteBaisseDes: detteBaisse ?? null,
    pireEcartPib: Math.min(...ANNEES.map((a) => res.ecartPib[a])),
    pireEmploi: Math.min(...ANNEES.map((a) => res.emploi[a])),
    excedentPrimaire2028: res.soldePrimaire[2028],
  };
}

/** Décomposition « de la somme naïve au solde » pour une année (2028 ou 2029). */
export function cascade(d, p, annee = 2029) {
  const naif = d.mesures.reduce((s, m) => s + (m.bfp || 0), 0);
  const fin = d.mesures.filter((m) => m.typ === "F").reduce((s, m) => s + (m.bfp || 0), 0);
  const struct = (sc) => {
    const r = simuler(d, { ...p, scenario: sc, base: sc, choix: {}, desactives: [], gradeMax: "E" });
    let bfpPart = 0, autresPos = 0, couts = 0;
    for (const l of r.lignes) {
      const v = l.brut[2029] * (d.ref.pib[2029] / d.ref.pib[2029]);
      if (l.bfp != null) bfpPart += v; else if (v >= 0) autresPos += v; else couts += v;
    }
    return { r, bfpPart, autresPos, couts };
  };
  const B = struct("bfp");
  const P = simuler(d, p);
  let bfpPart = 0, autresPos = 0, couts = 0, struct2029 = 0;
  for (const l of P.lignes) {
    const v = l.brut[2029];
    struct2029 += v;
    if (l.bfp != null) bfpPart += v; else if (v >= 0) autresPos += v; else couts += v;
  }
  const realise = sum(P.lignes.map((l) => l.brut[annee]));
  const netA = P.net[annee] * 1000 + P.reinvestissements[annee] * 1000; // net hors réinvestissement
  const etapes = [
    { cle: "naif", label: "Somme des 39 montants du BFP", valeur: naif, type: "total" },
    { cle: "fin", label: "Ventes d'actifs : sans effet sur le déficit", valeur: -fin, type: "delta" },
    { cle: "doublons", label: "Une seule variante par assiette", valeur: B.bfpPart - (naif - fin), type: "delta" },
    { cle: "bfpOnly", label: "Montants BFP sans doublons", valeur: B.bfpPart, type: "total" },
    { cle: "ajust", label: "Mesures déjà adoptées, conditions, autres variantes", valeur: bfpPart - B.bfpPart, type: "delta" },
    { cle: "autres", label: "Mesures non chiffrées par le BFP (estimations)", valeur: autresPos, type: "delta" },
    { cle: "couts", label: "Mesures coûteuses du catalogue", valeur: couts, type: "delta" },
    { cle: "pmc", label: "Paquet structurel (niveau 2029)", valeur: struct2029, type: "total" },
  ];
  etapes.push({ cle: "montee", label: `Montée en charge : ce qui est perçu en ${annee}`, valeur: realise - struct2029, type: "delta" });
  etapes.push(
    { cle: "fuites", label: "Évitement fiscal et indexation", valeur: netA - realise, type: "delta" },
    { cle: "macro", label: "Récession induite (stabilisateurs automatiques)", valeur: P.stabilisateurs[annee] * 1000, type: "delta" },
    { cle: "interets", label: "Intérêts économisés", valeur: (P.economieInterets[annee] + P.spread[annee]) * 1000, type: "delta" },
    { cle: "fin2", label: "Dividendes perdus et réinvestissements", valeur: -(P.dividendesPerdus[annee] + P.reinvestissements[annee]) * 1000, type: "delta" },
  );
  const final = (P.solde[annee] / 100 * P.pib[annee] - P.soldeRef[annee] / 100 * P.pibRef[annee]) * 1000;
  etapes.push({ cle: "final", label: `Amélioration du solde en ${annee}`, valeur: final, type: "total" });
  return { etapes, annee, resultat: P };
}
