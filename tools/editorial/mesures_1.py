# -*- coding: utf-8 -*-
from base import M

DC = ("bfp-classeur", "dc2024")
PV = "Chiffré en 2024, avant la contribution de solidarité de 10 % sur les plus-values financières en vigueur depuis le 1er janvier 2026 (environ 500 M€ par an en régime). Gain additionnel revu à la baisse. Montée en charge lente : seules les plus-values constituées depuis 2026 sont imposables."
GLOB = "Montant DC2024 repris tel quel. Les revenus de 2027 sont enrôlés en 2028 et le rapportage bancaire doit être mis en place : rien en 2027, 60 % en 2028."

M(1, "F05", "Supprimer les niches IPP : voitures, chèques-repas, éco-chèques", "R", (3500, 4459, 5000), (0.25, 0.55), "A",
  res="Supprimer progressivement l'avantage fiscal des voitures de société, des chèques-repas et des éco-chèques (DéFI).",
  note="Montant DC2024 (impulsion 2029). Suppression progressive : 25 % du rendement en 2027, 55 % en 2028. Volet fiscal seulement : les cotisations sociales restent à part (famille F05b).", src=DC)
M(2, "F01", "Globaliser revenus financiers et loyers réels (DéFI)", "R", (4500, 6369, 7500), (0.0, 0.6), "A", dl=2,
  res="Soumettre les revenus financiers au barème progressif de l'IPP et imposer les loyers réels, après déduction des charges du propriétaire (DéFI).",
  note=GLOB + " Inclut les loyers réels : la famille F04 devient sans objet.", src=DC)
M(3, "F01", "Globaliser travail et capital (Ecolo)", "R", (4500, 6369, 7500), (0.0, 0.6), "A", dl=2,
  res="Imposer intérêts et dividendes au même barème progressif que les revenus du travail, et taxer les loyers réels nets (Ecolo).",
  note=GLOB + " Variante retenue pour le paquet médian. Inclut les loyers réels.", src=DC)
M(4, "F02", "Contribution sur les patrimoines nets > 1 M€ (Ecolo)", "R", (2000, 3658, 4500), (0.0, 0.5), "A", dl=2,
  res="Impôt annuel de 0,5 % à 2 % sur les patrimoines nets de plus d'un million d'euros, hors logement principal, biens professionnels et terres agricoles (Ecolo).",
  note="Montant DC2024. Suppose un cadastre des patrimoines qui n'existe pas : aucune recette en 2027, la moitié en 2028. L'évitement est appliqué à part (paramètre d'érosion du simulateur). Variante du paquet médian.", src=DC)
M(5, "F05", "Supprimer l'avantage voiture-salaire et carte carburant (Ecolo)", "R", (4000, 5213, 5500), (0.25, 0.55), "A",
  res="Supprimer progressivement l'avantage en nature de la voiture de société et de la carte carburant, ainsi que la déductibilité de la TVA et des frais de carburant. Les avantages des voitures électriques sont maintenus (Ecolo).",
  note="Montant DC2024. Contredit la proposition BFP-141, qui supprime les régimes favorables aux voitures électriques.", src=DC)
M(6, "F02", "Impôt des millionnaires remplaçant la taxe sur les comptes-titres (Groen)", "R", (800, 1500, 2013), (0.0, 0.5), "B", dl=2,
  tf="Un impôt des millionnaires sur les grands patrimoines",
  res="Transformer la taxe annuelle sur les comptes-titres en impôt progressif sur tout le patrimoine net : 0 % jusqu'à 2,5 M€, puis 0,4 %, 0,8 % et 1,2 % au-delà de 10 M€ (Groen).",
  note="Le BFP reprend 2 013 M€ (DC2024). Depuis, la taxe sur les comptes-titres que cet impôt remplacerait a été doublée (0,15 % → 0,30 %, accord budgétaire de novembre 2025) : gain additionnel revu à environ 1,5 Md€.", src=DC + ("lavenir-accord-2025",))
