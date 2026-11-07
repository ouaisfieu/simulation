// Graphiques SVG sans dépendance, rendus au build (Eleventy) et dans le navigateur (simulateur).
// Les couleurs passent par des classes CSS (jetons clair/sombre) : jamais de couleur codée en dur ici.

const NF = (d) => new Intl.NumberFormat("fr-BE", { maximumFractionDigits: d, minimumFractionDigits: d });
export const fmt = (x, d = 1) => (x === null || x === undefined || Number.isNaN(x) ? "—" : NF(d).format(x).replace("-", "−"));
export const fmtSigne = (x, d = 1) => (x > 0 ? "+" : "") + fmt(x, d);
export function formatMeur(x) {
  if (x === null || x === undefined) return "—";
  return Math.abs(x) >= 1000 ? `${fmt(x / 1000, 1)} Md€` : `${fmt(x, 0)} M€`;
}
const esc = (s) => String(s ?? "").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
let compteur = 0;
const uid = (p) => `${p}-${(compteur++).toString(36)}`;

function graduations(min, max, n = 5) {
  const etendue = max - min || 1;
  const brut = etendue / n;
  const p = 10 ** Math.floor(Math.log10(brut));
  const pas = [1, 2, 2.5, 5, 10].map((k) => k * p).find((s) => etendue / s <= n) || 10 * p;
  const debut = Math.floor(min / pas) * pas;
  const fin = Math.ceil(max / pas) * pas;
  const t = [];
  for (let v = debut; v <= fin + pas / 1e6; v += pas) t.push(Math.round(v * 1e6) / 1e6);
  return t;
}

/** Deux rendus (large et étroit) dans une figure, + légende HTML + tableau des données. */
function figure({ id, titre, sousTitre, legende, svgLarge, svgEtroit, tableau, note }) {
  return `<figure class="graphique" id="${id}">
${titre ? `<figcaption class="graphique-titre"><strong>${esc(titre)}</strong>${sousTitre ? `<span>${esc(sousTitre)}</span>` : ""}</figcaption>` : ""}
${legende || ""}
<div class="graphique-svg g-large">${svgLarge}</div>
<div class="graphique-svg g-etroit">${svgEtroit}</div>
${note ? `<p class="graphique-note">${note}</p>` : ""}
${tableau ? `<details class="graphique-donnees"><summary>Voir les données</summary>${tableau}</details>` : ""}
</figure>`;
}

function legendeHtml(series) {
  if (series.length < 2) return "";
  return `<ul class="legende" aria-hidden="true">${series.map((s) => `<li><span class="puce g-${s.classe}${s.tirets ? " tirets" : ""}"></span>${esc(s.label)}</li>`).join("")}</ul>`;
}

