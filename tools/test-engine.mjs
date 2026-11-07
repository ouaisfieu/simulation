// Tests de cohérence du moteur + impression des scénarios de référence.
import fs from "node:fs";
import { preparer, parametres, simuler, cascade, paquetSuffisant, ANNEES } from "../src/assets/js/moteur.js";

const lire = (f) => JSON.parse(fs.readFileSync(new URL(`../data/${f}`, import.meta.url)));
const d = preparer(lire("mesures-bfp.json"), lire("editorial.json"), lire("base.json"), lire("hypotheses.json"));
const fmt = (x, n = 1) => (x >= 0 ? " " : "") + x.toFixed(n);
let echecs = 0;
const ok = (cond, msg) => { if (!cond) { echecs++; console.error("ÉCHEC :", msg); } };

// 1. Référence : sans mesure, la simulation reproduit la trajectoire de base
const vide = simuler(d, parametres("pmc", { desactives: d.mesures.map((m) => m.id) }));
for (const a of ANNEES) {
  ok(Math.abs(vide.solde[a] - d.ref.solde[a]) < 1e-9, `solde de référence ${a}`);
  ok(Math.abs(vide.dette[a] - d.ref.dette[a]) < 1e-9, `dette de référence ${a}`);
}

// 2. Somme naïve
const naif = d.mesures.reduce((s, m) => s + (m.bfp || 0), 0);
ok(naif === 135489, `somme naïve ${naif}`);

for (const sc of ["bfp", "med", "pmc", "litteral"]) {
  const r = simuler(d, parametres(sc));
  console.log(`\n=== ${sc} : ${r.selection.actifs.size} mesures actives`);
  console.log("année  brut(Md€) net    écartPIB  croiss  solde (réf)     dette (réf)     emploi(k)  chômage");
  for (const a of ANNEES) {
    console.log(`${a}  ${fmt(r.brut[a])}  ${fmt(r.net[a])}  ${fmt(r.ecartPib[a], 2)}%  ${fmt(r.croissance[a], 2)}  ${fmt(r.solde[a], 2)} (${fmt(r.soldeRef[a], 1)})  ${fmt(r.dette[a], 1)} (${fmt(r.detteRef[a], 1)})  ${fmt(r.emploi[a], 0)}  ${r.chomage[a].toFixed(1)}`);
  }
  console.log("indicateurs", r.indicateurs);
  if (sc === "pmc") {
    console.log("familles (brut 2029, M€) :");
    for (const f of r.familles.slice(0, 40)) console.log(`  ${f.code.padEnd(5)} ${f.label.slice(0, 55).padEnd(55)} ${Math.round(f.brut[2029]).toString().padStart(7)}  (2028 : ${Math.round(f.brut[2028])})`);
    console.log("incidence 2029 :");
    for (const [g, v] of Object.entries(r.incidence)) console.log(`  ${g.padEnd(4)} ${Math.round(v.total[2029])} M€` + (v.parMenage ? `  ${Math.round(v.parMenage[2029])} €/ménage (dont monétaire ${Math.round(v.parMenageMonetaire[2029])})  ${v.pctRevenu[2029].toFixed(1)} % du revenu (monétaire ${v.pctRevenuMonetaire[2029].toFixed(1)} %)` : ""));
    console.log("érosion effective", r.erosionEffective, r.famillesCapitalActives);
  }
}

for (const an of [2028, 2029]) {
  const c = cascade(d, parametres("pmc"), an);
  console.log(`\ncascade ${an} (M€)`);
  for (const e of c.etapes) console.log(`  ${e.type === "total" ? "=" : "+"} ${e.label.padEnd(55)} ${Math.round(e.valeur)}`);
  // la cascade doit se refermer
  const debut = c.etapes.find((e) => e.cle === "pmc").valeur;
  const deltas = c.etapes.slice(c.etapes.findIndex((e) => e.cle === "pmc") + 1, -1).reduce((s, e) => s + e.valeur, 0);
  ok(Math.abs(debut + deltas - c.etapes.at(-1).valeur) < 1, `cascade ${an} refermée (${debut + deltas} vs ${c.etapes.at(-1).valeur})`);
}

// 3. Sensibilité
for (const [lab, pr] of [["doux + haut", { macro: "doux", niveau: "haut", fuite: "doux", erosion: "doux" }], ["sévère + bas", { macro: "severe", niveau: "bas", fuite: "severe", erosion: "severe" }]]) {
  const r = simuler(d, parametres("pmc", pr));
  console.log(`\n${lab} : solde 2028 ${r.solde[2028].toFixed(2)} ; 2031 ${r.solde[2031].toFixed(2)} ; dette 2031 ${r.dette[2031].toFixed(1)} ; écart PIB min ${r.indicateurs.pireEcartPib.toFixed(2)} ; emploi min ${Math.round(r.indicateurs.pireEmploi)}`);
}
for (const crit of ["recessif", "rendement"]) {
  const ps = paquetSuffisant(d, parametres("pmc"), { seuil: -3, annee: 2028, critere: crit });
  console.log(`\npaquet suffisant (${crit}) : ${ps.familles.length} familles, atteint=${ps.atteint}, solde 2028 ${ps.resultat.solde[2028].toFixed(2)}, écart PIB 2028 ${ps.resultat.ecartPib[2028].toFixed(2)}, emploi ${Math.round(ps.resultat.emploi[2028])}`);
  console.log("  " + ps.familles.map((f) => `${f.code} (${Math.round(f.net)})`).join(", "));
}
// 4. Le paquet compact chargé par le navigateur reproduit les chiffres des pages statiques
const bundle = new URL("../src/_generated/simulation.json", import.meta.url);
if (fs.existsSync(bundle)) {
  const b = JSON.parse(fs.readFileSync(bundle));
  const dB = preparer(b.bfp, b.editorial, b.base, b.hyp);
  for (const sc of ["pmc", "med", "bfp", "litteral"]) {
    for (const extra of [{}, { macro: "severe", niveau: "haut" }, { gradeMax: "B" }]) {
      const r1 = simuler(d, parametres(sc, extra)); const r2 = simuler(dB, parametres(sc, extra));
      for (const a of ANNEES) for (const k of ["brut", "solde", "dette", "ecartPib"]) {
        ok(Math.abs(r1[k][a] - r2[k][a]) < 1e-9, `paquet navigateur ${sc} ${JSON.stringify(extra)} ${k} ${a}`);
      }
    }
  }
  console.log("\npaquet navigateur : identique aux données complètes");
} else console.log("\n(paquet navigateur absent : lancer npm run data pour le tester)");

if (echecs) { console.error(`${echecs} échec(s)`); process.exit(1); }
console.log("\nTous les tests passent.");
