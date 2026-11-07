# -*- coding: utf-8 -*-
from base import M

Q = "Coût évité selon le calendrier de la réforme fiscale : 0,5 Md€ en 2027, 0,75 Md€ en 2028, 3,5 Md€ en 2029 (estimation OECCBB)."
LSF = "Transfert de charge du fédéral vers les entités fédérées ; majorité spéciale requise (le BFP juge une refonte de la LSF peu envisageable hors réforme de l'État)."

M(131, "F08", "Reporter la hausse de la quotité exemptée jusqu'à une nouvelle LSF", "R", (3000, 3500, 4600), (0.143, 0.214), "B",
  tf="Reporter la réforme de la quotité exemptée",
  res="Reporter la hausse de la quotité exemptée jusqu'à une nouvelle loi de financement : cela épargne aux Régions une perte implicite de 1,1 Md€ et les incite à réformer la LSF.",
  note=Q, src=("oeccbb-quotite",))
M(132, "F28", "LSF 1 : autonomie fiscale par taux séparés", "N", comp="M", veh="LS", dl=3,
  tf="Réforme de la loi de financement 1 : autonomie fiscale",
  res="Remplacer les additionnels régionaux par un système de taux séparés (split rate) qui découple la base régionale de l'impôt fédéral.",
  note="Transparence et autonomie ; neutre pour le solde.")
M(133, "F21b", "LSF 2 : supprimer la dotation régionale pour dépenses fiscales", "T", (300, 800, 1500), (0.2, 0.5), "D", comp="M", veh="LS", dl=3,
  tf="Réforme de la loi de financement 2 : réduire la dotation régionale pour dépenses fiscales",
  res="Supprimer progressivement la part de la dotation aux Régions qui finançait des dépenses fiscales transférées (titres-services et autres).",
  note=LSF)
M(134, "F21b", "LSF 3 : réduire de 3 Md€ la dotation IPP des Communautés", "T", (1500, 3000, 3000), (0.33, 0.67), "C", comp="M", veh="LS", dl=3,
  tf="Réforme de la loi de financement 3 : réduire la dotation IPP aux Communautés",
  res="Réduire de 3 Md€ la dotation IPP des Communautés et ramener de 55 % à 0 % sa liaison à la croissance réelle.",
  note=LSF + " Charge reportée sur l'enseignement, la culture, l'aide aux personnes. Fumée blanche retient aussi 3 Md€.", src=("conclave",))
M(135, "F21b", "LSF 4 : découpler la dotation TVA de la croissance", "T", (300, 600, 900), (0.33, 0.67), "C", comp="M", veh="LS", dl=3,
  tf="Réforme de la loi de financement 4 : découpler la dotation TVA aux Communautés de la croissance réelle",
  res="Ramener de 91 % à 0 % la liaison de la dotation TVA des Communautés à la croissance réelle.",
  note=LSF + " L'économie s'accumule avec la croissance.")
M(136, "F21b", "LSF 5 : découpler les autres dotations", "T", (100, 300, 500), (0.33, 0.67), "C", comp="M", veh="LS", dl=3,
  tf="Réforme de la loi de financement 5 : découpler les autres dotations aux Communautés de la croissance réelle",
  res="Même logique pour les autres dotations aux Communautés : liaison à la croissance réelle (25 % ou 65 %) ramenée à 0 %.",
  note=LSF)
M(137, "F23b", "Créer une banque belge d'investissement", "C", (-2000, -500, 0), (0.0, 0.3), "E", comp="M", dl=2,
  tf="Créer une banque belge d'investissement",
  res="Verser une partie des économies dans un fonds géré par une instance indépendante (BNB, nouvel organe…), qui financerait des projets de toutes les entités.",
  note="Réinjecte une partie des économies : coût. Le texte évoque 11,3 Md€ d'économies à l'horizon 2034.")