// ---------------------------------------------------------------- Courbes
function svgCourbes(o, W) {
  const H = o.hauteur || 260;
  const etroit = W < 500;
  const m = { g: etroit ? 38 : 46, d: etroit ? 64 : 118, h: 14, b: 26 };
  const annees = o.annees;
  const toutes = o.series.flatMap((s) => annees.map((a) => s.valeurs[a]).filter((v) => v !== undefined && v !== null));
  if (o.seuil) toutes.push(o.seuil.valeur);
  if (o.bande) for (const a of annees) { for (const k of ["bas", "haut"]) { const v = o.bande[k][a]; if (v !== undefined && v !== null) toutes.push(v); } }
  let ymin = o.yMin ?? Math.min(...toutes), ymax = o.yMax ?? Math.max(...toutes);
  if (o.inclureZero) { ymin = Math.min(ymin, 0); ymax = Math.max(ymax, 0); }
  const ticks = graduations(ymin, ymax, etroit ? 4 : 5);
  ymin = ticks[0]; ymax = ticks.at(-1);
  const pasT = ticks.length > 1 ? ticks[1] - ticks[0] : 1;
  const decAxe = o.decimalesAxe ?? (pasT >= 1 - 1e-9 ? 0 : Math.abs(pasT * 10 - Math.round(pasT * 10)) < 1e-9 ? 1 : 2);
  const x = (a) => m.g + (annees.indexOf(a) / (annees.length - 1)) * (W - m.g - m.d);
  const y = (v) => m.h + (1 - (v - ymin) / (ymax - ymin)) * (H - m.h - m.b);
  const fs = etroit ? 11 : 12;
  let s = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="${esc(o.titre || "Graphique")}" class="svg-courbes" data-annees='${JSON.stringify(annees)}'>`;
  for (const t of ticks) {
    s += `<line class="${t === 0 ? "g-zero" : "g-grille"}" x1="${m.g}" x2="${W - m.d}" y1="${y(t)}" y2="${y(t)}"/>`;
    s += `<text class="g-txt2" x="${m.g - 6}" y="${y(t) + 4}" text-anchor="end" font-size="${fs}">${fmt(t, decAxe)}</text>`;
  }
  annees.forEach((a, i) => {
    if (etroit && annees.length > 6 && i % 2) return;
    s += `<text class="g-txt2" x="${x(a)}" y="${H - 6}" text-anchor="middle" font-size="${fs}">${a}</text>`;
  });
  if (o.seuil) {
    s += `<line class="g-seuil" x1="${m.g}" x2="${W - m.d}" y1="${y(o.seuil.valeur)}" y2="${y(o.seuil.valeur)}"/>`;
    s += `<text class="g-txt2" x="${W - m.d + 6}" y="${y(o.seuil.valeur) + 4}" font-size="${fs - 1}">${esc(o.seuil.label)}</text>`;
  }
  if (o.bande) { // bande d'incertitude [bas, haut]
    const pts = annees.filter((a) => o.bande.bas[a] !== undefined);
    const haut = pts.map((a) => `${x(a)},${y(o.bande.haut[a])}`).join(" ");
    const bas = pts.slice().reverse().map((a) => `${x(a)},${y(o.bande.bas[a])}`).join(" ");
    s += `<polygon class="g-bande g-${o.bande.classe || "s1"}" points="${haut} ${bas}"/>`;
  }
  // étiquettes de fin sans chevauchement
  const fins = o.series.map((serie) => {
    const dern = annees.filter((a) => serie.valeurs[a] !== undefined && serie.valeurs[a] !== null).at(-1);
    return { serie, a: dern, yv: y(serie.valeurs[dern]) };
  }).sort((p, q) => p.yv - q.yv);
  for (let i = 1; i < fins.length; i++) if (fins[i].yv - fins[i - 1].yv < 15) fins[i].yv = fins[i - 1].yv + 15;
  for (const serie of o.series) {
    const pts = annees.filter((a) => serie.valeurs[a] !== undefined && serie.valeurs[a] !== null);
    const d = pts.map((a, i) => `${i ? "L" : "M"}${x(a).toFixed(1)},${y(serie.valeurs[a]).toFixed(1)}`).join(" ");
    s += `<path class="g-ligne g-${serie.classe}${serie.tirets ? " tirets" : ""}" d="${d}"/>`;
    for (const a of pts) s += `<circle class="g-point g-${serie.classe}" cx="${x(a).toFixed(1)}" cy="${y(serie.valeurs[a]).toFixed(1)}" r="${serie.tirets ? 3 : 4}"/>`;
  }
  for (const f of fins) {
    const v = f.serie.valeurs[f.a];
    s += `<text class="g-txt" x="${x(f.a) + 8}" y="${f.yv + 4}" font-size="${fs}"><tspan font-weight="600">${fmt(v, o.decimales ?? 1)}${o.unite === "%" ? " %" : ""}</tspan>${etroit ? "" : ` <tspan class="g-txt2">${esc(f.serie.court || f.serie.label)}</tspan>`}</text>`;
  }
  // couche de survol : une zone par année
  const pas = (W - m.g - m.d) / (annees.length - 1);
  annees.forEach((a, i) => {
    const lignes = o.series.filter((sr) => sr.valeurs[a] !== undefined && sr.valeurs[a] !== null)
      .map((sr) => `${sr.label} : ${fmt(sr.valeurs[a], o.decimales ?? 1)}${o.unite === "%" ? " %" : ` ${o.unite || ""}`}`);
    const tip = [String(a), ...lignes].join("\n");
    s += `<line class="g-reticule" data-i="${i}" x1="${x(a)}" x2="${x(a)}" y1="${m.h}" y2="${H - m.b}"/>`;
    s += `<rect class="g-zone" data-i="${i}" data-tip="${esc(tip)}" x="${Math.max(m.g - pas / 2, x(a) - pas / 2)}" y="${m.h}" width="${pas}" height="${H - m.h - m.b}"/>`;
  });
  return s + "</svg>";
}

function tableCourbes(o) {
  return `<table class="tableau-donnees"><thead><tr><th scope="col">Année</th>${o.series.map((s) => `<th scope="col">${esc(s.label)}</th>`).join("")}</tr></thead><tbody>${o.annees.map((a) => `<tr><th scope="row">${a}</th>${o.series.map((s) => `<td>${s.valeurs[a] === undefined || s.valeurs[a] === null ? "—" : fmt(s.valeurs[a], o.decimales ?? 1)}</td>`).join("")}</tr>`).join("")}</tbody></table>`;
}

export function courbes(o) {
  return figure({ id: o.id || uid("courbes"), titre: o.titre, sousTitre: o.sousTitre, legende: legendeHtml(o.series), note: o.note,
    svgLarge: svgCourbes(o, 720), svgEtroit: svgCourbes(o, 360), tableau: tableCourbes(o) });
}
export const courbesSvg = svgCourbes;

// ---------------------------------------------------------------- Cascade
function svgCascade(o, W) {
  const etroit = W < 500;
  const e = o.etapes;
  const lh = etroit ? 50 : 30;
  const labelW = etroit ? 0 : Math.round(W * 0.46);
  const m = { g: etroit ? 8 : labelW + 10, d: etroit ? 70 : 84, h: 6 };
  const H = m.h + e.length * lh + 22;
  let cum = 0; const barres = [];
  for (const et of e) {
    if (et.type === "total") { barres.push({ ...et, de: 0, a: et.valeur }); cum = et.valeur; }
    else { barres.push({ ...et, de: cum, a: cum + et.valeur }); cum += et.valeur; }
  }
  const vals = barres.flatMap((b) => [b.de, b.a, 0]);
  const vmin = Math.min(...vals), vmax = Math.max(...vals);
  const x = (v) => m.g + ((v - vmin) / (vmax - vmin || 1)) * (W - m.g - m.d);
  const fs = etroit ? 11.5 : 12.5;
  let s = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="${esc(o.titre || "Cascade")}" class="svg-cascade">`;
  s += `<line class="g-zero" x1="${x(0)}" x2="${x(0)}" y1="${m.h}" y2="${H - 18}"/>`;
  barres.forEach((b, i) => {
    const y0 = m.h + i * lh + (etroit ? 18 : 5);
    const bh = etroit ? 20 : 20;
    const xa = Math.min(x(b.de), x(b.a)), xb = Math.max(x(b.de), x(b.a));
    const cls = b.type === "total" ? "g-tot" : b.valeur >= 0 ? "g-pos" : "g-neg";
    const lab = etroit
      ? `<text class="g-txt" x="${m.g}" y="${y0 - 5}" font-size="${fs}">${esc(b.label)}</text>`
      : `<text class="g-txt${b.type === "total" ? " gras" : ""}" x="${labelW}" y="${y0 + 14}" text-anchor="end" font-size="${fs}">${esc(b.label)}</text>`;
    const val = `${b.type === "total" ? "" : b.valeur >= 0 ? "+" : ""}${fmt(b.valeur / 1000, 1)} Md€`;
    s += lab;
    s += `<rect class="${cls}" x="${xa}" y="${y0}" width="${Math.max(2, xb - xa)}" height="${bh}" rx="3" data-tip="${esc(`${b.label}\n${val}`)}"/>`;
    s += `<text class="g-txt${b.type === "total" ? " gras" : ""}" x="${xb + 6}" y="${y0 + 14}" font-size="${fs}">${val}</text>`;
    if (i < barres.length - 1 && barres[i + 1].type !== "total") {
      s += `<line class="g-lien" x1="${x(b.a)}" x2="${x(b.a)}" y1="${y0 + bh}" y2="${y0 + lh + (etroit ? 0 : 0)}"/>`;
    }
  });
  return s + "</svg>";
}
export function cascade(o) {
  const tab = `<table class="tableau-donnees"><thead><tr><th scope="col">Étape</th><th scope="col">Montant (Md€)</th></tr></thead><tbody>${o.etapes.map((e) => `<tr><th scope="row">${esc(e.label)}</th><td>${e.type === "total" ? "" : e.valeur >= 0 ? "+" : ""}${fmt(e.valeur / 1000, 1)}</td></tr>`).join("")}</tbody></table>`;
  return figure({ id: o.id || uid("cascade"), titre: o.titre, sousTitre: o.sousTitre, note: o.note, svgLarge: svgCascade(o, 720), svgEtroit: svgCascade(o, 360), tableau: tab });
}
export const cascadeSvg = svgCascade;

