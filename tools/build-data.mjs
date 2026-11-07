// Génère les données dérivées à partir de data/*.json (aucune dépendance) :
//  - src/_generated/simulation.json : paquet compact chargé par le simulateur dans le navigateur
//  - data/export/mesures.json et mesures.csv : jeu de données ouvert, fusion BFP + couche éditoriale
import fs from "node:fs";

const lire = (f) => JSON.parse(fs.readFileSync(`data/${f}`, "utf8"));
const bfp = lire("mesures-bfp.json");
const ed = lire("editorial.json");
const base = lire("base.json");
const hyp = lire("hypotheses.json");
const liens = lire("liens.json");

fs.mkdirSync("src/_generated", { recursive: true });
fs.mkdirSync("data/export", { recursive: true });

const edMap = new Map(ed.mesures.map((m) => [m.id, m]));
const compact = {
  version: "2026-11-06",
  bfp: { mesures: bfp.mesures.map((m) => ({ id: m.id, ref: m.ref, montant2029: m.montant2029, langue: m.langue })) },
  editorial: {
    familles: ed.familles.map(({ code, label, groupe, mode, choix, absorbe, recouvrement, membres }) => ({ code, label, groupe, mode, choix, absorbe, recouvrement, membres })),
    contradictions: ed.contradictions,
    mesures: ed.mesures.map(({ id, fam, t, typ, est, ph, gr, mc, inc, comp, dl }) => ({ id, fam, t, typ, est, ph, gr, mc, inc, comp, dl })),
  },
  base, hyp,
};
fs.writeFileSync("src/_generated/simulation.json", JSON.stringify(compact));

// Jeu de données ouvert
const fusion = bfp.mesures.map((b) => {
  const e = edMap.get(b.id);
  return {
    ref: b.ref, id: b.id, categorie: b.categorie, sousCategorie: b.sousCategorie, langue: b.langue,
    description: b.description, modalites: b.modalites, motivation: b.motivation,
    montantBfp2029: b.montant2029, sourceChiffrage: b.sourceChiffrage,
    titreCourt: e.t, titreFr: e.tf || (b.langue === "fr" ? b.description : null), resume: e.res,
    famille: e.fam, type: e.typ, estimationBas: e.est.bas, estimationCentrale: e.est.central, estimationHaut: e.est.haut,
    part2027: e.ph[0], part2028: e.ph[1], confiance: e.gr, multiplicateur: e.mc, incidence: e.inc,
    competence: e.comp, vehicule: e.veh, delai: e.dl, note: e.note, sources: e.src.join(" "),
    ficheConclave: `https://ouaisfieu.github.io/sims/conclave/mesures/${liens.conclave[b.id]}.html`,
    fiche: `https://ouaisfieu.github.io/simulation/mesures/${b.ref.toLowerCase()}/`,
  };
});
fs.writeFileSync("data/export/mesures.json", JSON.stringify({ meta: { ...bfp.meta, couche: "Couche éditoriale du site (CC BY 4.0)" }, mesures: fusion }, null, 1));
const cols = Object.keys(fusion[0]);
const q = (v) => (v === null || v === undefined ? "" : /[";\n,]/.test(String(v)) ? `"${String(v).replace(/"/g, '""')}"` : String(v));
fs.writeFileSync("data/export/mesures.csv", "﻿" + [cols.join(","), ...fusion.map((r) => cols.map((c) => q(r[c])).join(","))].join("\n"));
console.log(`simulation.json : ${(fs.statSync("src/_generated/simulation.json").size / 1024).toFixed(0)} Ko ; mesures.csv : ${fusion.length} lignes`);