M(7, "F01", "Contribution sur les gains du patrimoine (Groen)", "R", (8000, 11265, 12000), (0.0, 0.6), "A", dl=2,
  tf="Une contribution plus juste sur les plus-values et revenus du patrimoine",
  res="Globaliser dividendes et intérêts, remplacer l'imposition cadastrale des loyers par les loyers réels nets, taxer les plus-values à 30 % et les rachats d'actions propres à 25 % (Groen).",
  note="Montant DC2024, le plus élevé du catalogue hors privatisations. Variante composite : elle rend sans objet les familles plus-values (F03) et loyers (F04).", src=DC)
M(8, "F12a", "Resserrer les RDT et supprimer la taxe carat (Groen)", "R", (600, 1050, 1300), (0.8, 1.0), "A",
  tf="Moins de régimes dérogatoires à l'impôt des sociétés",
  res="Durcir la condition de participation pour la déduction des revenus définitivement taxés, supprimer le régime favorable des sicav RDT et le régime de la taxe carat du secteur diamantaire (Groen).",
  note="Montant DC2024 ; le BFP l'arrondit à 1 Md€.", src=DC)
M(9, "F05", "Aligner toute la rémunération alternative sur le salaire (Groen)", "R", (4000, 5452, 6500), (0.25, 0.5), "A",
  tf="Adapter le traitement fiscal et parafiscal des composantes de la rémunération alternative",
  res="Aligner pas à pas le traitement fiscal et parafiscal de toutes les formes de rémunération alternative sur celui du salaire ordinaire (Groen).",
  note="Montant DC2024, volets fiscal et parafiscal compris. Variante du paquet médian. Alignement progressif : montée en charge lente.", src=DC)
M(10, "F13c", "Borner la réduction premier engagement (Groen)", "N", (0, 0, 495), (1.0, 1.0), "B",
  tf="Limiter dans le temps et rendre dégressive la subvention à l'embauche du premier travailleur",
  res="Limiter la réduction de cotisations pour le premier travailleur aux 26 premiers trimestres et la rendre dégressive ; l'économie est réaffectée à des baisses de cotisations sur les bas salaires (Groen).",
  note="Le BFP retient l'impulsion brute de 495 M€. Mais le texte prévoit de réaffecter intégralement l'économie : l'effet net sur le solde est nul. Exemple d'un montant officiel qui ne mesure pas la mesure telle qu'elle est écrite.", src=DC)
M(11, "F03", "Taxer les plus-values à 30 % (Les Engagés)", "R", (900, 1800, 2889), (0.3, 0.6), "B",
  res="Taxer les plus-values nettes à un taux de 30 % qui favorise l'actionnariat de long terme plutôt que la spéculation (Les Engagés).",
  note="DC2024 : 2 889 M€. " + PV + " Variante du paquet médian.", src=DC + ("pm-plusvalues",))
M(12, "F01", "Globaliser les revenus mobiliers (PS)", "R", (4000, 5649, 6500), (0.0, 0.6), "A", dl=2,
  res="Soumettre au barème progressif de l'IPP les revenus aujourd'hui frappés du précompte mobilier libératoire de 30 % (PS).",
  note=GLOB + " Variante la moins rémunératrice de la famille.", src=DC)
M(13, "F02", "Taxer le patrimoine à partir de 1,25 M€ (PS)", "R", (4000, 7558, 8500), (0.0, 0.5), "A", dl=2,
  res="Impôt progressif sur les patrimoines à partir de 1,25 M€, hors habitation et biens professionnels : 0,4 % à 1,5 % selon la tranche (PS).",
  note="Montant DC2024, le plus élevé de la famille : variante du paquet maximal. Suppose un cadastre des patrimoines.", src=DC)
M(14, "F03", "Taxer les plus-values à 30 % (PS)", "R", (900, 1800, 2889), (0.3, 0.6), "B",
  res="Assujettir les plus-values à un impôt de 30 % en modifiant le Code des impôts sur les revenus (PS).",
  note="DC2024 : 2 889 M€. " + PV, src=DC + ("pm-plusvalues",))
M(15, "F02", "Taxe des millionnaires, 2 % et 3 % (PVDA-PTB)", "R", (2000, 3907, 4500), (0.0, 0.5), "A", dl=2,
  tf="Taxe des millionnaires",
  res="Impôt de 2 % sur les fortunes au-delà de 5 M€ et de 3 % au-delà de 10 M€ (PVDA-PTB).",
  note="Montant DC2024. Taux élevés sur une base étroite : forte sensibilité à l'évitement et à l'expatriation.", src=DC)