M(138, "F21b", "Relever la cotisation pension des entités fédérées", "T", (100, 300, 600), (0.5, 1.0), "D", comp="M", veh="LS",
  tf="Revoir la contribution de pension des Communautés, des Régions et des pouvoirs locaux",
  res="Étendre la contribution de responsabilisation pension des entités fédérées et des pouvoirs locaux, qui atteint son régime de croisière en 2028.",
  note="Transfert de charge.")
M(139, "F25", "Test d'efficience pour toute dépense", "P",
  tf="Instaurer un test d'efficience et d'effectivité (revue de dépenses)",
  res="Soumettre toute dépense, fiscale comprise, à un test préalable et récurrent d'efficience ; suppression automatique en cas d'inefficacité démontrée.",
  note="Procédure.")
M(140, "F05d", "Supprimer les avantages fiscaux des voitures électriques", "R", (300, 600, 1000), (0.6, 1.0), "D",
  res="Abolir les régimes fiscaux favorables aux voitures électriques, puisque le marché des voitures neuves bascule vers ce type de motorisation.",
  note="Contredit la variante Ecolo (BFP-006), qui maintient ces avantages. Sans objet si la variante retenue en F05 supprime déjà tous les avantages.")
M(141, "F12f", "Réduire les avantages des footballeurs professionnels", "R", (20, 40, 150), (0.8, 1.0), "D",
  res="Réduire les avantages fiscaux et parafiscaux des meilleurs footballeurs.",
  note="Recoupe la suppression de la dispense de précompte des sportifs (BFP-037) : gain résiduel.")
M(142, "F05c", "Supprimer le régime favorable des chèques-repas", "R", (600, 1200, 2000), (0.7, 1.0), "D",
  res="Supprimer le régime fiscal favorable des chèques-repas.",
  note="Ordre de grandeur : plus de deux millions de bénéficiaires ; une partie seulement serait convertie en salaire imposable.")
M(143, "F18", "Saut d'index généralisé avec cotisation de modération", "D", (2000, 3500, 5500), (1.0, 1.0), "D",
  res="Ne pas indexer, à concurrence de 2 %, salaires, traitements, allocations sociales et l'ensemble des revenus ; les entreprises versent une cotisation de modération salariale à due concurrence.",
  note="Ordre de grandeur : 2 % des prestations sociales et des salaires publics, plus la cotisation sur la masse salariale privée, moins les recettes perdues sur des salaires plus bas. Pèse sur tous les revenus. Fumée blanche retient 2,4 Md€.", src=("conclave",))
M(144, "F20", "Évaluer et limiter les subsides aux entreprises", "P",
  res="Évaluer le système d'aides aux entreprises pour éviter les effets d'aubaine et augmenter son efficacité.",
  note="Évaluation préalable : effet budgétaire différé.")
M(145, "F14", "Norme santé compatible avec la faible croissance", "D", (2000, 3500, 4537), (0.33, 0.67), "D",
  res="Revenir à une norme indicative de croissance qui tienne compte de la croissance des recettes et du vieillissement.",
  note="Proche de la variante N-VA (BFP-029).")
M(146, "F28", "Réformer fiscalité et subsides énergétiques", "N",
  res="Modifier les prix relatifs des énergies fossiles et décarbonées, tout en garantissant des prix compatibles avec le pouvoir d'achat et la sécurité d'approvisionnement.",
  note="Réforme d'équilibre : neutre par construction. L'auteur doute qu'on puisse alourdir les taxes fossiles quand le pétrole est cher.")
M(147, "F25", "Évaluer l'ensemble des dépenses fiscales", "P",
  res="Évaluer les dépenses fiscales que les conclaves citent toujours : voitures de société, avantages de toute nature, sociétés unipersonnelles, deuxième et troisième piliers…",
  note="Selon l'inventaire cité par l'auteur, les dépenses fiscales fédérales ont triplé entre 2004 et 2021.")
