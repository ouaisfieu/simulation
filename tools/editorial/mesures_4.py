# -*- coding: utf-8 -*-
from base import M

M(201, "F06", "Soumettre flexi-jobs et jobs étudiants aux cotisations", "R", (200, 400, 800), (0.8, 1.0), "D",
  res="Soumettre flexi-jobs et jobs étudiants aux cotisations sociales, éventuellement réduites, voire dans une mesure limitée à l'IPP.",
  note="Variante la plus large de F06 : paquet maximal. Une partie des heures disparaîtrait.")
M(202, "F05", "Imposer davantage les voitures de société", "R", (1500, 2500, 4000), (0.6, 1.0), "D",
  res="Imposer davantage les voitures de société, fiscalement et/ou parafiscalement.",
  note="Variante partielle de F05.", src=("bfp-wp-voitures",))
M(203, "F24", "Durcir la taxe Caïman", "R", (50, 150, 250), (0.5, 1.0), "D",
  res="Mettre en œuvre les recommandations non suivies de la Cour des comptes sur la taxe Caïman (rapport de suivi 2026).",
  note="Fumée blanche retient 250 M€ (haut de fourchette).", src=("conclave",))
M(204, "F13b", "Réductions groupe cible : suivre la Cour des comptes", "R", (50, 200, 400), (0.5, 1.0), "D",
  res="Mettre en œuvre les recommandations de la Cour des comptes sur les réductions groupe cible de cotisations patronales (premiers engagements, 2025).",
  note="Ordre de grandeur ; recoupe la réduction premier engagement (F13c).")
M(205, "F20", "Limiter les dépenses fiscales en faveur des entreprises", "R", (100, 300, 600), (0.5, 1.0), "D",
  res="Limiter les dépenses fiscales à destination des entreprises, faute d'efficacité économique démontrée et d'évaluation.",
  note="Renvoie au rapport de la Cour des comptes sur le budget 2026.")
M(206, "F13a", "Supprimer le plafond de 340 000 € des cotisations patronales", "R", (50, 150, 400), (1.0, 1.0), "D",
  res="Revenir sur la décision de ne plus prélever de cotisations patronales au-delà de 340 000 € bruts par an.",
  note="Assiette étroite (quelques milliers de rémunérations). Fumée blanche retient 400 M€, en haut de fourchette. Variante du paquet.", src=("conclave",))
M(207, "F14i", "Mieux contrôler le coût des médicaments", "D", (100, 300, 600), (0.4, 0.8), "D",
  res="Négociation des prix et contrats confidentiels, politique des génériques et biosimilaires, réforme du remboursement, encadrement des prix des médicaments innovants, lutte contre les pénuries.",
  note="Instrument de la norme santé.")
M(208, "F14i", "Forfaits par pathologie", "D", (0, 100, 300), (0.2, 0.5), "E",
  res="Financer certaines pathologies (diabète, oncologie) par des forfaits.", note="Instrument de long terme de la norme santé.")
M(209, "F14i", "Antibiotiques : suivre la Cour des comptes", "D", (5, 20, 50), (0.5, 1.0), "D",
  res="Poursuivre la mise en œuvre des recommandations de la Cour des comptes sur la prescription et la délivrance des antibiotiques.",
  note="Petit montant ; instrument de la norme santé.")
M(210, "F26", "Économie circulaire", "P",
  res="Mettre en œuvre les recommandations de la Cour des comptes sur l'économie circulaire.", note="Pas d'effet budgétaire direct à deux ans.")
M(211, "F19", "Mieux gérer les marchés publics", "D", (0, 100, 300), (0.2, 0.5), "D",
  res="Corriger les dysfonctionnements des marchés publics fédéraux relevés par la Cour des comptes (2025).", note="Gain d'efficience de long terme.")
M(212, "F19", "Fin du cumul logement de fonction et indemnité pour les ministres", "D", (0, 0.5, 1), (1.0, 1.0), "D",
  res="Mettre fin au cumul possible d'une indemnité de logement et d'un logement mis à disposition pour les ministres fédéraux.",
  note="Symbolique : moins d'un million d'euros.")
