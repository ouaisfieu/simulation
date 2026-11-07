# -*- coding: utf-8 -*-
"""Couche éditoriale : une entrée par mesure du classeur BFP.

Champs
  fam   code de famille (voir familles.py)
  t     titre court en français
  tf    traduction française de l'intitulé original (mesures en néerlandais ou en anglais)
  typ   R recette | D économie de dépense | C coût | T transfert entre niveaux de pouvoir
        P processus ou long terme (pas d'effet direct) | F opération financière
        N neutre par construction | X hors compétence belge ou juridiquement impossible
  est   (bas, central, haut) : rendement structurel annuel en millions d'euros, niveau 2029,
        positif = améliore le solde, négatif = coûte
  ph    (part 2027, part 2028) du rendement structurel effectivement perçue (montée en charge)
  gr    niveau de confiance : A montant BFP (DC2024) repris tel quel ; B estimation officielle ou
        montant BFP ajusté ; C calcul assiette × taux sur données publiques ; D ordre de grandeur
        par analogie ; E spéculatif ; — sans objet (aucun effet chiffrable)
  mc    classe de multiplicateur macroéconomique ; inc profil d'incidence (qui paie)
  comp  compétence : F fédéral, R entités fédérées, M mixte, UE, BCE
  veh   véhicule : L loi, LS loi spéciale, AR arrêté royal, AC accord de coopération,
        ADM gestion administrative, UE négociation européenne, REF réforme de l'État, - aucun
  dl    délai de mise en œuvre : 0 moins de 6 mois, 1 environ un an, 2 environ deux ans, 3 plus
  res   résumé en français ; note : méthode du chiffrage et réserves ; src : clés de sources
"""

MESURES = {}

FAM_DEFAUTS = {
    "F01": ("capital", "CAP"), "F02": ("capital", "PAT"), "F03": ("capital", "PV"), "F04": ("capital", "LOY"),
    "F04b": ("capital", "LOY"), "F05": ("ipp", "AVA"), "F05b": ("ipp", "AVA"), "F05c": ("ipp", "CHQ"),
    "F05d": ("ipp", "AVA"), "F06": ("ipp", "FLX"), "F07": ("ipp", "NICH"), "F07b": ("ipp", "NICH"),
    "F08": ("ipp", "IPPL"), "F09a": ("ipp", "TRAV"), "F09b": ("transf_bas", "CRED"), "F09c": ("ipp", "ENF"),
    "F09d": ("ipp", "IPPH"), "F10": ("conso", "TVA"), "F10b": ("conso", "TVA"), "F11": ("accises", "ACC"),
    "F11b": ("accises", "ACC"), "F11c": ("accises", "ACC"), "F11d": ("accises", "ACC"),
    "F12a": ("entreprises", "ENT"), "F12b": ("entreprises", "IPPH"), "F12e": ("entreprises", "ENT"),
    "F12f": ("entreprises", "IPPH"), "F13a": ("entreprises", "ENT"), "F13b": ("entreprises", "ENT"),
    "F13c": ("entreprises", "ENT"), "F13d": ("capital", "CAP"), "F13e": ("ipp", "IND"),
    "F14": ("sante", "SAN"), "F14i": ("sante", "SAN"), "F15": ("transf_bas", "INC"), "F15b": ("entreprises", "ENT"),
    "F16": ("transf", "PEH"), "F16b": ("exterieur", "EXT"), "F17": ("transf_bas", "ALB"), "F17b": ("transf_bas", "ALB"),
    "F18": ("index", "IDX"), "F18b": ("index", "IDX"), "F19": ("consopub", "FP"), "F19c": ("exterieur", "EXT"),
    "F19d": ("exterieur", "EXT"), "F19e": ("consopub", "SP"), "F20": ("entreprises", "ENT"),
    "F21a": ("regions", "REG"), "F21b": ("regions", "REG"), "F22": ("nul", "NEU"), "F23": ("nul", "NEU"),
    "F23b": ("consopub", "NEU"), "F24": ("fraude", "FRA"), "F25": ("nul", "NEU"), "F26": ("nul", "NEU"),
    "F27": ("entreprises", "ENT"), "F28": ("nul", "NEU"),
}


def M(id, fam, t, typ, est=(0, 0, 0), ph=(1.0, 1.0), gr="—", mc=None, inc=None, comp="F", veh="L", dl=1,
      tf=None, res="", note="", src=()):
    assert id not in MESURES, f"doublon {id}"
    d_mc, d_inc = FAM_DEFAUTS[fam]
    b, c, h = est
    assert b <= c <= h or (b >= c >= h), f"fourchette incohérente {id}"
    if typ in ("P", "N", "X") and gr == "—":
        assert est == (0, 0, 0) or typ == "N", f"processus avec montant {id}"
    MESURES[id] = dict(id=id, fam=fam, t=t, tf=tf, typ=typ, est=dict(bas=b, central=c, haut=h),
                       ph=list(ph), gr=gr, mc=mc or d_mc, inc=inc or d_inc, comp=comp, veh=veh, dl=dl,
                       res=res, note=note, src=list(src))
