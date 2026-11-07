// Interface du simulateur : lit les réglages, appelle le moteur, redessine.
import { preparer, parametres, simuler, cascade, ANNEES } from "./moteur.js";
import { courbesSvg, cascadeSvg, barresSvg, incidenceSvg, fmt, fmtSigne, formatMeur } from "./graphiques.js";

const BASE = new URL("../../", import.meta.url).pathname; // « /simulation/ »
const $ = (s, r = document) => r.querySelector(s);
const form = $("#sim-form");
const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
const ref = (id) => `BFP-${String(id + 1).padStart(3, "0")}`;

let D = null; let brut = null;
const SCENARIOS = {};

async function demarrer() {
  try {
    const rep = await fetch(new URL("../data/simulation.json", import.meta.url));
    brut = await rep.json();
  } catch (e) {
    $("#sim-alerte").innerHTML = `<p class="alerte-sim">Impossible de charger les données du simulateur.</p>`;
    return;
  }
  D = preparer(brut.bfp, brut.editorial, brut.base, brut.hyp);
  Object.assign(SCENARIOS, brut.hyp.scenarios);
  construireFamilles();
  lireEtat();
  form.addEventListener("input", miseAJour);
  form.addEventListener("change", miseAJour);
  $("#sim-reset").addEventListener("click", () => { history.replaceState(null, "", location.pathname); form.reset(); construireFamilles(); miseAJour(); });
  $("#sim-lien").addEventListener("click", async () => {
    try { await navigator.clipboard.writeText(location.href); $("#sim-lien-etat").textContent = "Lien copié."; }
    catch (e) { $("#sim-lien-etat").textContent = location.href; }
  });
  let t; addEventListener("resize", () => { clearTimeout(t); t = setTimeout(miseAJour, 150); });
  miseAJour();
}

// ---------- Familles : une liste par groupe ----------
function construireFamilles() {
  const zone = $("#sim-familles");
  zone.querySelectorAll("details").forEach((d) => d.remove());
  const groupes = new Map();
  for (const f of D.familles.values()) {
    if (["processus", "neutre"].includes(f.mode)) continue;
    if (!groupes.has(f.groupe)) groupes.set(f.groupe, []);
    groupes.get(f.groupe).push(f);
  }
  for (const [g, fams] of groupes) {
    const det = document.createElement("details");
    let html = `<summary><span>${esc(g)}</span><span class="petit muet">${fams.length}</span></summary>`;
    for (const f of fams) {
      if (f.mode === "exclusif") {
        const opts = [`<option value="defaut">Selon la lecture choisie</option>`, `<option value="aucune">Aucune variante</option>`]
          .concat(f.membres.filter((i) => !["P", "N", "X"].includes(D.parId.get(i).typ) || D.parId.get(i).typ === "N").map((i) => `<option value="${i}">${ref(i)} · ${esc(D.parId.get(i).t)}</option>`));
        if (f.choix.pmc && Array.isArray(f.choix.pmc)) opts.splice(2, 0, `<option value="${f.choix.pmc.join("+")}">${f.choix.pmc.map(ref).join(" + ")}</option>`);
        html += `<label class="curseur"><span>${esc(f.code)} · ${esc(f.label)}</span><select data-famille="${f.code}">${opts.join("")}</select></label>`;
      } else {
        html += `<label class="case"><input type="checkbox" data-famille-on="${f.code}" checked> ${esc(f.code)} · ${esc(f.label)}${f.mode === "instruments" ? " <span class=\"verrou\">(voir la case « instruments santé »)</span>" : ""}</label>`;
      }
    }
    det.innerHTML = html;
    zone.appendChild(det);
  }
}