M(213, "F19", "Limiter le nombre de collaborateurs parlementaires", "D", (5, 10, 20), (0.5, 1.0), "D",
  res="Réduire la dotation de la Chambre en limitant le nombre de collaborateurs parlementaires, dont une partie travaille pour les partis, déjà financés par ailleurs.",
  note="Exemplarité ; montant faible. Relève de l'autonomie de la Chambre.")
M(214, "F18b", "Abandonner le centim'index (proposition des partenaires sociaux)", "C", (-900, -300, 0), (1.0, 1.0), "D",
  res="Abandonner le centim'index, dont la complexité impose de coûteuses adaptations des logiciels de paie, et suivre la proposition des interlocuteurs sociaux.",
  note="Nul si l'alternative des partenaires sociaux rapporte autant, coûteux sinon. Fumée blanche intitule cette fiche « Prolonger le centim'index » (+883 M€), ce qui inverse son sens.", src=("conclave",))
M(215, "F25", "Un cycle budgétaire à la néerlandaise", "P",
  tf="Professionnaliser le cycle budgétaire fédéral sur le modèle néerlandais",
  res="Calendrier fixe : base du BFP, contrôle du CSF sur la trajectoire de dépenses nettes, revues de dépenses, fiches obligatoires au-delà d'environ 50 M€, document budgétaire public de 100 à 150 pages.",
  note="Procédure.")
M(216, "F25", "Norme de dépenses primaires avec ancre de dette", "P",
  tf="Norme de dépenses primaires avec ancre de dette et correction conjoncturelle",
  res="Les dépenses primaires récurrentes ne peuvent croître plus vite que le PIB nominal potentiel, diminué d'une correction pour la dette et la haute conjoncture.",
  note="Règle budgétaire ; alignée sur le cadre européen.")
M(217, "F25", "Revues de dépenses 2.0", "P",
  tf="Revues de dépenses 2.0 selon la logique néerlandaise (IBO)",
  res="Cinq à huit revues par an, chacune avec une option neutre, une option -10 % et une option -20 % ; le gouvernement répond selon le principe « appliquer ou expliquer ».",
  note="Procédure.")
M(218, "F25", "Clauses de caducité pour les dépenses fiscales", "P",
  tf="Clauses de caducité comme standard pour les dépenses fiscales fédérales",
  res="Chaque dépense fiscale fédérale reçoit une date d'expiration et n'est prolongée qu'après réexamen ; l'inventaire 2024 en recense 255 chiffrées, pour 39,4 Md€ de recettes perdues en 2023 (6,7 % du PIB).",
  note="Procédure ; effet à moyen terme.")
M(219, "F10", "Supprimer les taux réduits de TVA à finalité régionale", "R", (300, 800, 1500), (0.7, 1.0), "D",
  tf="Test de subsidiarité et d'efficacité pour les dépenses fiscales fédérales à finalité régionale ou communautaire",
  res="Éteindre les dépenses fiscales fédérales dont l'objectif est régional : TVA réduite sur la construction et la rénovation, l'horeca, la presse, dispense de précompte pour les travaux immobiliers, zones d'aide.",
  note="Variante de la famille TVA (recoupe BFP-222).")
M(220, "F11", "Accélérer la sortie des subsides fossiles fédéraux", "R", (800, 1500, 2500), (0.4, 0.7), "D",
  tf="Réduction et reconversion accélérées des subsides fédéraux aux énergies fossiles",
  res="Un calendrier fédéral de sortie : verdir encore voitures de société et cartes carburant, supprimer le diesel professionnel et les écarts d'accises, convertir les avantages mazout et gaz en aides ciblées.",
  note="Variante la plus large : paquet maximal. La Commission estimait les subsides fossiles fédéraux à 2,4 % du PIB en 2022 ; leur suppression ne rapporte qu'une fraction de ce montant.", src=("ce-csr-2026",))
M(221, "F10", "Élargir la base TVA en supprimant des taux réduits", "R", (500, 1000, 1800), (0.7, 1.0), "D",
  tf="Élargir la base de la TVA par l'extinction sélective des régimes réduits, avec un crédit d'impôt ciblé",
  res="Pas de hausse générale : supprimer progressivement des taux réduits (rénovation sans objectif énergétique, horeca, presse) en compensant par un crédit d'impôt ciblé.",
  note="Variante la plus légère de la famille TVA.")