M(16, "F03", "Plus-values financières à 30 % et à l'Isoc (PVDA-PTB)", "R", (1200, 2600, 3772), (0.3, 0.6), "B",
  tf="Imposition des plus-values financières",
  res="Taxer à 30 % les plus-values financières à l'IPP et supprimer leur exonération à l'impôt des sociétés (PVDA-PTB).",
  note="DC2024 : 3 772 M€. " + PV + " Variante la plus large de la famille (elle touche aussi les sociétés) : paquet maximal.", src=DC + ("pm-plusvalues",))
M(17, "F12e", "Taxe sur les surprofits bancaires (PVDA-PTB)", "R", (300, 640, 900), (1.0, 1.0), "A",
  tf="Taxe sur les surprofits bancaires",
  res="Taxer à 50 % la part des bénéfices bancaires qui dépasse un rendement de 5 % des fonds propres (PVDA-PTB).",
  note="Montant DC2024. Rendement très dépendant des marges d'intérêt.", src=DC)
M(18, "F01", "Globaliser les revenus financiers (Vooruit)", "R", (6000, 9695, 10500), (0.0, 0.6), "A", dl=2,
  tf="Globalisation à l'IPP : revenus du patrimoine financier",
  res="Intégrer tous les revenus du patrimoine financier dans la base de l'IPP, hors fonds et assurances pension ; le précompte mobilier cesse d'être libératoire (Vooruit).",
  note=GLOB + " Variante du paquet maximal : elle ne couvre ni les plus-values ni les loyers, chiffrés à part par le même parti (BFP-020, BFP-021).", src=DC)
M(19, "F04", "Taxer les loyers réels (Vooruit)", "R", (300, 676, 900), (0.0, 0.6), "A", dl=2,
  tf="Globalisation à l'IPP : loyers réels",
  res="Imposer à l'IPP les loyers réels nets, après déduction des frais réels, avec une déduction temporaire majorée pour les rénovations énergétiques (Vooruit).",
  note="Montant DC2024. Déclaratif : enrôlement l'année suivante. Variante du paquet médian.", src=DC)
M(20, "F03", "Plus-values sur actions au barème de l'IPP (Vooruit)", "R", (900, 1800, 2889), (0.3, 0.6), "B",
  tf="Globalisation à l'IPP : plus-values sur actions",
  res="Intégrer dans la base de l'IPP les plus-values sur actifs financiers détenus directement ou indirectement, pour les seules plus-values constituées après la réforme (Vooruit).",
  note="DC2024 : 2 889 M€. " + PV, src=DC + ("pm-plusvalues",))
M(21, "F15", "Réintégrer les malades de longue durée (CD&V)", "D", (100, 300, 574), (0.4, 0.7), "B",
  tf="Renforcer la réintégration des malades de longue durée",
  res="Davantage de trajets de réintégration avec les services régionaux de l'emploi, plus de coordinateurs « retour au travail », cumul possible d'une allocation et d'un revenu (CD&V).",
  note="DC2024 : 574 M€. L'accord budgétaire de novembre 2025 attend déjà environ 1,9 Md€ de la remise au travail des malades de longue durée d'ici 2029 : gain additionnel estimé à 300 M€.", src=DC + ("cdc-budget-2026",))
M(22, "F09c", "Supprimer l'exonération pour enfants à charge (Les Engagés)", "R", (0, 700, 1983), (0.8, 0.9), "B", comp="M",
  res="Supprimer l'exonération fiscale pour enfants à charge une fois les allocations familiales portées à 300 €, pour les enfants nés après 2020 (Les Engagés).",
  note="Le BFP retient 1 983 M€, gain fédéral. La condition préalable (allocations à 300 €, compétence des Communautés) coûterait de l'ordre de 1,3 Md€ : effet net pour l'ensemble des pouvoirs publics estimé à 0,7 Md€. Variante du paquet médian.", src=DC)