M(148, "F12a", "Revoir les conditions de la déduction RDT", "R", (300, 700, 1500), (0.8, 1.0), "D",
  res="Porter le seuil d'investissement de 2,5 à 4 M€, revoir l'accès des sicav RDT et réduire le taux de déduction (100 % aujourd'hui).",
  note="Déduction RDT à l'exercice 2024 : 21,9 Md€ ; plus-values RDT : 7,2 Md€ ; impôt des sociétés enrôlé : 23,6 Md€ (chiffres cités par l'auteur).")
M(149, "F08", "Suspendre ou conditionner la hausse de la quotité exemptée", "R", (3000, 3500, 4600), (0.143, 0.214), "B",
  res="Suspendre la hausse de la quotité exemptée ou la conditionner au retour à une situation budgétaire plus acceptable.",
  note=Q, src=("oeccbb-quotite",))
M(150, "F14i", "Réformer le statut BIM", "D", (300, 550, 800), (0.4, 0.9), "B", inc="ALB",
  res="Remplacer le seuil d'accès au statut BIM (25 630 € de revenus bruts imposables) par des interventions dégressives avec le revenu, pour gommer l'effet de seuil.",
  note="Les notes de travail du gouvernement (octobre 2026) chiffraient une réforme comparable à 550 M€. Instrument de la norme santé.", src=("rtbf-pistes-2026",))
M(151, "F26", "Cibler la hausse du budget de la défense", "P",
  res="Prioriser les dépenses de défense qui génèrent des effets retour importants sur l'activité belge, comme l'investissement.",
  note="Pas d'économie directe. Fumée blanche lui attribue 1,5 Md€ (« Réorienter l'effort de défense ») : cette lecture n'est pas reprise ici.", src=("conclave",))
M(152, "F04", "Simplifier l'imposition des loyers (loyers réels)", "R", (0, 400, 800), (0.0, 0.6), "D", dl=2,
  tf="Simplifier l'imposition des revenus locatifs à l'IPP, sur la base des loyers réels",
  res="Simplifier l'imposition des revenus locatifs à l'IPP, sur la base des loyers réels.",
  note="Simplification : rendement incertain.")
M(153, "F17b", "Élargir le revenu pris en compte pour les aides", "D", (100, 300, 600), (0.2, 0.6), "D",
  tf="Élargir la notion de revenu pour les allocations, avantages sociaux et bourses soumis à conditions de ressources",
  res="Intégrer revenus du capital et revenus perçus via une société dans le revenu qui conditionne allocations, avantages sociaux et bourses.",
  note="Suppose un cadastre des revenus mobiliers ; variante retenue de F17b.")
M(154, "F12b", "Décourager les sociétés de management", "R", (100, 300, 600), (0.8, 1.0), "D",
  tf="Sociétés de management",
  res="Durcir les conditions, par exemple celles du taux réduit de l'Isoc pour les petites sociétés, afin de décourager les sociétés de management.",
  note="Ordre de grandeur.")
M(155, "F25", "Politique fondée sur les preuves", "P",
  tf="Politique fondée sur les preuves (evidence-based policy)",
  res="Développer outils, accès aux données et écosystème public-académique pour optimiser systèmes fiscal et social.",
  note="Procédure.")
M(156, "F12b", "Taux d'Isoc lié à l'emploi", "R", (0, 500, 1200), (0.5, 1.0), "E",
  tf="Taux progressif de l'impôt des sociétés",
  res="Lier le taux de l'Isoc à l'emploi, pour que les sociétés sans personnel (sociétés de management, certains holdings) paient plus que les sociétés d'exploitation.",
  note="Ordre de grandeur très incertain.")
M(157, "F20", "Moduler la déduction pour investissement", "R", (50, 200, 500), (0.8, 1.0), "D",
  tf="Moduler la déduction pour investissement",
  res="Réduire ou supprimer la déduction pour investissement des sociétés sans personnel.",
  note="Ordre de grandeur.")
