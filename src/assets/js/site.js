// Comportements communs : thème, infobulles des graphiques, réticule.
const racine = document.documentElement;

// Thème clair / sombre, mémorisé dans ce navigateur seulement
const bouton = document.getElementById("bascule-theme");
if (bouton) {
  bouton.addEventListener("click", () => {
    const sombreSysteme = matchMedia("(prefers-color-scheme: dark)").matches;
    const actuel = racine.getAttribute("data-theme") || (sombreSysteme ? "dark" : "light");
    const suivant = actuel === "dark" ? "light" : "dark";
    racine.setAttribute("data-theme", suivant);
    try { localStorage.setItem("simulation-theme", suivant); } catch (e) { /* stockage indisponible */ }
  });
}

// Infobulles : tout élément SVG portant data-tip
const bulle = document.createElement("div");
bulle.className = "infobulle";
bulle.setAttribute("role", "status");
document.body.appendChild(bulle);
function placer(e) {
  const x = e.clientX, y = e.clientY;
  const w = bulle.offsetWidth, h = bulle.offsetHeight;
  let gx = x + 14, gy = y + 14;
  if (gx + w > innerWidth - 8) gx = x - w - 14;
  if (gy + h > innerHeight - 8) gy = y - h - 14;
  bulle.style.left = `${Math.max(8, gx)}px`;
  bulle.style.top = `${Math.max(8, gy)}px`;
}
document.addEventListener("pointerover", (e) => {
  const cible = e.target.closest?.("[data-tip]");
  if (!cible) return;
  bulle.textContent = cible.getAttribute("data-tip");
  bulle.classList.add("visible");
  placer(e);
  const i = cible.getAttribute("data-i");
  if (i !== null) cible.closest("svg")?.querySelectorAll(`.g-reticule[data-i="${i}"]`).forEach((l) => l.classList.add("actif"));
});
document.addEventListener("pointermove", (e) => { if (bulle.classList.contains("visible")) placer(e); });
document.addEventListener("pointerout", (e) => {
  const cible = e.target.closest?.("[data-tip]");
  if (!cible) return;
  bulle.classList.remove("visible");
  cible.closest("svg")?.querySelectorAll(".g-reticule.actif").forEach((l) => l.classList.remove("actif"));
});

// Filtres de la liste des mesures
const liste = document.querySelector("[data-liste-mesures]");
if (liste) {
  const items = [...liste.querySelectorAll("li[data-texte]")];
  const champs = [...document.querySelectorAll("[data-filtre]")];
  const compteur = document.querySelector("[data-compteur]");
  const tri = document.querySelector("[data-tri]");
  const norm = (s) => s.normalize("NFD").replace(/[̀-ͯ]/g, "").toLowerCase();
  const appliquer = () => {
    const v = Object.fromEntries(champs.map((c) => [c.dataset.filtre, c.value]));
    const q = norm(v.q || "");
    let n = 0;
    for (const li of items) {
      const okQ = !q || norm(li.dataset.texte).includes(q);
      const okC = !v.categorie || li.dataset.groupe === v.categorie;
      const okT = !v.type || li.dataset.type === v.type;
      const okG = !v.grade || li.dataset.grade === v.grade;
      const okS = !v.statut || li.dataset.statut === v.statut;
      const okL = !v.langue || li.dataset.langue === v.langue;
      const vis = okQ && okC && okT && okG && okS && okL;
      li.hidden = !vis; if (vis) n++;
    }
    if (compteur) compteur.textContent = `${n} mesure${n > 1 ? "s" : ""} affichée${n > 1 ? "s" : ""} sur ${items.length}`;
    const params = new URLSearchParams();
    for (const [k, val] of Object.entries(v)) if (val) params.set(k, val);
    history.replaceState(null, "", params.toString() ? `?${params}` : location.pathname);
  };
  const trier = () => {
    const mode = tri?.value || "ref";
    const cle = (li) => mode === "montant" ? -Math.abs(+li.dataset.montant || 0) : mode === "bfp" ? -(+li.dataset.bfp || -1) : +li.dataset.id;
    items.sort((a, b) => cle(a) - cle(b)).forEach((li) => liste.appendChild(li));
  };
  const init = new URLSearchParams(location.search);
  for (const c of champs) if (init.get(c.dataset.filtre)) c.value = init.get(c.dataset.filtre);
  champs.forEach((c) => c.addEventListener("input", appliquer));
  tri?.addEventListener("change", () => { trier(); appliquer(); });
  appliquer();
}