M(23, "F16", "Geler l'indexation des pensions au-delà de 3 500 € (N-VA)", "D", (300, 600, 841), (0.6, 0.9), "B",
  tf="Prévoir une contribution des pensions les plus élevées",
  res="Ne pas indexer les pensions supérieures à 3 500 € pendant trois ans et supprimer entièrement la péréquation des pensions du secteur public (N-VA).",
  note="DC2024 : 841 M€, pour une période qui commençait en 2025. Transposé à 2027-2029 et compte tenu de la réforme des pensions votée le 29 mai 2026, gain additionnel estimé à 600 M€.", src=DC)
M(24, "F17", "Geler le revenu d'intégration (N-VA)", "D", (300, 507, 600), (0.35, 0.65), "A",
  tf="Réformer le revenu d'intégration pour creuser l'écart entre travailler et ne pas travailler",
  res="Ne pas indexer ni revaloriser le revenu d'intégration pendant la législature, et en conditionner une partie à la connaissance de la langue, au parcours d'intégration ou à l'inscription comme demandeur d'emploi (N-VA).",
  note="Montant DC2024. L'économie croît avec l'inflation cumulée. Le BFP range la mesure parmi les réformes de long terme.", src=DC)
M(25, "F05b", "Cotiser sur toute rémunération alternative (PS)", "R", (1500, 2055, 2300), (0.7, 1.0), "A",
  res="Cotisation patronale de 25 % sur les avantages aujourd'hui exonérés : usage privé de la voiture de société, interventions domicile-travail, prime bénéficiaire, chèques sport et culture, options sur actions (PS).",
  note="Montant DC2024. Perception rapide par l'ONSS. Sans objet si la variante retenue en F05 couvre déjà le volet parafiscal.", src=DC)
M(26, "F16", "Abaisser le plafond de pension (VB)", "D", (300, 600, 788), (0.5, 0.8), "B",
  tf="Des pensions équitables par l'abaissement de la pension maximale",
  res="Ramener la pension légale maximale de 7 969 € à 4 780 € bruts par mois (montants 2024), toutes les pensions restant indexées (VB).",
  note="DC2024 : 788 M€. Une application aux pensions en cours heurterait les droits acquis et le principe de confiance légitime : seule une application progressive est retenue (600 M€).", src=DC)
M(27, "F14", "Maintenir la norme santé à 2,5 % (Groen)", "D", (600, 1244, 1500), (0.33, 0.67), "A",
  tf="Maintien de la norme de croissance légale de 2,5 % du budget de l'assurance maladie (INAMI)",
  res="Revenir à la procédure budgétaire légale de l'INAMI, avec une norme de croissance de 2,5 % au-delà de l'inflation (Groen).",
  note="Montant DC2024, mesuré par rapport à une trajectoire tendancielle plus dépensière. Contredit les variantes qui abaissent la norme : exclue du paquet cohérent.", src=DC)
M(28, "F14", "Aligner la santé sur la croissance (N-VA)", "D", (2500, 4537, 5000), (0.33, 0.67), "A",
  tf="Aligner davantage les dépenses de soins de santé sur la croissance économique",
  res="Ramener la norme de croissance des soins de santé vers la croissance de l'économie d'ici la fin de la législature (N-VA).",
  note="Montant DC2024, le plus élevé de la famille : variante du paquet maximal. Fourchette du BFP : 3,3 à 4,5 Md€. Les économies s'accumulent d'année en année (un tiers en 2027, deux tiers en 2028).", src=DC)
M(29, "F14", "Norme santé ramenée à 1,5 % (Open VLD)", "D", (2000, 3253, 4000), (0.33, 0.67), "A",
  tf="Rendre les soins de santé soutenables à long terme en ramenant la norme de croissance à 1,5 % au-delà de l'index",
  res="Abaisser la norme de croissance des soins de santé à 1,5 % au-delà de l'index (Open VLD).",
  note="Montant DC2024. Variante du paquet médian.", src=DC)
M(30, "F15", "Responsabiliser sur l'incapacité de travail (N-VA)", "D", (150, 400, 796), (0.4, 0.7), "B",
  tf="Éviter l'incapacité de travail de longue durée et favoriser la réintégration des malades et invalides",
  res="Contribution des grandes entreprises proportionnelle au coût de l'incapacité, réductions d'indemnités en cas de manquements administratifs, financement de la réintégration selon les résultats (N-VA).",
  note="DC2024 : 796 M€. Recouvre en partie le plan de retour au travail déjà compté dans l'accord de novembre 2025 : gain additionnel estimé à 400 M€.", src=DC + ("cdc-budget-2026",))
