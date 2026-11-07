// Configuration Eleventy 3 — « Simulation : et si la Belgique adoptait les 263 mesures ? »
import fs from "node:fs";
import { HtmlBasePlugin } from "@11ty/eleventy";
import * as G from "./src/assets/js/graphiques.js";

const PATH_PREFIX = process.env.PATH_PREFIX || "/simulation/";
const nf = (d) => new Intl.NumberFormat("fr-BE", { maximumFractionDigits: d, minimumFractionDigits: d });

export default function (eleventyConfig) {
  eleventyConfig.addPlugin(HtmlBasePlugin);

  // Fichiers statiques
  eleventyConfig.addPassthroughCopy({ "src/assets/css": "assets/css", "src/assets/js": "assets/js", "src/assets/img": "assets/img" });
  eleventyConfig.addPassthroughCopy({
    "node_modules/@fontsource-variable/inter/files/inter-latin-wght-normal.woff2": "assets/fonts/inter-latin-wght-normal.woff2",
    "node_modules/@fontsource-variable/inter/files/inter-latin-ext-wght-normal.woff2": "assets/fonts/inter-latin-ext-wght-normal.woff2",
    "node_modules/@fontsource-variable/source-serif-4/files/source-serif-4-latin-wght-normal.woff2": "assets/fonts/source-serif-4-latin-wght-normal.woff2",
    "node_modules/@fontsource-variable/source-serif-4/files/source-serif-4-latin-wght-italic.woff2": "assets/fonts/source-serif-4-latin-wght-italic.woff2",
  });
  eleventyConfig.addPassthroughCopy({ "data": "donnees/fichiers" });
  eleventyConfig.addPassthroughCopy({ "src/_generated": "assets/data" });
  eleventyConfig.addPassthroughCopy({ "src/robots.txt": "robots.txt" });

  // ---------- Filtres de mise en forme (français de Belgique) ----------
  eleventyConfig.addFilter("num", (x, d = 0) => (x === null || x === undefined || Number.isNaN(x) ? "—" : nf(d).format(x)));
  eleventyConfig.addFilter("signe", (x, d = 1) => (x === null || x === undefined ? "—" : (x > 0 ? "+" : x < 0 ? "−" : "") + nf(d).format(Math.abs(x))));
  eleventyConfig.addFilter("md", (meur, d = 1) => (meur === null || meur === undefined ? "—" : nf(d).format(meur / 1000))); // M€ -> Md€
  eleventyConfig.addFilter("meur", (x) => G.formatMeur(x));
  eleventyConfig.addFilter("pct", (x, d = 1) => (x === null || x === undefined ? "—" : nf(d).format(x) + " %"));
  eleventyConfig.addFilter("ref", (id) => `BFP-${String(id + 1).padStart(3, "0")}`);
  eleventyConfig.addFilter("refSlug", (id) => `bfp-${String(id + 1).padStart(3, "0")}`);
  eleventyConfig.addFilter("dateFr", (s) => {
    if (!s) return "";
    const p = String(s).split("-");
    const mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"];
    if (p.length === 3) return `${+p[2]} ${mois[+p[1] - 1]} ${p[0]}`.replace(/^1 /, "1er ");
    if (p.length === 2) return `${mois[+p[1] - 1]} ${p[0]}`;
    return p[0];
  });
  eleventyConfig.addFilter("json", (x) => JSON.stringify(x));
  eleventyConfig.addFilter("jsonAttr", (x) => JSON.stringify(x).replace(/'/g, "&#39;"));
  eleventyConfig.addFilter("sociopo", (slug) => `https://ouaisfieu.github.io/sociopo/notions/${slug}/`);
  eleventyConfig.addFilter("conclave", (slug) => `https://ouaisfieu.github.io/sims/conclave/mesures/${slug}.html`);
  eleventyConfig.addFilter("limit", (a, n) => (a || []).slice(0, n));
  eleventyConfig.addFilter("where", (a, k, v) => (a || []).filter((x) => x[k] === v));
  eleventyConfig.addFilter("sortBy", (a, k, desc = false) => [...(a || [])].sort((x, y) => (desc ? -1 : 1) * ((x[k] > y[k]) - (x[k] < y[k]))));
  eleventyConfig.addFilter("abs", (x) => Math.abs(x));
  eleventyConfig.addFilter("langueNom", (l) => ({ fr: "français", nl: "néerlandais", en: "anglais", "fr-nl": "français et néerlandais" }[l] || l));

  // ---------- Graphiques SVG rendus au build ----------
  eleventyConfig.addShortcode("courbes", (opts) => G.courbes(opts));
  eleventyConfig.addShortcode("cascade", (opts) => G.cascade(opts));
  eleventyConfig.addShortcode("barres", (opts) => G.barres(opts));
  eleventyConfig.addShortcode("incidence", (opts) => G.incidence(opts));

  eleventyConfig.addGlobalData("pathPrefix", PATH_PREFIX);
  eleventyConfig.addGlobalData("maj", "2026-11-06");

  // Vérifie que les données générées existent (npm run data)
  if (!fs.existsSync("src/_generated/simulation.json")) {
    console.warn("[simulation] src/_generated/simulation.json absent : lancer d'abord « npm run data ».");
  }

  return {
    dir: { input: "src", includes: "_includes", data: "_data", output: "_site" },
    pathPrefix: PATH_PREFIX,
    templateFormats: ["njk", "md", "11ty.js"],
    markdownTemplateEngine: "njk",
    htmlTemplateEngine: "njk",
  };
}