M(158, "F19", "Simplifier le contrôle fiscal", "P",
  tf="Simplifier le contrôle fiscal",
  res="Reprendre le modèle de l'expert-estimateur de l'impôt flamand sur les successions : le SPF Finances accepte les évaluations des experts-comptables liés par un protocole.",
  note="Efficacité administrative.")
M(159, "F19", "Élargir la conciliation fiscale", "P",
  tf="Élargir la conciliation fiscale",
  res="Permettre la conciliation fiscale avant que le conflit ne s'envenime, et non seulement après réclamation.",
  note="Moins de litiges.")
M(160, "F01", "Dividendes à 22,5 % pour tous, VVPR-bis compris", "C", (-1500, -800, -200), (0.8, 1.0), "D", dl=0,
  tf="Uniformiser le taux forfaitaire des revenus mobiliers",
  res="Taxer au même taux linéaire de 22,5 % les dividendes VVPR-bis (taux réduit) et les autres dividendes.",
  note="Baisser de 30 % à 22,5 % le taux des dividendes ordinaires coûte plus que ne rapporte la hausse du VVPR-bis (déjà porté à 18 %). Contredit l'uniformisation à 30 %.")
M(161, "F01", "Précompte non libératoire et barème progressif", "R", (3000, 5000, 7000), (0.0, 0.6), "D", dl=2,
  tf="Supprimer le caractère libératoire du précompte mobilier, avec un taux progressif sur les revenus du patrimoine",
  res="Déclarer les revenus mobiliers à l'IPP et les rendre visibles sur l'avertissement-extrait de rôle, pour la transparence et un meilleur ciblage des aides sociales.",
  note="Équivaut à une globalisation (F01) : même ordre de grandeur que la variante PS.")
M(162, "F01", "Barème progressif sur les revenus du patrimoine", "R", (3000, 5000, 7000), (0.0, 0.6), "D", dl=2,
  tf="Taux progressif sur les revenus du patrimoine, avec la suppression du précompte libératoire",
  res="Appliquer un barème progressif aux revenus du capital : qui reçoit 2 000 € de dividendes paie aujourd'hui le même taux que qui en reçoit 2 millions.",
  note="Équivaut à une globalisation (F01).")
M(163, "F09d", "Requalifier les revenus mobiliers et divers au-delà d'un plafond", "R", (50, 150, 400), (0.0, 0.8), "E",
  tf="Comparer le traitement des revenus mobiliers, immobiliers et divers",
  res="Comme pour les droits d'auteur (environ 70 000 €), requalifier en revenus professionnels les revenus mobiliers, immobiliers ou divers au-delà d'un plafond.",
  note="Assiette mal connue.")
M(164, "F05", "Réévaluer les forfaits d'avantages de toute nature", "R", (600, 1200, 2000), (0.7, 1.0), "C",
  tf="Réévaluer les avantages de toute nature fixés forfaitairement",
  res="Évaluer à leur valeur réelle les avantages de toute nature aujourd'hui fixés par forfait.",
  note="Variante partielle de F05.", src=("bfp-wp-voitures",))
M(165, "F14i", "Ticket modérateur selon le revenu", "D", (0, 200, 500), (0.5, 1.0), "D",
  tf="Rendre le ticket modérateur davantage dépendant du revenu",
  res="Moduler davantage le ticket modérateur selon les revenus du patient.",
  note="Instrument de la norme santé.")
M(166, "F08", "Réorienter la hausse de la quotité exemptée", "N", (0, 0, 0), (0.143, 0.214), "B",
  tf="Réorienter le relèvement de la quotité exemptée d'impôt",
  res="Geler ou affaiblir fortement la hausse de la quotité exemptée vers 15 300 € en 2029 et réorienter le budget vers des instruments ciblés : relever les seuils des taux de 45 % et 50 %, baisser les cotisations sur les bas salaires.",
  note="Réaffectation : neutre pour le solde. Contredit l'abandon pur et simple.", src=("oeccbb-quotite",))