M(31, "F19c", "Modèle danois pour l'asile (VB)", "D", (0, 200, 716), (0.6, 0.9), "B",
  tf="Limiter les coûts migratoires en réduisant les arrivées et en augmentant les départs du dispositif d'asile",
  res="Douze mesures inspirées du modèle danois pour viser au plus 40 demandeurs d'asile pour 100 000 habitants : procédure raccourcie, suppression du revenu d'intégration et de l'argent de poche, accueil uniquement collectif, aide juridique réduite (VB).",
  note="DC2024 : 716 M€. Selon le BFP, la limitation de l'asile a déjà été adoptée dans l'accord de gouvernement : gain additionnel faible (200 M€). Plusieurs volets se heurtent au droit européen et international.", src=DC)
M(32, "F23", "Vendre les participations publiques en 2029 (VB)", "F", (0, 0, 0), (0.0, 0.0), "—",
  tf="Investir stratégiquement grâce à la vente des participations publiques non stratégiques",
  res="Vendre en 2029 les participations non stratégiques de l'État dans Proximus, Belfius, bpost, Ageas, BNP Paribas et Ethias (VB).",
  note="Les 15 Md€ sont un produit de vente, pas une impulsion budgétaire : ils réduisent la dette, pas le déficit au sens du SEC 2010. L'État perd en outre des dividendes, qui peuvent dépasser les intérêts économisés. Le texte situe la vente en 2029, après la fenêtre de deux ans.", src=DC)
M(33, "F20", "Tailler dans les subsides fédéraux, SNCB comprise (N-VA)", "D", (800, 1291, 1500), (0.6, 0.85), "A", inc="SP",
  tf="Réduire les subsides fédéraux et abandonner des missions",
  res="Réduire subsides et missions fédérales, geler la dotation d'exploitation de la SNCB et d'Infrabel au niveau de 2024 avec une baisse annuelle supplémentaire, réduire la contribution à l'Agence spatiale européenne et la subvention à bpost, supprimer l'aide à la presse et le soutien au réseau d'hydrogène (N-VA).",
  note="Montant DC2024.", src=DC)
M(34, "F19d", "Supprimer la coopération au développement fédérale (N-VA)", "D", (500, 900, 1432), (0.7, 1.0), "B",
  tf="Inscrire la coopération au développement dans un agenda économique et de sécurité plus large",
  res="Supprimer entièrement l'aide publique au développement fédérale, hors traités multilatéraux ; la direction générale de la coopération disparaît et les Régions mènent leur propre politique (N-VA).",
  note="DC2024 : 1 432 M€. L'Arizona a déjà réduit cette aide : le BFP la dit partiellement adoptée. Gain additionnel estimé à 0,9 Md€.", src=DC + ("bfp-rapport",))
M(35, "F19c", "Ramener l'accueil à 12 000 places (N-VA)", "D", (0, 200, 548), (0.6, 0.9), "B",
  tf="Limiter les arrivées en matière de migration",
  res="Ramener la capacité d'accueil à 12 000 places, ne garder que l'accueil collectif, préférer la contribution financière européenne à l'accueil, renvoyer au moins la moitié des détenus en séjour irrégulier (N-VA).",
  note="DC2024 : 548 M€. Déjà largement adopté selon le BFP : gain additionnel faible. Variante du paquet médian.", src=DC + ("bfp-rapport",))
M(36, "F20", "Rationaliser les subsides aux entreprises (Vooruit)", "R", (500, 936, 1100), (0.6, 0.85), "A",
  tf="Économies sur les subsides aux entreprises",
  res="Limiter à 24 mois les plans d'embauche « plus », supprimer progressivement en 2027-2028 la dispense de précompte des sportifs, réduire de 5,3 % les autres dispenses de versement du précompte professionnel (Vooruit).",
  note="Montant DC2024.", src=DC)
