// Contrôle du site construit (_site) : liens internes, ancres, titres, valeurs non calculées,
// et liens vers les projets liés limités aux pages vérifiées (data/liens.json).
// Usage : node tools/check.mjs   (après npm run build)
import fs from "node:fs";
import path from "node:path";

const SITE = "_site";
const PREFIXE = "/simulation/";
const liens = JSON.parse(fs.readFileSync("data/liens.json", "utf8"));
const sociopoOk = new Set([...Object.keys(liens.sociopo).map((s) => `notions/${s}/`), ...liens.dossiersSociopo.map((s) => `dossiers/${s}/`), ""]);
const conclaveOk = new Set(Object.values(liens.conclave).map((s) => `${s}.html`));
conclaveOk.add("");

const fichiers = [];
(function parcourir(dir) {
  for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) { if (e.name !== "pagefind") parcourir(p); }
    else if (e.name.endsWith(".html")) fichiers.push(p);
  }
})(SITE);

const cacheIds = new Map();
const ids = (fichier) => {
  if (!cacheIds.has(fichier)) {
    const html = fs.readFileSync(fichier, "utf8");
    cacheIds.set(fichier, new Set([...html.matchAll(/\sid="([^"]+)"/g)].map((m) => m[1])));
  }
  return cacheIds.get(fichier);
};
const cible = (url) => {
  let p = decodeURI(url.slice(PREFIXE.length));
  if (p === "" || p.endsWith("/")) p += "index.html";
  return path.join(SITE, p);
};

const erreurs = [];
let nLiens = 0;
for (const f of fichiers) {
  const html = fs.readFileSync(f, "utf8");
  const rel = path.relative(SITE, f);
  // Titres et structure
  const h1 = (html.match(/<h1[\s>]/g) || []).length;
  if (!/<title>[^<]+<\/title>/.test(html)) erreurs.push(`${rel} : pas de <title>`);
  if (h1 !== 1) erreurs.push(`${rel} : ${h1} titres h1`);
  // Valeurs non calculées dans le texte visible
  const texte = html.replace(/<script[\s\S]*?<\/script>/g, "").replace(/<[^>]+>/g, " ");
  for (const motif of [/\bNaN\b/, /\bundefined\b/, /\[object Object\]/, /\bInfinity\b/]) {
    const m = texte.match(motif);
    if (m) erreurs.push(`${rel} : « ${m[0]} » dans le texte`);
  }
  // Liens sans texte accessible
  for (const m of html.matchAll(/<a\b([^>]*)>((?:(?!<\/a>)[\s\S])*)<\/a>/g)) {
    const visible = m[2].replace(/<[^>]+>/g, "").trim();
    if (!visible && !/aria-label=/.test(m[1]) && !/<svg|<img/.test(m[2])) erreurs.push(`${rel} : lien sans texte ${m[1].trim().slice(0, 80)}`);
  }
  // Liens
  for (const m of html.matchAll(/\s(?:href|src)="([^"]+)"/g)) {
    const url = m[1].replace(/&amp;/g, "&");
    nLiens++;
    if (/^(mailto:|tel:|data:|javascript:)/.test(url)) continue;
    if (url.startsWith("#")) {
      if (url.length > 1 && !ids(f).has(decodeURIComponent(url.slice(1)))) erreurs.push(`${rel} : ancre absente ${url}`);
      continue;
    }
    if (url.startsWith("https://ouaisfieu.github.io/sociopo/")) {
      const reste = url.slice("https://ouaisfieu.github.io/sociopo/".length).split("#")[0];
      if (!sociopoOk.has(reste)) erreurs.push(`${rel} : notice Sociopo non vérifiée ${url}`);
      continue;
    }
    if (url.startsWith("https://ouaisfieu.github.io/sims/conclave/mesures/")) {
      const reste = url.slice("https://ouaisfieu.github.io/sims/conclave/mesures/".length).split("#")[0];
      if (!conclaveOk.has(reste)) erreurs.push(`${rel} : fiche Fumée blanche non vérifiée ${url}`);
      continue;
    }
    if (/^https?:\/\//.test(url)) continue;
    if (!url.startsWith(PREFIXE)) { erreurs.push(`${rel} : lien sans préfixe ${url}`); continue; }
    const [chemin, ancre] = url.split("#");
    const sansRequete = chemin.split("?")[0];
    if (sansRequete.startsWith(`${PREFIXE}pagefind/`)) continue; // index généré par Pagefind
    const fc = cible(sansRequete);
    if (!fs.existsSync(fc)) { erreurs.push(`${rel} : lien cassé ${url}`); continue; }
    if (ancre && fc.endsWith(".html") && !ids(fc).has(decodeURIComponent(ancre))) erreurs.push(`${rel} : ancre absente ${url}`);
  }
}

// Fichiers attendus
for (const f of ["index.html", "404.html", "sitemap.xml", "robots.txt", "llms.txt", "assets/data/simulation.json", "donnees/fichiers/export/mesures.csv"]) {
  if (!fs.existsSync(path.join(SITE, f))) erreurs.push(`fichier manquant : ${f}`);
}
// Chaque source du fichier de données figure sur la page Sources
const pageSources = fs.readFileSync(path.join(SITE, "sources/index.html"), "utf8");
for (const src of JSON.parse(fs.readFileSync("data/sources.json", "utf8"))) {
  if (!pageSources.includes(`id="src-${src.cle}"`)) erreurs.push(`source absente de la page Sources : ${src.cle}`);
}
const nFiches = fs.readdirSync(path.join(SITE, "mesures")).filter((d) => d.startsWith("bfp-")).length;
if (nFiches !== 263) erreurs.push(`${nFiches} fiches de mesures au lieu de 263`);

console.log(`${fichiers.length} pages, ${nLiens} liens examinés, ${nFiches} fiches de mesures.`);
if (erreurs.length) {
  console.error(`${erreurs.length} problème(s) :`);
  for (const e of erreurs.slice(0, 80)) console.error(`  - ${e}`);
  process.exit(1);
}
console.log("Aucun problème détecté.");