M(167, "F28", "Déplacer la charge fiscale du travail vers la consommation", "N",
  tf="Déplacer la charge fiscale du travail vers la consommation",
  res="Baisser l'IPP sur le travail, financé par une hausse de la TVA et la simplification des taux réduits de 6 % et 12 %.",
  note="Glissement neutre par construction.")
M(168, "F06", "Restreindre les flexi-jobs aux secteurs en pénurie", "R", (50, 150, 300), (0.8, 1.0), "D",
  tf="Restreindre et réformer de manière ciblée le régime des flexi-jobs",
  res="Limiter les flexi-jobs aux secteurs en pénurie structurelle et interdire leur cumul avec une réduction d'horaire chez l'employeur principal.",
  note="Ordre de grandeur.")
M(169, "F20", "Évaluation critique des subsides aux entreprises", "P",
  tf="Évaluer de façon critique les subsides et aides à l'investissement aux entreprises",
  res="Analyser, pour chaque subside, s'il atteint efficacement son objectif ; plus de transparence est nécessaire.",
  note="Évaluation préalable.")
M(170, "F13c", "Réduire la réduction premier engagement", "R", (100, 300, 488), (0.6, 1.0), "C",
  tf="Réduire le biais des subsides en faveur des petites entreprises",
  res="Les aides perdues au-delà d'un seuil incitent à rester petit : la réduction pour le premier travailleur a coûté 488 M€ en 2023 sans création nette d'emplois durable.",
  note="Hypothèse : avantage réduit d'environ 60 %.")
M(171, "F11c", "Indexer les accises", "R", (100, 300, 500), (0.5, 1.0), "C",
  tf="Limiter l'impact de l'inflation importée sur le solde budgétaire (accises)",
  res="Les accises, fixées par unité et non en proportion du prix, baissent par rapport au PIB : les indexer.",
  note="Carburants, tabac et alcool sont exclus de l'indice santé : peu d'effet retour par l'indexation.")
M(172, "F18", "Freiner l'indexation automatique des dépenses", "D", (300, 800, 1500), (1.0, 1.0), "D",
  tf="Limiter l'impact de l'inflation importée sur le solde budgétaire (indexation automatique des dépenses)",
  res="Environ la moitié des dépenses primaires sont liées à l'indice santé, qui augmente plus vite que le déflateur du PIB quand l'inflation est importée : limiter cette indexation.",
  note="Ordre de grandeur.")
M(173, "F28", "Glissement vers les taxes environnementales", "N",
  tf="Un glissement général vers les taxes environnementales, et un glissement au sein des prélèvements liés aux gaz à effet de serre pour les rendre plus neutres",
  res="Taxer davantage l'environnement et uniformiser le prix du CO2 entre secteurs ; la voiture de société avec carte carburant externalise entièrement le coût de la pollution.",
  note="Glissement neutre par construction.")
M(174, "F25", "Évaluer les dépenses plus élevées que chez les voisins", "P",
  tf="Évaluer de façon critique les fonctions de dépense relativement élevées en Belgique par rapport aux pays voisins (COFOG)",
  res="Les dépenses publiques belges dépassaient de 4,5 points de PIB la moyenne des principaux pays voisins en 2019 : examiner les fonctions où l'écart est le plus grand.",
  note="Diagnostic.")
M(175, "F25", "Constat : recettes inférieures de 3 points à 2014", "P",
  tf="Les recettes se situaient en 2025 à 3 % du PIB sous leur niveau de 2014, alors historiquement élevé",
  res="Le tax shift de 2015 a été une baisse d'impôt plus qu'un glissement, faute de recettes compensatoires.",
  note="Constat, pas mesure.")
M(176, "F14i", "Constat : santé et incapacité croissent plus vite que le PIB", "P",
  tf="Les dépenses de soins de santé et d'incapacité augmentent plus vite que le PIB",
  res="Les dépenses de soins de santé et d'incapacité de travail ont fortement augmenté.", note="Constat, pas mesure.")