M(37, "F23", "Vendre les participations, moitié réinvestie (N-VA)", "F", (0, 0, 0), (0.0, 0.0), "—",
  tf="Vendre les participations publiques non stratégiques : produit réparti entre désendettement et investissements",
  res="Vendre les participations non stratégiques (Proximus, Belfius, bpost, Ageas, BNP Paribas) et la Loterie nationale ; la moitié du produit réduit la dette, l'autre finance des investissements en défense et en énergie (N-VA).",
  note="10 Md€ de produit. La moitié réinvestie accroît le déficit : l'opération dégrade le solde.", src=DC)
M(38, "F11", "Sortir des subsides fossiles au transport (Groen)", "R", (800, 1256, 1500), (0.5, 0.75), "A", comp="M",
  tf="Démanteler les subsides fossiles du transport et fluidifier la mobilité par une fiscalité routière incitative",
  res="Ramener à zéro le remboursement du diesel professionnel, accise sur le GPL, le GNC et le GNL, réforme de la taxe de mise en circulation et taxe kilométrique intelligente dans les trois Régions (Groen).",
  note="Montant DC2024. La taxe kilométrique et la taxe de mise en circulation sont régionales. Variante du paquet médian.", src=DC)
M(39, "F11", "Supprimer le remboursement du diesel professionnel (Vooruit)", "R", (500, 825, 900), (0.4, 0.6), "A",
  tf="Supprimer la subvention au diesel professionnel",
  res="Supprimer linéairement en cinq ans le remboursement du diesel professionnel (Vooruit).",
  note="Montant DC2024.", src=DC)
M(40, "F28", "Financer les soins de santé par tous les revenus", "N",
  res="Une cotisation proportionnelle sur l'ensemble des revenus finance la totalité des dépenses de santé ; son taux découle du budget voulu.",
  note="Réforme du mode de financement, sans recette nette en soi : neutre par construction.")
M(41, "F05", "Supprimer tous les régimes favorables de rémunération alternative (volet fiscal)", "R", (3500, 4500, 5500), (0.25, 0.55), "D",
  res="Soumettre toutes les rémunérations au même régime fiscal : fin des avantages des voitures de société, chèques, plans cafétéria, primes et autres formes de rémunération alternative.",
  note="Variante la plus large de la famille : paquet maximal. Ordres de grandeur : coût fiscal et parafiscal des voitures de société de 4,7 à 5,2 Md€ (BFP, WP 04-25), chèques-repas et éco-chèques environ 1,5 Md€, autres avantages environ 1 Md€. Volet fiscal estimé à 4,5 Md€ après conversion partielle en salaire.", src=("bfp-wp-voitures",))
M(42, "F05b", "Supprimer tous les régimes favorables (volet parafiscal)", "R", (1500, 2000, 2800), (0.6, 0.9), "D",
  res="Soumettre aux cotisations sociales toutes les formes de rémunération alternative.",
  note="Alternative à la mesure PS chiffrée par le BFP (BFP-026, 2 055 M€).", src=("bfp-wp-voitures",))
M(43, "F07", "Supprimer l'épargne-pension et l'exonération des intérêts", "R", (500, 900, 1300), (0.3, 0.9), "C",
  res="Supprimer des niches de l'IPP à l'efficacité douteuse, comme l'épargne-pension et l'exonération du précompte mobilier sur les intérêts.",
  note="Ordre de grandeur des deux avantages. L'exonération des intérêts se perçoit à la source ; la réduction d'impôt pour épargne-pension, à l'enrôlement.")
M(44, "F13a", "Plafonner à nouveau les cotisations sociales", "C", (-800, -400, -150), (1.0, 1.0), "D",
  res="Réintroduire un plafond aux cotisations sociales pour en renforcer la légitimité et rendre le financement transparent.",
  note="Mesure coûteuse. Contredit trois propositions qui suppriment tout plafond (BFP-207, BFP-240, BFP-248) : exclue du paquet cohérent.")
M(45, "F09a", "Réduire les pièges à la promotion (volet fiscal)", "C", (-1500, -700, -300), (0.5, 1.0), "D",
  res="Atténuer le saut du taux marginal de 25 % à 40 % et la dégressivité du bonus à l'emploi.",
  note="Allègement du travail non compensé dans le texte : coût.")