M(222, "F24", "Offensive sur l'écart de TVA", "R", (300, 600, 1000), (0.3, 0.7), "D",
  tf="Offensive sur l'écart de TVA, au-delà de la facturation électronique déjà prévue",
  res="Exploiter la facturation électronique obligatoire depuis 2026 : déclarations préremplies, rapprochement des factures et des déclarations, scores de risque, contrôles ciblés.",
  note="Écart de TVA de 5,23 Md€ en 2023 (12,3 % de la TVA théorique), selon l'auteur. Fumée blanche retient 750 M€.", src=("conclave",))
M(223, "F20", "Auditer et plafonner les dispenses de précompte professionnel", "R", (300, 600, 1200), (0.5, 1.0), "D",
  tf="Auditer, plafonner et redessiner les subventions salariales et de précompte professionnel",
  res="Soumettre les dispenses de versement du précompte professionnel (4,4 Md€ en 2024, dont 2,6 Md€ pour l'emploi et 1,6 Md€ pour la R&D) à un test d'additionnalité, les plafonner et les redessiner.",
  note="Ordre de grandeur.")
M(224, "F20", "Convertir les subsides en contrats de résultats", "P",
  tf="Convertir les subsides directs fédéraux en contrats de résultats",
  res="Remplacer les subsides ouverts par des contrats limités dans le temps, avec objectifs mesurables, plafond, évaluation et clause de récupération.",
  note="Effet de moyen terme.")
M(225, "F28", "Âge de la pension à la carte, actuariellement neutre", "N",
  tf="L'âge de la pension comme droit ouvert, avec un bonus-malus actuariellement neutre et un lien à l'espérance de vie en bonne santé",
  res="Faire de l'âge légal un âge à partir duquel on peut demander sa pension, avec un bonus-malus actuariellement neutre et un lien à l'espérance de vie en bonne santé.",
  note="Neutre par construction pour la sécurité sociale, selon son auteur. Fumée blanche lui attribue 1,5 Md€ : cette lecture n'est pas reprise ici.", src=("conclave",))
M(226, "F14i", "Médicaments : contrats fondés sur la valeur", "D", (50, 150, 300), (0.3, 0.7), "D",
  tf="Budget des médicaments : MORSE+, contrats fondés sur la valeur et accès « valeur positive »",
  res="Piloter le budget des médicaments par une cellule de prévision, des prix par indication, des paiements liés aux résultats et des clauses prix-volume.",
  note="Instrument de la norme santé.")
M(227, "F14i", "Supprimer les soins de faible valeur", "D", (50, 200, 400), (0.3, 0.7), "D",
  tf="Supprimer les soins de faible valeur et lier davantage le remboursement INAMI aux preuves",
  res="Identifier chaque année les soins, examens et médicaments de faible valeur et lier le remboursement aux preuves.",
  note="Instrument de la norme santé.")
M(228, "F04b", "Péréquation du revenu cadastral sur dix ans", "R", (600, 1500, 2500), (0.33, 0.67), "D", comp="M",
  tf="Péréquation fédérale du revenu cadastral étalée sur dix ans",
  res="Réévaluer progressivement le revenu cadastral sur dix ans (un dixième de l'écart par an), à partir des données existantes : transactions, permis, certificats PEB, superficies.",
  note="Le RC renvoie encore à la valeur locative de 1975. Le gain irait surtout au précompte immobilier régional et communal, une partie à l'IPP (secondes résidences, biens loués).")
M(229, "F19", "Régie des Bâtiments, gestionnaire actif", "D", (30, 100, 200), (0.2, 0.5), "D",
  tf="La Régie des Bâtiments comme gestionnaire immobilier actif : cadastre, normes d'occupation et rénovation énergétique rentable",
  res="Cadastre immobilier, normes d'occupation, vente ou location des actifs excédentaires (4,8 % de vacance sur plus de 7 millions de m²), rénovations rentables.",
  note="Gain de long terme.")