// ---------- État <-> URL ----------
function etat() {
  const fd = new FormData(form);
  const e = { sc: fd.get("sc"), niv: fd.get("niv"), mac: fd.get("mac"), fui: fd.get("fui"), ero: fd.get("ero"), gr: fd.get("gr"),
    reg: form.reg.checked ? 1 : 0, cou: form.cou.checked ? 1 : 0, ins: form.ins.checked ? 1 : 0, pri: form.pri.checked ? 1 : 0,
    phi: +fd.get("phi"), tm: +fd.get("tm"), km: +fd.get("km"), ch: {}, off: [] };
  form.querySelectorAll("select[data-famille]").forEach((s) => { if (s.value !== "defaut") e.ch[s.dataset.famille] = s.value; });
  form.querySelectorAll("input[data-famille-on]").forEach((c) => { if (!c.checked) e.off.push(c.dataset.familleOn); });
  return e;
}
function ecrireEtat(e) {
  const p = new URLSearchParams();
  const h = D.hyp;
  const def = { sc: "pmc", niv: "central", mac: "central", fui: "central", ero: "central", gr: "E", reg: 1, cou: 1, ins: 0, pri: 1,
    phi: Math.round(h.repercussionRegions.valeur * 100), tm: h.tauxMarche.valeur, km: h.reactionMarches.valeur };
  for (const [k, v] of Object.entries(def)) if (String(e[k]) !== String(v)) p.set(k, e[k]);
  const ch = Object.entries(e.ch).map(([k, v]) => `${k}:${v}`).join(",");
  if (ch) p.set("ch", ch);
  if (e.off.length) p.set("off", e.off.join(","));
  history.replaceState(null, "", p.toString() ? `#${p}` : location.pathname);
}
function lireEtat() {
  const p = new URLSearchParams(location.hash.slice(1));
  const radio = (n) => { const v = p.get(n); if (v) { const el = form.querySelector(`input[name="${n}"][value="${v}"]`); if (el) el.checked = true; } };
  ["sc", "niv", "mac"].forEach(radio);
  for (const n of ["fui", "ero", "gr", "phi", "tm", "km"]) if (p.get(n) !== null) form[n].value = p.get(n);
  for (const n of ["reg", "cou", "ins", "pri"]) if (p.get(n) !== null) form[n].checked = p.get(n) === "1";
  for (const kv of (p.get("ch") || "").split(",").filter(Boolean)) {
    const [k, v] = kv.split(":");
    const s = form.querySelector(`select[data-famille="${k}"]`);
    if (s && [...s.options].some((o) => o.value === v)) s.value = v;
  }
  for (const k of (p.get("off") || "").split(",").filter(Boolean)) {
    const c = form.querySelector(`input[data-famille-on="${k}"]`);
    if (c) c.checked = false;
  }
}

function versParametres(e) {
  const base = e.sc;
  const choix = {};
  for (const [k, v] of Object.entries(e.ch)) choix[k] = v === "aucune" ? "aucune" : v.includes("+") ? v.split("+").map(Number) : Number(v);
  const desactives = [];
  for (const code of e.off) desactives.push(...(D.familles.get(code)?.membres || []));
  return parametres(Object.keys(choix).length && base !== "litteral" ? "perso" : base, {
    base, choix, desactives, niveau: e.niv, macro: e.mac, fuite: e.fui, erosion: e.ero, gradeMax: e.gr,
    inclureRegions: !!e.reg, inclureCouts: !!e.cou, instrumentsSante: !!e.ins, privatisations: !!e.pri,
    repercussion: e.phi / 100, tauxMarche: e.tm, reactionMarches: e.km,
  });
}

// ---------- Rendu ----------
function largeur(el) { return Math.max(320, Math.min(900, Math.round(el.getBoundingClientRect().width || 700) - 32)); }
function carte(id, titre, sousTitre, svg, legende = "", tableau = "") {
  const el = $(id);
  el.innerHTML = `<figure class="graphique"><figcaption class="graphique-titre"><strong>${esc(titre)}</strong>${sousTitre ? `<span>${esc(sousTitre)}</span>` : ""}</figcaption>${legende}<div class="graphique-svg">${svg}</div>${tableau ? `<details class="graphique-donnees"><summary>Voir les données</summary>${tableau}</details>` : ""}</figure>`;
}
const legende = (items) => `<ul class="legende" aria-hidden="true">${items.map(([c, l, t]) => `<li><span class="puce g-${c}${t ? " tirets" : ""}"></span>${esc(l)}</li>`).join("")}</ul>`;
const table = (titres, lignes) => `<table class="tableau-donnees"><thead><tr>${titres.map((t) => `<th scope="col">${esc(t)}</th>`).join("")}</tr></thead><tbody>${lignes.map((l) => `<tr>${l.map((c, i) => (i ? `<td>${c}</td>` : `<th scope="row">${c}</th>`)).join("")}</tr>`).join("")}</tbody></table>`;

