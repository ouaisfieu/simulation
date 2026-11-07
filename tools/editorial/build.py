# -*- coding: utf-8 -*-
"""Assemble et valide la couche éditoriale → data/editorial.json et data/sources.json.
Usage : python3 tools/editorial/build.py   (depuis la racine du dépôt)"""
import json, os, sys, collections

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)
RACINE = os.path.abspath(os.path.join(ICI, "..", ".."))

from base import MESURES  # noqa: E402
import mesures_1, mesures_2, mesures_3, mesures_4  # noqa: E402,F401
from familles import FAMILLES, CONTRADICTIONS, TENSIONS  # noqa: E402
from sources import SOURCES  # noqa: E402

bfp = json.load(open(os.path.join(RACINE, "data", "mesures-bfp.json")))
ids_bfp = [m["id"] for m in bfp["mesures"]]
erreurs = []

# 1. couverture : exactement les 263 mesures
manque = sorted(set(ids_bfp) - set(MESURES))
trop = sorted(set(MESURES) - set(ids_bfp))
if manque: erreurs.append(f"mesures sans fiche éditoriale : {manque}")
if trop: erreurs.append(f"fiches sans mesure : {trop}")

# 2. familles
fam = {f["code"]: dict(f) for f in FAMILLES}
for f in fam.values():
    f["membres"] = sorted(i for i, m in MESURES.items() if m["fam"] == f["code"])
    f.setdefault("choix", {})
    f.setdefault("absorbe", {})
    f.setdefault("recouvrement", 1.0)
    f.setdefault("note", "")
for i, m in MESURES.items():
    if m["fam"] not in fam:
        erreurs.append(f"BFP-{i+1:03d} : famille inconnue {m['fam']}")
for f in fam.values():
    if not f["membres"]:
        erreurs.append(f"famille vide {f['code']}")
    for sc, v in f["choix"].items():
        for x in (v if isinstance(v, list) else [v]):
            if x not in f["membres"]:
                erreurs.append(f"{f['code']} choix {sc}={x} hors famille")
    for v, cibles in f["absorbe"].items():
        if v not in f["membres"]:
            erreurs.append(f"{f['code']} absorbe : variante {v} hors famille")
        for c in cibles:
            if c not in fam:
                erreurs.append(f"{f['code']} absorbe une famille inconnue {c}")

# 3. sources citées
cles = {s["cle"] for s in SOURCES}
for i, m in MESURES.items():
    for s in m["src"]:
        if s not in cles:
            erreurs.append(f"BFP-{i+1:03d} : source inconnue {s}")

# 4. cohérence BFP : les 39 mesures chiffrées sont gradées A ou B
for m in bfp["mesures"]:
    e = MESURES.get(m["id"])
    if e and m["montant2029"] is not None and e["gr"] not in ("A", "B", "—"):
        erreurs.append(f"BFP-{m['id']+1:03d} chiffrée par le BFP mais gradée {e['gr']}")
    if e and m["montant2029"] is None and e["gr"] in ("A",):
        erreurs.append(f"BFP-{m['id']+1:03d} gradée A sans montant BFP")

if erreurs:
    print("\n".join(erreurs))
    sys.exit(1)

# Clés JSON : identifiants en chaîne pour l'objet absorbe
for f in fam.values():
    f["absorbe"] = {str(k): v for k, v in f["absorbe"].items()}

sortie = dict(
    familles=list(fam.values()),
    contradictions=CONTRADICTIONS,
    tensions=TENSIONS,
    mesures=[MESURES[i] for i in sorted(MESURES)],
)
json.dump(sortie, open(os.path.join(RACINE, "data", "editorial.json"), "w"), ensure_ascii=False, indent=1)
json.dump(SOURCES, open(os.path.join(RACINE, "data", "sources.json"), "w"), ensure_ascii=False, indent=1)

typ = collections.Counter(m["typ"] for m in MESURES.values())
gr = collections.Counter(m["gr"] for m in MESURES.values())
print(f"{len(MESURES)} mesures, {len(fam)} familles, {len(SOURCES)} sources")
print("types :", dict(typ))
print("grades :", dict(gr))
