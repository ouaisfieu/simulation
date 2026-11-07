# Et si la Belgique adoptait les 263 mesures ?

Encyclopédie et simulateur citoyens du catalogue « Options de politiques pour l'élaboration du budget 2027 », publié en juin 2026 par le Bureau fédéral du Plan (BFP). Le site examine une hypothèse : la Belgique adopte en 2027 et 2028, puis maintient, l'ensemble des 263 mesures. Que rapporteraient-elles ? Que coûteraient-elles en activité et en emplois ? Qui paierait ? Le résultat serait-il soutenable ?

Site publié : <https://ouaisfieu.github.io/simulation/>

## Contenu

- **Le dossier** (`src/dossier/`) : huit chapitres, de l'hypothèse à la soutenabilité.
- **Le simulateur** (`src/simulateur/`, `src/assets/js/simulateur.js`) : choix des variantes par famille, hypothèses macroéconomiques, filtre « BFP seul », état partageable dans l'adresse.
- **Les 263 fiches de mesures** et les 57 familles, générées depuis les données.
- **Les modules** : contradictions, incidence (« Qui paie ? »), précédent de 1993-2000, comparaisons européennes, contexte, méthode, sources, glossaire, données ouvertes, projets liés.

## Construire le site

Il faut Node 20 ou plus récent (voir `.nvmrc`).

```sh
npm ci
npm run build    # données dérivées, puis Eleventy, puis l'index de recherche Pagefind
npm run check    # liens internes, ancres, titres, valeurs non calculées
npm test         # build, tests du moteur et contrôles
npm run dev      # serveur local avec rechargement : http://localhost:8080/simulation/
```

Le site est construit pour le préfixe `/simulation/` (constante `PATH_PREFIX` dans `eleventy.config.js`).

## Publier sur GitHub Pages

1. Créer le dépôt vide `simulation` sur le compte `ouaisfieu` (sans README).
2. Pousser ce dossier sur la branche `main` :

   ```sh
   cd simulation
   git init -b main
   git add .
   git commit -m "Première version du site"
   git remote add origin https://github.com/ouaisfieu/simulation.git
   git push -u origin main
   ```

   Par l'interface web de GitHub (« Add file → Upload files »), veiller à envoyer aussi le dossier masqué `.github` : sans lui, rien n'est publié. Sur macOS, Cmd + Maj + . affiche les fichiers masqués dans le Finder.
3. Dans le dépôt : **Settings → Pages → Build and deployment → Source : GitHub Actions**.
4. Le flux `.github/workflows/deploy.yml` construit, teste et publie le site à chaque poussée sur `main`. Le site apparaît à l'adresse <https://ouaisfieu.github.io/simulation/> après deux à trois minutes (onglet **Actions** pour suivre).

## Organisation

| Chemin | Rôle |
|---|---|
| `data/mesures-bfp.json` | Extraction brute du classeur du BFP (263 mesures), avec l'empreinte SHA-256 du fichier source |
| `data/editorial.json` | Grille éditoriale : type, famille, estimations gradées, montée en charge, compétence… |
| `data/base.json` | Trajectoire de référence 2025-2031 (BNB et BFP, juin 2026), budget 2026, règles européennes |
| `data/hypotheses.json` | Hypothèses du modèle : multiplicateurs, fuites, érosion, marchés, incidence, scénarios |
| `data/sources.json`, `data/liens.json`, `data/conclave-analyse.json` | Sources, correspondances avec les projets liés |
| `src/assets/js/moteur.js` | Moteur de simulation, module ES sans dépendance, exécuté au build et dans le navigateur |
| `src/assets/js/graphiques.js` | Graphiques SVG (courbes, cascade, barres, incidence), rendus au build et dans le navigateur |
| `src/_data/sim.js` | Précalcul des scénarios pour les pages statiques |
| `tools/extract_bfp.py` | Extraction du classeur XLSX vers `data/mesures-bfp.json` |
| `tools/editorial/` | Sources Python de la grille éditoriale ; `python3 tools/editorial/build.py` régénère `data/editorial.json` et `data/sources.json` |
| `tools/build-data.mjs` | Paquet compact du simulateur et export ouvert (JSON, CSV) |
| `tools/test-engine.mjs`, `tools/check.mjs` | Tests du moteur et contrôle du site construit |

## Mettre à jour

- **Une estimation ou une fiche** : modifier l'entrée dans `tools/editorial/mesures_*.py`, puis lancer `python3 tools/editorial/build.py` (le script valide la couverture des 263 mesures, les familles, les sources et les niveaux de confiance), puis `npm test`.
- **La trajectoire de référence** : modifier `data/base.json` (signaler les valeurs interpolées dans `estimationSite`).
- **Les hypothèses** : modifier `data/hypotheses.json` ; toutes sont aussi réglables dans le simulateur.
- **La date de mise à jour** : constante `maj` dans `eleventy.config.js`, bandeau dans `src/_includes/layouts/base.njk`.

## Licences

- Code : MIT.
- Textes, traductions, estimations et données propres au site : CC BY 4.0.
- Les textes et montants du classeur restent la propriété du Bureau fédéral du Plan, cité comme source.
- Polices Inter et Source Serif 4 : SIL Open Font License 1.1.

Ce site est indépendant. Il n'émane ni du Bureau fédéral du Plan ni d'aucune institution ou parti.