M(177, "F28", "Toute baisse sur le travail doit être compensée", "N",
  tf="La consolidation restant nécessaire, toute nouvelle baisse des prélèvements sur le travail exige des mesures compensatoires",
  res="Toute nouvelle baisse des prélèvements sur le travail doit être compensée, de préférence par des taxes sur la consommation (surtout nuisible à l'environnement) et sur le capital.",
  note="Principe de neutralité.")
M(178, "F25", "Budget pluriannuel pour chaque niveau de pouvoir", "P",
  tf="Une application crédible des règles budgétaires exige que chaque niveau de pouvoir établisse un budget pluriannuel",
  res="Chaque gouvernement doit adopter dès le début de la législature un budget pluriannuel avec des mesures décidées pour toute la période.",
  note="Procédure.")
M(179, "F25", "Encadrer les gouvernements en affaires courantes", "P",
  tf="Surveillance plus étroite et règles plus strictes pour le budget des gouvernements en affaires courantes",
  res="Renforcer le contrôle budgétaire des gouvernements en affaires courantes.",
  note="Actuel : sans budget 2027 voté avant le 31 décembre 2026, l'État fonctionnera en douzièmes provisoires.")
M(180, "F01", "Uniformiser l'imposition entre sources de revenus", "R", (0, 4000, 8000), (0.0, 0.6), "E", dl=2,
  res="Globaliser travail et capital (loyers et plus-values compris), ou taxer le patrimoine à un niveau équivalent à celui du travail ; selon le choix, la recette augmente ou reste stable.",
  note="Rendement compris entre zéro (glissement) et une globalisation complète.")
M(181, "F27", "Facturer la police aux grands événements payants", "R", (30, 80, 150), (0.5, 1.0), "D", comp="M",
  res="Facturer le maintien de l'ordre aux organisateurs d'événements commerciaux payants (festivals, matchs de football), jamais aux manifestations.",
  note="Ordre de grandeur ; recettes partagées avec les zones de police locales.")
M(182, "F11b", "Taxe carbone ou taxe kilométrique", "R", (300, 1000, 2500), (0.3, 0.6), "D", comp="M",
  res="Une taxe sur la tonne de CO2, en plus de la TVA, et/ou une taxe kilométrique, pour mieux appliquer le principe pollueur-payeur.",
  note="La taxe kilométrique est régionale ; l'ETS2 européen s'applique aux carburants et au chauffage à partir de 2028.")
M(183, "F22", "Financement monétaire de la transition", "X", comp="BCE", veh="-", dl=3,
  res="Créer de la monnaie à la banque centrale pour financer sans intérêts des investissements de transition, sous un contrôle démocratique strict.",
  note="Hors compétence belge : la politique monétaire relève de la BCE, et l'article 123 du TFUE interdit le financement monétaire des États.")
M(184, "F22", "Taxer le kérosène au niveau international", "P", comp="UE", veh="UE", dl=3,
  res="Lancer une concertation internationale pour taxer équitablement les carburants de l'aviation.",
  note="Dépend d'accords internationaux.")
M(185, "F20", "Réduire les subsides aux entreprises ou les rendre remboursables", "D", (200, 500, 1000), (0.5, 1.0), "D",
  res="Évaluer les effets retour des subsides et supprimer ceux dont l'effet net est insuffisant, ou prévoir un remboursement par un pourcentage des bénéfices ultérieurs.",
  note="Ordre de grandeur.")
M(186, "F05", "Supprimer l'avantage des voitures de société (impôts et cotisations)", "R", (4000, 5000, 6000), (0.25, 0.55), "C",
  res="Supprimer les écarts d'impôts et de cotisations, pour l'entreprise et le travailleur, entre le salaire et la voiture de société.",
  note="Volets fiscal et parafiscal ; ordre de grandeur du BFP (WP 04-25) : 4,7 à 5,2 Md€ par an.", src=("bfp-wp-voitures",))