// ---------------------------------------------------------------- Barres horizontales
function svgBarres(o, W) {
  const etroit = W < 500;
  const items = o.items;
  const lh = etroit ? 44 : 26;
  const labelW = etroit ? 0 : Math.round(W * (o.partLabel || 0.42));
  const m = { g: etroit ? 8 : labelW + 10, d: etroit ? 66 : 76, h: 4 };
  const H = m.h + items.length * lh + 8;
  const vals = items.map((i) => i.valeur).concat([0]);
  const vmin = Math.min(...vals), vmax = Math.max(...vals);
  const x = (v) => m.g + ((v - vmin) / (vmax - vmin || 1)) * (W - m.g - m.d);
  const fs = etroit ? 11.5 : 12.5;
  let s = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="${esc(o.titre || "Barres")}" class="svg-barres">`;
  s += `<line class="g-zero" x1="${x(0)}" x2="${x(0)}" y1="${m.h}" y2="${H - 4}"/>`;
  items.forEach((it, i) => {
    const y0 = m.h + i * lh + (etroit ? 18 : 4);
    const bh = 18;
    const xa = Math.min(x(0), x(it.valeur)), xb = Math.max(x(0), x(it.valeur));
    const cls = it.classe || (it.valeur >= 0 ? "g-s1" : "g-neg");
    const lab = esc(it.label);
    const labHtml = it.href ? `<a href="${esc(it.href)}">${lab}</a>` : lab;
    s += etroit
      ? `<text class="g-txt" x="${m.g}" y="${y0 - 5}" font-size="${fs}">${labHtml}</text>`
      : `<text class="g-txt" x="${labelW}" y="${y0 + 13}" text-anchor="end" font-size="${fs}">${labHtml}</text>`;
    s += `<rect class="${cls}" x="${xa}" y="${y0}" width="${Math.max(2, xb - xa)}" height="${bh}" rx="3" data-tip="${esc(`${it.label}\n${it.texteValeur || fmt(it.valeur, o.decimales ?? 1)}`)}"/>`;
    s += `<text class="g-txt" x="${(it.valeur >= 0 ? xb : xb) + 6}" y="${y0 + 13}" font-size="${fs}">${esc(it.texteValeur || fmt(it.valeur, o.decimales ?? 1))}</text>`;
  });
  return s + "</svg>";
}
export function barres(o) {
  const tab = `<table class="tableau-donnees"><thead><tr><th scope="col">${esc(o.colonne || "Élément")}</th><th scope="col">${esc(o.unite || "Valeur")}</th></tr></thead><tbody>${o.items.map((i) => `<tr><th scope="row">${esc(i.label)}</th><td>${esc(i.texteValeur || fmt(i.valeur, o.decimales ?? 1))}</td></tr>`).join("")}</tbody></table>`;
  return figure({ id: o.id || uid("barres"), titre: o.titre, sousTitre: o.sousTitre, note: o.note, legende: o.legende || "", svgLarge: svgBarres(o, 720), svgEtroit: svgBarres(o, 360), tableau: tab });
}
export const barresSvg = svgBarres;

// ---------------------------------------------------------------- Incidence (barres empilées : revenu + services)
function svgIncidence(o, W) {
  const etroit = W < 500;
  const lh = etroit ? 48 : 34;
  const labelW = etroit ? 0 : 150;
  const m = { g: etroit ? 8 : labelW + 12, d: etroit ? 70 : 90, h: 4 };
  const H = m.h + o.groupes.length * lh + 8;
  const max = Math.max(...o.groupes.map((g) => g.monetaire + g.services), 1);
  const x = (v) => m.g + (v / max) * (W - m.g - m.d);
  const fs = etroit ? 11.5 : 12.5;
  let s = `<svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="${esc(o.titre || "Incidence")}" class="svg-incidence">`;
  o.groupes.forEach((g, i) => {
    const y0 = m.h + i * lh + (etroit ? 20 : 7);
    const bh = 20;
    s += etroit
      ? `<text class="g-txt" x="${m.g}" y="${y0 - 6}" font-size="${fs}">${esc(g.label)}</text>`
      : `<text class="g-txt" x="${labelW}" y="${y0 + 14}" text-anchor="end" font-size="${fs}">${esc(g.label)}</text>`;
    const w1 = Math.max(0, x(g.monetaire) - x(0));
    const w2 = Math.max(0, x(g.monetaire + g.services) - x(g.monetaire));
    const tip = `${g.label}\nRevenu : ${fmt(g.monetaire, 1)} ${o.unite}\nServices : ${fmt(g.services, 1)} ${o.unite}`;
    if (w1 > 0) s += `<rect class="g-s1" x="${x(0)}" y="${y0}" width="${w1}" height="${bh}" rx="3" data-tip="${esc(tip)}"/>`;
    if (w2 > 0) s += `<rect class="g-s1-clair" x="${x(g.monetaire) + (w1 > 0 ? 2 : 0)}" y="${y0}" width="${Math.max(0, w2 - (w1 > 0 ? 2 : 0))}" height="${bh}" rx="3" data-tip="${esc(tip)}"/>`;
    s += `<text class="g-txt" x="${x(g.monetaire + g.services) + 6}" y="${y0 + 14}" font-size="${fs}"><tspan font-weight="600">${fmt(g.monetaire + g.services, 1)}</tspan> ${esc(o.unite)}</text>`;
  });
  return s + "</svg>";
}
export function incidence(o) {
  const leg = `<ul class="legende" aria-hidden="true"><li><span class="puce g-s1"></span>${esc(o.labelMonetaire || "Perte de revenu")}</li><li><span class="puce g-s1-clair"></span>${esc(o.labelServices || "Moins de services (santé, services publics)")}</li></ul>`;
  const tab = `<table class="tableau-donnees"><thead><tr><th scope="col">Groupe</th><th scope="col">Revenu</th><th scope="col">Services</th><th scope="col">Total</th></tr></thead><tbody>${o.groupes.map((g) => `<tr><th scope="row">${esc(g.label)}</th><td>${fmt(g.monetaire, 1)}</td><td>${fmt(g.services, 1)}</td><td>${fmt(g.monetaire + g.services, 1)}</td></tr>`).join("")}</tbody></table>`;
  return figure({ id: o.id || uid("incidence"), titre: o.titre, sousTitre: o.sousTitre, note: o.note, legende: leg, svgLarge: svgIncidence(o, 720), svgEtroit: svgIncidence(o, 360), tableau: tab });
}
export const incidenceSvg = svgIncidence;