M(230, "F11d", "Incitants fiscaux énergie-climat ciblés", "C", (-500, -200, 0), (0.5, 1.0), "E",
  res="Des incitants fiscaux annoncés à l'avance, ciblés et temporaires pour les ménages et les entreprises.",
  note="Dépense fiscale nouvelle : coût.")
M(231, "F09a", "Réduire la pression parafiscale sur le travail", "C", (-3000, -1500, -500), (0.5, 1.0), "E",
  res="Revoir la progressivité des taux marginaux de prélèvement pour réduire les pièges à l'emploi et à la promotion.",
  note="Non compensé : coût. Variante alternative au paquet BFP-046/047.")
M(232, "F11", "Démanteler plus vite les subsides fossiles", "R", (600, 1200, 2000), (0.4, 0.7), "D",
  tf="Démanteler plus rapidement les subsides fossiles",
  res="Accélérer la sortie des subsides fossiles dommageables prévue par l'accord de gouvernement et convenue avec la Commission européenne.",
  note="Variante de F11.")
M(233, "F20", "Raboter de 10 % les subsides économiques", "D", (500, 790, 900), (0.8, 1.0), "C",
  tf="Réduire de 10 % les subsides économiques par la méthode du rabot, en attendant un outil d'analyse de leur utilité sociale",
  res="Réduire immédiatement de 10 % tous les subsides économiques, puis garder ou supprimer chaque subside quand un outil d'évaluation existera.",
  note="10 % de 7,9 Md€ de subsides fédéraux. Fumée blanche retient le même montant.", src=("conclave", "bfp-rapport"))
M(234, "F09c", "Rendre imposables les allocations familiales", "R", (500, 1000, 2000), (0.3, 1.0), "D", comp="M",
  tf="Rendre les allocations familiales imposables",
  res="Les plus hauts revenus n'ont pas besoin d'aide à l'entretien des enfants ; l'imposition ne change rien pour les plus bas revenus.",
  note="Allocations familiales : de l'ordre de 8 à 9 Md€ par an, versées par les Communautés. Variante du paquet maximal pour F09c.")
M(235, "F19", "Inciter les administrations à innover", "P",
  tf="Stimuler l'innovation en matière d'efficience au sein de l'administration",
  res="Laisser aux services qui économisent une partie des moyens dégagés, pour que l'efficience ne les rende pas « moins importants ».",
  note="Incitant ; pas d'effet direct.")
M(236, "F19", "Norme 10 % + 10 % pour tous les SPF", "D", (300, 1000, 2500), (0.4, 0.8), "E",
  tf="Norme de 10 % + 10 % pour tous les SPF",
  res="Chaque SPF propose 10 % de simplification et 10 % de suppression de dépenses existantes ; le politique choisit dans cette liste.",
  note="Produit une liste d'options plutôt qu'une économie automatique.")
M(237, "F04", "Taxer les loyers, éventuellement de façon progressive", "R", (400, 900, 1500), (0.0, 0.6), "D", dl=2,
  res="Imposer les loyers réels, éventuellement selon un barème progressif : la Belgique est l'un des rares pays développés à ne pas le faire.",
  note="Variante la plus large de F04 : paquet maximal.")
M(238, "F09d", "Augmenter le nombre de tranches de l'IPP", "N", (-500, 0, 500), (0.0, 1.0), "E",
  res="Rétablir davantage de tranches pour supprimer les effets de seuil et l'imposition élevée des revenus moyens.",
  note="Effet dépendant du barème retenu.")
M(239, "F13a", "Annuler le plafonnement des cotisations sociales", "R", (50, 150, 400), (1.0, 1.0), "D",
  res="Annuler le plafonnement des cotisations sociales, vu la hausse rapide des dépenses liées au vieillissement.",
  note="Doublon de BFP-207.")
M(240, "F07", "Diminuer les niches fiscales de l'IPP", "R", (600, 1500, 2500), (0.4, 0.9), "D",
  res="Diminuer les dépenses fiscales de l'IPP, qui atteignaient près de 10 Md€ en 2023.",
  note="Hors voitures de société. Variante du paquet médian.")