M(187, "F12b", "Imposer à l'IPP les revenus des sociétés de management", "R", (300, 800, 1500), (0.6, 1.0), "D",
  res="Supprimer ou durcir le statut des sociétés de management en soumettant une plus grande part de leurs revenus à l'IPP, idéalement tous les revenus des sociétés unipersonnelles.",
  note="Variante la plus large de F12b : paquet maximal.")
M(188, "F07", "Supprimer les niches fiscales", "R", (800, 2000, 3500), (0.4, 0.9), "E",
  res="Évaluer si les niches atteignent leurs objectifs et supprimer d'urgence celles qui ne les atteignent pas.",
  note="Hors voitures de société (F05). Variante la plus large : paquet maximal.")
M(189, "F26", "Recourir davantage aux partenariats public-privé", "P",
  res="Financer une partie des projets collectifs en partenariat avec le privé.",
  note="Selon les règles d'Eurostat, un PPP n'échappe à la dette publique que si le partenaire privé porte l'essentiel des risques : pas d'économie en soi.")
M(190, "F14i", "Délivrer les médicaments à l'unité", "D", (20, 50, 100), (0.3, 1.0), "D",
  res="Ne vendre que le nombre d'unités nécessaires au traitement prescrit, comme aux Pays-Bas.",
  note="Instrument de la norme santé.")
M(191, "F26", "Faciliter les solidarités chaudes", "P",
  res="Analyser comment les mesures publiques encouragent ou pénalisent la solidarité familiale et de proximité.",
  note="Analyse, pas mesure.")
M(192, "F14i", "Encourager les soins au forfait", "P",
  res="Encourager les maisons médicales et le paiement au forfait plutôt qu'à l'acte.",
  note="Instrument de long terme de la norme santé.")
M(193, "F28", "Un réel tax shift du travail vers le capital", "N",
  res="Déplacer la pression fiscale du travail vers le capital, comme le recommandent de nombreuses institutions internationales.",
  note="Glissement neutre par construction.")
M(194, "F25", "Réduire la complexité institutionnelle", "P", comp="M", veh="REF", dl=3,
  res="Repenser l'organisation de la Belgique : absorption des provinces et des Communautés, suppression des réseaux d'enseignement…",
  note="Pas d'impact direct sur le budget fédéral, selon l'auteur lui-même.")
M(195, "F25", "Repenser les missions de l'État", "P",
  res="Analyser systématiquement la valeur ajoutée de l'intervention publique dans toutes les missions non régaliennes.",
  note="Procédure.")
M(196, "F25", "Prévention et soins sous le même pouvoir", "P", comp="M", veh="REF", dl=3,
  res="Organiser les institutions pour que les économies produites par la prévention d'une entité ne profitent pas à une autre.",
  note="Réforme institutionnelle.")
M(197, "F25", "Planifier le budget à long terme", "P",
  res="Autoriser des dépenses accrues à court terme si elles génèrent des économies supérieures à moyen terme, dans l'esprit du plan budgétaire et structurel à moyen terme européen.",
  note="Procédure.")
M(198, "F25", "Appliquer les recommandations de la Cour des comptes", "P",
  res="Analyser et, le cas échéant, mettre en œuvre les recommandations de la Cour des comptes, souvent ignorées.",
  note="Les recommandations chiffrables figurent dans d'autres fiches (taxe Caïman, réductions groupe cible, antibiotiques…).")
M(199, "F12b", "Réduire les avantages des sociétés de management", "R", (150, 400, 800), (0.8, 1.0), "D",
  res="Revoir le taux réduit et limiter des régimes comme le VVPR-bis pour freiner le passage en société de management.",
  note="Le précompte VVPR-bis a déjà été porté de 15 % à 18 % (accord de novembre 2025).", src=("lavenir-accord-2025",))
M(200, "F01", "Étudier la globalisation des revenus", "P",
  res="Étudier la globalisation de l'ensemble des revenus professionnels, mobiliers et immobiliers à l'IPP.",
  note="Étude préalable.")
