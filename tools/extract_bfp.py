#!/usr/bin/env python3
"""Transcription fidèle du classeur du Bureau fédéral du Plan
« DATA_BUDGET2027_13320.xlsx » (Options de politiques pour l'élaboration du budget 2027, 1er juin 2026)
vers data/mesures-bfp.json. Usage : python3 tools/extract_bfp.py chemin/vers/DATA_BUDGET2027_13320.xlsx
Requiert openpyxl. Les textes sont conservés tels quels (espaces normalisés seulement)."""
import json, re, sys, hashlib
import openpyxl

NL = {"de", "het", "een", "van", "en", "worden", "wordt", "voor", "met", "op", "naar", "bij", "niet", "zijn", "door", "tot", "ook", "dat", "die", "we"}
EN = {"the", "of", "and", "to", "is", "in", "for", "that", "on", "with", "which", "are", "by", "subsidy", "spending"}
FR = {"le", "la", "les", "des", "du", "une", "et", "pour", "sur", "dans", "par", "est", "sont", "à", "au", "aux", "qui"}

def norm(s):
    if s is None:
        return None
    s = str(s).replace("\xa0", " ").replace("_x0002_", "")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\s*\n\s*", "\n", s).strip()
    return s or None

def langue(*txts):
    words = re.findall(r"[a-zà-ÿ]+", " ".join(t for t in txts if t).lower())
    sc = {k: sum(w in v for w in words) for k, v in (("nl", NL), ("en", EN), ("fr", FR))}
    return max(sc, key=sc.get)

# Corrections manuelles de la détection automatique de langue (vérifiées à la lecture)
LANGUE_FORCEE = {15: "fr-nl", 16: "fr-nl", 17: "fr-nl", 73: "fr", 103: "fr", 104: "fr", 105: "fr",
                 112: "fr", 113: "fr", 120: "fr"}

def main(path):
    raw = open(path, "rb").read()
    wb = openpyxl.load_workbook(path, data_only=True)
    ws = wb.worksheets[0]
    rows = list(ws.iter_rows(values_only=True))
    out = []
    for i, r in enumerate(rows[1:], start=1):
        m = r[5]
        montant = None
        if m not in (None, ""):
            montant = int(round(float(str(m).replace(",", "."))))
        src = norm(r[6])
        url = None
        if src:
            u = re.search(r"https?://\S+", src)
            url = u.group(0).rstrip(".,;)") if u else None
        out.append({
            "id": i,
            "ref": f"BFP-{i+1:03d}",
            "ligne": i + 1,
            "categorie": norm(r[0]),
            "sousCategorie": norm(r[1]),
            "description": norm(r[2]),
            "modalites": norm(r[3]),
            "motivation": norm(r[4]),
            "montant2029": montant,
            "sourceChiffrage": src,
            "sourceUrl": url,
            "langue": LANGUE_FORCEE.get(i, langue(norm(r[2]), norm(r[3]), norm(r[4]))),
        })
    meta = {
        "fichier": "DATA_BUDGET2027_13320.xlsx",
        "sha256": hashlib.sha256(raw).hexdigest(),
        "publication": "Bureau fédéral du Plan, Options de politiques pour l'élaboration du budget 2027 (rapport 13320), 1er juin 2026",
        "urlRapport": "https://www.plan.be/sites/default/files/documents/REP_BUDGET2027_13320_FR.pdf",
        "urlClasseur": "https://www.plan.be/sites/default/files/documents/DATA_BUDGET2027_13320.xlsx",
        "feuille": ws.title,
        "enTetes": [norm(h) for h in rows[0]],
        "unite": "Impulsion budgétaire annuelle estimée en 2029, millions d'euros (colonne F), uniquement pour les mesures issues du chiffrage des programmes électoraux 2024 (DC2024)",
        "nombre": len(out),
    }
    return {"meta": meta, "mesures": out}

if __name__ == "__main__":
    data = main(sys.argv[1])
    json.dump(data, open("data/mesures-bfp.json", "w"), ensure_ascii=False, indent=1)
    c = {}
    for m in data["mesures"]:
        c[m["langue"]] = c.get(m["langue"], 0) + 1
    print(data["meta"]["nombre"], "mesures ;", sum(1 for m in data["mesures"] if m["montant2029"] is not None), "chiffrées ; langues", c)