M(241, "F02", "Relever la taxe sur les comptes-titres", "R", (300, 700, 1200), (0.8, 1.0), "C",
  res="Relever le taux de la taxe sur les comptes-titres ou instaurer un impôt sur la fortune.",
  note="Taux déjà doublé de 0,15 % à 0,30 % en novembre 2025 : nouveau relèvement estimé à 0,7 Md€. Fumée blanche retient 1 Md€.", src=("lavenir-accord-2025", "conclave"))
M(242, "F05", "Réduire ou supprimer les avantages des voitures de société", "R", (2000, 3000, 4500), (0.4, 0.8), "D",
  res="Diminuer ou supprimer les avantages fiscaux des voitures de société ; les estimations de pertes de recettes citées par l'auteur vont de 2 à 4 Md€.",
  note="Variante partielle de F05.", src=("bfp-wp-voitures",))
M(243, "F15b", "Allonger le salaire garanti à charge de l'employeur", "D", (300, 600, 1200), (0.7, 1.0), "D",
  res="Augmenter le nombre de mois indemnisés par l'employeur en cas d'incapacité de travail (30 jours aujourd'hui).",
  note="Économie pour l'assurance maladie, coût pour les employeurs : la charge se déplace. Le BFP rappelle que le gouvernement a déjà pris des mesures de responsabilisation.", src=("bfp-rapport",))
M(244, "F13b", "Limiter les réductions de cotisations patronales", "R", (200, 500, 900), (0.8, 1.0), "C",
  res="Limiter les réductions de cotisations patronales : le taux implicite net est passé de 32,6 % à 21,5 % de la masse salariale entre 1996 et 2025.",
  note="Fumée blanche retient 500 M€.", src=("conclave",))
M(245, "F12b", "Revoir les avantages des sociétés unipersonnelles", "R", (150, 400, 800), (0.8, 1.0), "D",
  res="Revoir les avantages des sociétés unipersonnelles, utilisées pour optimiser l'imposition des indépendants.",
  note="Variante du paquet médian.")
M(246, "F25", "Faire revenir les gains de la prévention à qui l'organise", "P", comp="M",
  tf="Assurer une meilleure coordination entre niveaux de pouvoir",
  res="Faire en sorte que les gains budgétaires de la prévention, de la remise au travail ou du travail plus long reviennent aux entités qui les produisent.",
  note="Réforme institutionnelle.")
M(247, "F13e", "Aligner les cotisations des indépendants sur celles des salariés", "R", (500, 1500, 3000), (0.5, 1.0), "D",
  res="À revenu égal, des cotisations équivalentes à celles des salariés (avec les mêmes droits) et la fin du plafonnement des cotisations des indépendants.",
  note="Ordre de grandeur ; les droits supplémentaires coûteraient ensuite. Contredit le plafonnement des cotisations (BFP-045).")
M(248, "F07", "Supprimer l'avantage du 3e pilier et des comptes d'épargne", "R", (600, 1000, 1400), (0.3, 0.9), "C",
  res="Supprimer l'avantage fiscal du troisième pilier de pension et celui des comptes d'épargne : tous les revenus devraient être traités de la même manière.",
  note="Fumée blanche retient 1 Md€. Contredit l'extension du troisième pilier (BFP-087).", src=("conclave",))
M(249, "F25", "Mieux répartir la charge entre niveaux de pouvoir", "P", comp="M",
  res="Défense et vieillissement pèsent surtout sur l'Entité I : mieux répartir l'effort entre niveaux de pouvoir, en tenant compte de la situation de chaque entité.",
  note="Orientation, sans mécanisme précis.")
M(250, "F25", "Gouvernance budgétaire et évaluation (I)", "P",
  res="Systématiser les revues de dépenses et développer une culture de l'évaluation des politiques publiques.", note="Procédure.")
M(251, "F25", "Gouvernance budgétaire et évaluation (II)", "P",
  res="Renforcer l'autonomie et les moyens du Conseil supérieur des Finances ; revoir le définancement du Comité d'étude sur les investissements publics.", note="Procédure.")
M(252, "F25", "Améliorer l'analyse de soutenabilité de la dette", "P",
  res="Corriger les failles méthodologiques de l'analyse de soutenabilité de la dette (DSA) européenne, notamment la sous-estimation de la croissance potentielle.", note="Procédure européenne.")