M(46, "F09a", "Réduire les pièges à la promotion (volet parafiscal)", "C", (-1000, -500, -200), (0.5, 1.0), "D",
  res="Atténuer la progressivité des cotisations liée à la dégressivité du bonus à l'emploi.",
  note="Volet parafiscal de la mesure précédente : coût.")
M(47, "F17b", "Tenir compte de tous les revenus pour l'accès aux aides", "D", (100, 300, 600), (0.2, 0.6), "D",
  res="Étendre le revenu pris en compte pour l'accès aux dispositifs sociaux à tous les revenus du travail, mobiliers et immobiliers.",
  note="Recoupe la réforme du statut BIM (BFP-151). Exige des échanges de données qui n'existent pas encore pour les revenus mobiliers.")
M(48, "F09b", "Bonus à l'emploi remplacé par un crédit d'impôt (volet fiscal)", "C", (-800, -300, 0), (0.0, 0.5), "E", dl=2,
  res="Remplacer le bonus à l'emploi fiscal par un crédit d'impôt intégralement et immédiatement remboursable.",
  note="Réforme de structure ; le remboursement immédiat élargit le public bénéficiaire : coût probable.")
M(49, "F09b", "Bonus à l'emploi remplacé par un crédit d'impôt (volet parafiscal)", "N", (-300, 0, 300), (0.0, 0.5), "E", dl=2,
  res="Remplacer le bonus à l'emploi social par le même crédit d'impôt remboursable.",
  note="Transfert d'un instrument parafiscal vers l'IPP : effet net proche de zéro.")
M(50, "F09b", "Charges de famille par crédits d'impôt remboursables", "C", (-1500, -500, 0), (0.0, 0.5), "E", dl=2,
  res="Unifier la prise en compte des personnes à charge dans un crédit d'impôt unique, intégralement et immédiatement remboursable.",
  note="Le caractère remboursable profite aux ménages non imposables : coût probable.")
M(51, "F09b", "Remplacer la quotité exemptée par un crédit d'impôt remboursable", "C", (-4000, -2000, -800), (0.0, 0.5), "E", dl=2,
  res="Transformer la quotité exemptée d'impôt en crédit d'impôt immédiatement et intégralement remboursable.",
  note="Les contribuables non imposables recevraient la valeur de la quotité exemptée : coût de plusieurs milliards selon le calibrage. Très incertain.")
M(52, "F26", "Une seule rémunération mensuelle (fin des primes annuelles)", "P",
  res="Diviser la rémunération annuelle par douze : fin du double pécule et de la prime de fin d'année versés à part.",
  note="Transparence et simplification ; pas d'effet budgétaire direct.")
M(53, "F18", "Indexer tout deux fois par an, au même moment", "N", (-500, 0, 500), (0.5, 1.0), "E",
  res="Indexer salaires, allocations, subsides et barèmes fiscaux deux fois par an, simultanément.",
  note="Effet budgétaire ambigu, selon le calendrier retenu. Contredit l'indexation annuelle (BFP-093) et la suppression de l'indexation automatique des salaires (BFP-071).")
M(54, "F19", "Unifier la perception des prélèvements", "P",
  res="Confier la perception de tous les prélèvements fiscaux et parafiscaux obligatoires à une seule administration.",
  note="Gains d'efficacité à long terme, non chiffrables à deux ans.")
M(55, "F08", "Reporter ou abandonner la baisse d'IPP programmée", "R", (3000, 3500, 4600), (0.143, 0.214), "B",
  tf="Court terme : reporter ou abandonner la baisse programmée de l'impôt des personnes physiques",
  res="Reporter ou abandonner la hausse de la quotité exemptée, mesure très coûteuse qui n'améliore guère les incitants au travail.",
  note="Coût évité selon le calendrier de la réforme : 0,5 Md€ en 2027, 0,75 Md€ en 2028, 3,5 Md€ en 2029 (estimation OECCBB). Fourchette haute : additionnels régionaux inclus.", src=("oeccbb-quotite",))