function miseAJour() {
  if (!D) return;
  const e = etat();
  ecrireEtat(e);
  $("#o-phi").textContent = `${e.phi} %`;
  $("#o-tm").textContent = `${fmt(e.tm, 1)} %`;
  $("#o-km").textContent = `${e.km} pb par point`;
  $("#sc-desc").textContent = SCENARIOS[e.sc]?.description || "";
  const p = versParametres(e);
  const r = simuler(D, p);
  const pib = D.ref.pib;

  // alertes
  const alertes = [];
  if (e.sc === "litteral") alertes.push("Lecture littérale : toutes les variantes et contradictions sont appliquées en même temps. C'est impossible en pratique ; ce scénario ne sert qu'à mesurer l'ampleur des doublons.");
  if (e.gr === "A" && e.sc !== "bfp") alertes.push("Seules les estimations de confiance A (montants du BFP repris tels quels) sont utilisées.");
  if (r.indicateurs.pireEcartPib < -5) alertes.push("Choc d'activité supérieur à 5 % du PIB : le modèle linéaire sous-estime probablement les effets non linéaires (faillites, confiance, marché du travail).");
  $("#sim-alerte").innerHTML = alertes.map((a) => `<p class="alerte-sim">${esc(a)}</p>`).join("");

  // tuiles
  const sous3 = r.indicateurs.soldeSous3;
  const tuiles = [
    ["Paquet en régime (2029)", `${fmt(r.brut[2029], 0)} Md€`, `${fmt(r.brut[2029] / pib[2029] * 100, 1)} % du PIB · ${r.selection.actifs.size} mesures`],
    ["Perçu en 2028", `${fmt(r.brut[2028], 0)} Md€`, `net après fuites : ${fmt(r.net[2028], 0)} Md€`],
    ["Solde public 2028", `${fmt(r.solde[2028], 1)} %`, `référence ${fmt(r.soldeRef[2028], 1)} %`],
    ["Dette publique 2031", `${fmt(r.dette[2031], 0)} %`, `référence ${fmt(r.detteRef[2031], 0)} %`],
    ["PIB 2028 / référence", `${fmtSigne(r.ecartPib[2028], 1)} %`, `croissance 2027 : ${fmt(r.croissance[2027], 1)} %, 2028 : ${fmt(r.croissance[2028], 1)} %`],
    ["Emploi 2028", `${fmtSigne(r.emploi[2028], 0)} 000`, `chômage ${fmt(r.chomage[2028], 1)} % (réf. ${fmt(D.ref.chomage[2028], 1)} %)`],
    ["Déficit sous 3 %", sous3 ? String(sous3) : "non", sous3 ? "première année" : "d'ici 2031"],
  ];
  $("#sim-tuiles").innerHTML = tuiles.map(([l, v, d]) => `<div class="tuile"><span class="tuile-label">${esc(l)}</span><span class="tuile-valeur">${esc(v)}</span><span class="tuile-detail">${esc(d)}</span></div>`).join("");

  // courbes
  const W = largeur($("#sim-g-solde"));
  const s = (cle, label, court, classe, valeurs, tirets) => ({ cle, label, court, classe, valeurs, tirets });
  carte("#sim-g-solde", "Solde des administrations publiques", "En % du PIB", courbesSvg({ titre: "Solde", annees: ANNEES, series: [s("ref", "À politique inchangée", "référence", "ref", r.soldeRef, true), s("sc", "Scénario", "scénario", "s1", r.solde)], unite: "%", decimales: 1, seuil: { valeur: -3, label: "−3 %" }, inclureZero: true }, W),
    legende([["ref", "À politique inchangée", true], ["s1", "Scénario"]]), table(["Année", "Référence", "Scénario"], ANNEES.map((a) => [a, fmt(r.soldeRef[a], 2), fmt(r.solde[a], 2)])));
  carte("#sim-g-dette", "Dette publique", "En % du PIB", courbesSvg({ titre: "Dette", annees: ANNEES, series: [s("ref", "À politique inchangée", "référence", "ref", r.detteRef, true), s("sc", "Scénario", "scénario", "s1", r.dette)], unite: "%", decimales: 1 }, W),
    legende([["ref", "À politique inchangée", true], ["s1", "Scénario"]]), table(["Année", "Référence", "Scénario"], ANNEES.map((a) => [a, fmt(r.detteRef[a], 1), fmt(r.dette[a], 1)])));
  carte("#sim-g-croissance", "Croissance du PIB en volume", "En % par an", courbesSvg({ titre: "Croissance", annees: ANNEES, series: [s("ref", "À politique inchangée", "référence", "ref", r.croissanceRef, true), s("sc", "Scénario", "scénario", "s1", r.croissance)], unite: "%", decimales: 1, inclureZero: true }, W),
    legende([["ref", "À politique inchangée", true], ["s1", "Scénario"]]), table(["Année", "Référence", "Scénario", "Écart de niveau du PIB", "Emploi (milliers)"], ANNEES.map((a) => [a, fmt(r.croissanceRef[a], 2), fmt(r.croissance[a], 2), `${fmt(r.ecartPib[a], 2)} %`, fmt(r.emploi[a], 0)])));

  // cascade 2028
  if (e.sc !== "litteral") {
    const c = cascade(D, p, 2028);
    carte("#sim-g-cascade", "Du catalogue au solde de 2028", "Milliards d'euros", cascadeSvg({ titre: "Cascade", etapes: c.etapes }, W), "",
      table(["Étape", "Md€"], c.etapes.map((x) => [esc(x.label), fmt(x.valeur / 1000, 1)])));
  } else $("#sim-g-cascade").innerHTML = "";

  // familles
  const items = r.familles.filter((f) => Math.abs(f.brut[2028]) > 100).sort((x, y) => Math.abs(y.brut[2028]) - Math.abs(x.brut[2028])).slice(0, 25).map((f) => ({ label: `${f.code} · ${f.label}`, valeur: f.brut[2028] / 1000, texteValeur: formatMeur(f.brut[2028]) }));
  carte("#sim-g-familles", "Contribution des familles en 2028", "Avant fuites et effets macroéconomiques ; les 25 plus importantes", items.length ? barresSvg({ titre: "Familles", items, partLabel: 0.5 }, W) : "<p>Aucune famille active.</p>", "",
    table(["Famille", "Md€ 2028"], items.map((i) => [esc(i.label), fmt(i.valeur, 2)])));

  // incidence
  const grp = ["D13", "D47", "D89", "D10"].filter((g) => r.incidence[g]).map((g) => ({ label: r.incidence[g].label, monetaire: Math.max(0, r.incidence[g].pctRevenuMonetaire[2029]), services: Math.max(0, r.incidence[g].pctRevenu[2029] - r.incidence[g].pctRevenuMonetaire[2029]) }));
  carte("#sim-g-incidence", "Qui paie ? Charge en 2029", "En % du revenu disponible de chaque groupe de ménages (ordre de grandeur)", grp.length ? incidenceSvg({ groupes: grp, unite: "%" }, W) : "",
    legende([["s1", "Perte de revenu"], ["s1-clair", "Moins de services"]]),
    table(["Groupe", "% revenu", "% services", "€ par ménage"], ["D13", "D47", "D89", "D10"].filter((g) => r.incidence[g]).map((g) => [esc(r.incidence[g].label), fmt(r.incidence[g].pctRevenuMonetaire[2029], 1), fmt(r.incidence[g].pctRevenu[2029] - r.incidence[g].pctRevenuMonetaire[2029], 1), fmt(r.incidence[g].parMenage[2029], 0)])));

  // liste des mesures
  const parFam = new Map();
  for (const l of r.lignes) { if (!parFam.has(l.fam)) parFam.set(l.fam, []); parFam.get(l.fam).push(l); }
  let html = `<p class="petit muet">${r.selection.actifs.size} mesures en vigueur, dont ${r.lignes.length} avec un effet chiffré. Érosion effective des impôts sur le capital : ${fmt(r.erosionEffective * 100, 0)} %.</p>`;
  for (const [code, ls] of [...parFam].sort((a, b) => a[0].localeCompare(b[0], "fr", { numeric: true }))) {
    html += `<h3 class="petit">${esc(code)} · ${esc(D.familles.get(code).label)}</h3><ul class="petit">${ls.map((l) => `<li><a href="${BASE}mesures/bfp-${String(l.id + 1).padStart(3, "0")}/">${ref(l.id)}</a> · ${esc(D.parId.get(l.id).t)} — ${formatMeur(l.brut[2028])} en 2028${l.poids < 1 ? ` (compté à ${fmt(l.poids * 100, 0)} %)` : ""}</li>`).join("")}</ul>`;
  }
  $("#sim-liste-contenu").innerHTML = html;
}

demarrer();