M(253, "F25", "Coordonner les niveaux de pouvoir", "P", comp="M",
  res="Négocier un accord de coopération budgétaire contraignant, aligné sur les règles européennes, avec une norme de dépenses nettes et un mécanisme de correction.",
  note="L'accord de coopération de 2013 n'a jamais été appliqué effectivement.")
M(254, "F26", "Leviers structurels : emploi et productivité", "P",
  res="Augmenter le taux d'emploi et la productivité.", note="Long terme.")
M(255, "F26", "Leviers structurels : investissement public", "P",
  res="Réorienter l'investissement public vers l'énergie, la mobilité, le numérique et la formation ; selon le FMI, transférer 2 % du PIB des dépenses courantes vers l'investissement sur cinq ans accroîtrait le PIB d'environ 6 % à long terme.",
  note="Long terme ; chiffre attribué au FMI par l'auteur.")
M(256, "F26", "Leviers structurels : cofinancement européen", "P",
  res="Maximiser le recours aux fonds européens ; le plan de relance belge (5,3 Md€) accroîtrait le PIB d'environ 0,2 % d'ici 2030 selon le BFP.", note="Long terme.")
M(257, "F25", "Des hypothèses macrobudgétaires réalistes", "P",
  res="Le plan budgétaire et structurel à moyen terme de 2025 reposait sur des effets retour jugés trop optimistes par le BFP et le Comité de monitoring ; intégrer les risques climatiques dès le budget 2027.",
  note="Procédure.")
M(258, "F25", "Impliquer les interlocuteurs sociaux", "P",
  res="La Commission européenne a relevé l'absence de consultation des partenaires sociaux dans l'élaboration du plan belge, pourtant exigée par le cadre européen.",
  note="Procédure.")
M(259, "F26", "Défense : un effort orienté vers la croissance", "P",
  res="Privilégier les dépenses de défense aux plus forts effets multiplicateurs et coordonner les marchés publics de défense au niveau européen.",
  note="Pas d'économie directe.")
M(260, "F10", "Adopter le système de TVA néerlandais (9 % et 21 %)", "R", (1200, 2000, 3000), (0.9, 1.0), "C",
  tf="Reprendre le système de TVA néerlandais pour la structure des taux et la classification des biens et services",
  res="Remplacer les taux de 6 % et 12 % par un taux unique de 9 % et reprendre la classification néerlandaise ; faire de la baisse d'impôt prévue (3,9 Md€) un glissement à rendement constant.",
  note="Les notes de travail du gouvernement (octobre 2026) chiffraient une variante proche (21 % → 22 %, 6 % et 12 % → 9 %) à près de 2 Md€. Variante du paquet médian. Avant effets induits par l'indexation.", src=("rtbf-pistes-2026",))
M(261, "F28", "Une vraie réforme fiscale, sortie du bricolage", "N",
  tf="Une vraie réforme fiscale, qui sorte du bricolage",
  res="Reprendre le plan de 2014 du Conseil supérieur des Finances : élargir les bases (selon la Commission, 2,4 points de PIB, soit 15 Md€, partent en déductions et exemptions) pour baisser les taux.",
  note="Glissement neutre par construction.")
M(262, "F18", "Lisser les prix fossiles et prolonger le centim'index", "D", (200, 500, 900), (1.0, 1.0), "D",
  tf="Lisser dans le temps les hausses de prix des carburants fossiles, en combinaison avec un centim'index comme lors des assainissements passés",
  res="Lisser les hausses de prix des carburants et plafonner l'indexation en montants (centim'index), comme lors des assainissements des années 1980 et 1990.",
  note="Ordre de grandeur : prolonger le plafonnement de l'indexation décidé pour 2026 et 2028.", src=("lavenir-accord-2025",))
M(263, "F14i", "Limiter le comptage des cellules endothéliales avant une opération de la cataracte", "D", (5, 10, 20), (0.8, 1.0), "C",
  tf="Économie sur le comptage des cellules endothéliales lors des opérations de la cataracte",
  res="Limiter le remboursement de ce test aux patients présentant une affection connue de la cornée, comme le recommande le KCE (2024).",
  note="Petit montant ; instrument de la norme santé.")