M(56, "F28", "Élargir davantage les bases imposables (volet IPP)", "N",
  tf="Court terme : élargir davantage les bases imposables fiscales et parafiscales (volet IPP)",
  res="Réduire autant que possible les régimes dérogatoires de l'IPP, dans un exercice budgétairement neutre qui permet de baisser les taux marginaux.",
  note="Neutre par construction, selon son auteur.")
M(57, "F28", "Élargir davantage les bases imposables (volet cotisations)", "N",
  tf="Court terme : élargir davantage les bases imposables fiscales et parafiscales (volet cotisations sociales)",
  res="Même exercice pour les cotisations sociales, en revenant notamment sur l'extension des flexi-jobs.",
  note="Neutre par construction, selon son auteur.")
M(58, "F28", "Élargir davantage les bases imposables (volet plus-values)", "N",
  tf="Court terme : élargir davantage les bases imposables fiscales et parafiscales (volet plus-values)",
  res="Même exercice pour la contribution sur les plus-values qui vient d'être instaurée.",
  note="Neutre par construction, selon son auteur.")
M(59, "F28", "Large réforme fiscale : glissement des prélèvements", "N",
  tf="Long terme : large réforme fiscale, volet glissement des prélèvements",
  res="Une réforme fiscale plutôt qu'une baisse d'impôt : glisser les prélèvements du travail vers les revenus du patrimoine, uniformiser l'imposition du capital, supprimer les exceptions, sortir des subsides fossiles, instaurer le péage kilométrique.",
  note="Long terme et neutre par construction ; recoupe l'abandon de la baisse d'IPP (F08).")
M(60, "F28", "Large réforme fiscale : suppression des régimes dérogatoires", "N",
  tf="Long terme : large réforme fiscale, volet suppression des régimes (para)fiscaux dérogatoires",
  res="Volet « suppression des exceptions » de la même réforme d'ensemble.", note="Long terme et neutre par construction.")
M(61, "F28", "Large réforme fiscale : sortie des subsides fossiles", "N",
  tf="Long terme : large réforme fiscale, volet transformation ou suppression des subsides fossiles",
  res="Volet « subsides fossiles » de la même réforme d'ensemble.", note="Long terme et neutre par construction.")
M(62, "F28", "Cotisation sociale généralisée pour la santé", "N",
  tf="Long terme : instaurer une cotisation sociale généralisée",
  res="Rendre visible le financement de chaque branche de la sécurité sociale et créer, pour les soins de santé, une cotisation générale sur les revenus du travail et du patrimoine.",
  note="Réforme du financement : neutre par construction.")
M(63, "F14i", "Exercices d'efficience en santé", "P",
  tf="Poursuivre durablement la maîtrise des dépenses de santé par des exercices d'efficience",
  res="Continuer à contenir les dépenses de santé par des exercices d'efficience.",
  note="Sans modalités : instrument de la norme de croissance (F14).")
M(64, "F21a", "Faire contribuer les Régions et Communautés", "D", (3000, 5000, 7000), (0.33, 0.67), "D", comp="R", veh="-",
  tf="Contribution des Régions aux économies",
  res="La Flandre dégage des excédents et réduit sa dette ; les autres entités atteignent l'équilibre budgétaire d'ici la fin de la législature.",
  note="Seule mesure qui demande un effort aux entités fédérées elles-mêmes. Ordre de grandeur : le déficit des Communautés, Régions et pouvoirs locaux représenterait 0,7 à 1 % du PIB vers 2029 (écart entre le solde de l'ensemble des administrations et celui de l'Entité I) ; l'effacer représente 5 à 7 Md€. Le pouvoir fédéral ne peut pas l'imposer.", src=("cm-juillet-2026", "bfp-juin-2026"))
M(65, "F10", "TVA à deux taux : 22 % et 12 %", "R", (4000, 6000, 8000), (0.9, 1.0), "D",
  tf="Simplifier et relever les impôts sur la consommation",
  res="Deux taux de TVA seulement : le taux normal passe par exemple de 21 % à 22 % et tous les autres taux à 12 %.",
  note="Ordre de grandeur : un point de taux normal rapporte de 1,5 à 2 Md€, et le passage de 6 % à 12 % rapporte nettement plus. Variante la plus lourde : paquet maximal. Avant effets induits : une grande partie revient par l'indexation (paramètre du simulateur).", src=("bfp-rapport",))
