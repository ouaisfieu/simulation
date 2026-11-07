# -*- coding: utf-8 -*-
from base import M

Q = "Coût évité selon le calendrier de la réforme fiscale : 0,5 Md€ en 2027, 0,75 Md€ en 2028, 3,5 Md€ en 2029 (estimation OECCBB)."

M(66, "F08", "Abandonner la hausse de la quotité exemptée", "R", (3000, 3500, 4600), (0.143, 0.214), "B",
  tf="Abandonner le relèvement de la quotité exemptée d'impôt",
  res="Abandonner la hausse prévue de la quotité exemptée : en période budgétaire tendue, baisser l'impôt n'est pas réaliste et ce n'est pas le moyen le plus efficace de créer des emplois.",
  note=Q + " Variante du paquet maximal.", src=("oeccbb-quotite",))
M(67, "F08", "Transférer la baisse d'impôt aux Régions", "N", (0, 0, 1050), (0.143, 0.214), "B", comp="M",
  tf="Transférer la baisse d'impôt vers les Régions",
  res="Abandonner la hausse fédérale de la quotité exemptée et laisser les Régions accorder une baisse équivalente, qu'elles financent par d'autres impôts.",
  note="Pour le fédéral, économie de 3,5 Md€ en 2029. Pour l'ensemble des pouvoirs publics, neutre si les Régions financent la baisse par d'autres impôts, comme le prévoit le texte.", src=("oeccbb-quotite",))
M(68, "F01", "Dual income tax : un taux unique sur le capital", "R", (-1000, 1500, 4000), (0.0, 0.5), "E", dl=2,
  tf="Dual income tax (impôt dual)",
  res="Taxer tous les revenus du capital (dividendes, plus-values, loyers…) à un taux proportionnel unique, par exemple 20 % ou 25 %.",
  note="Selon le taux, le rendement peut être positif (loyers et plus-values aujourd'hui peu taxés) ou négatif (intérêts et dividendes aujourd'hui à 30 %). Architecture incompatible avec la globalisation progressive.")
M(69, "F26", "Grand nettoyage de la réglementation", "P",
  tf="Grand nettoyage dans la réglementation",
  res="Simplifier en profondeur les réglementations fédérales, régionales et locales pour renforcer la concurrence entre entreprises.",
  note="« Gratuit » selon son auteur ; effet de productivité à long terme.")
M(70, "F18", "Supprimer l'indexation automatique des salaires", "D", (-500, 500, 1500), (0.5, 1.0), "E",
  tf="Supprimer l'indexation automatique des salaires et la loi sur la norme salariale",
  res="Abolir dès l'année suivante l'indexation automatique des salaires et la loi de 1996 sur la norme salariale.",
  note="Effet budgétaire ambigu : moins de dépenses salariales publiques, mais moins de recettes sur les salaires privés. Contredit l'harmonisation de l'indexation (BFP-054) et le refus de toute suspension (BFP-094).")
M(71, "F05", "Revoir le calcul de l'avantage voiture de société", "R", (800, 1500, 2500), (0.6, 0.9), "C",
  res="Rapprocher la formule forfaitaire de l'avantage de toute nature de l'avantage réel, éventuellement en distinguant les voitures avec et sans carte carburant.",
  note="Variante partielle de la famille F05. Ordre de grandeur : un tiers à la moitié de l'avantage fiscal des voitures de société.", src=("bfp-wp-voitures",))
M(72, "F01", "Uniformiser le précompte mobilier à 30 %", "R", (300, 600, 1200), (0.8, 1.0), "C", dl=0,
  res="Porter à 30 % tous les taux du précompte mobilier (intérêts d'épargne au-delà du plafond exonéré, régimes réduits) et prévoir un plafond d'exonération commun.",
  note="Variante « taux unique » de F01, incompatible avec une globalisation progressive. Perception à la source : effet rapide.")
M(73, "F25", "Davantage de revues de dépenses", "P",
  res="Multiplier les revues de dépenses (spending reviews) pour identifier des économies supplémentaires.",
  note="Outil, pas mesure : aucun effet chiffrable à deux ans.")
M(74, "F06", "Revoir le traitement des flexi-jobs", "R", (100, 250, 450), (0.8, 1.0), "D",
  res="Réduire le plafond de l'exonération fiscale des flexi-jobs, ou les imposer à taux réduit dès le premier euro.",
  note="Ordre de grandeur. Variante du paquet médian.")
M(75, "F24", "Renforcer les services de contrôle fiscal", "R", (100, 400, 1000), (0.2, 0.6), "E",
  res="Affecter et engager davantage d'agents aux services de contrôle pour améliorer la perception.",
  note="Le BFP juge le chiffrage de la lutte contre la fraude « très hasardeux ». L'accord de novembre 2025 prévoit déjà 377 inspecteurs et 472 M€ par an.", src=("bfp-rapport", "lavenir-accord-2025"))
M(76, "F19e", "Supprimer des dépenses fédérales en compétences régionales", "D", (50, 150, 300), (0.6, 1.0), "D",
  tf="Supprimer diverses dépenses relevant des compétences des Communautés et des Régions (par exemple en politique scientifique)",
  res="Supprimer des dépenses fédérales qui relèvent de compétences communautaires ou régionales, par exemple en politique scientifique.",
  note="Ordre de grandeur.")
M(77, "F21b", "Faire cofinancer la police par les Régions", "T", (100, 300, 500), (0.5, 1.0), "D", comp="M", veh="AC",
  tf="Associer les Régions au financement des zones de police et de secours",
  res="Faire participer les Régions au financement des zones de police et de secours.",
  note="Transfert de charge : gain fédéral, coût régional. L'effet pour l'ensemble des pouvoirs publics dépend de la réaction des Régions.")
M(78, "F21b", "Réforme de l'État et révision de la loi de financement", "P", comp="M", veh="REF", dl=3,
  tf="Un traitement de fond des finances publiques exige une réforme de l'État et une révision profonde de la loi spéciale de financement",
  res="Le problème des finances publiques ne se réglera que par une réforme de l'État et une révision profonde de la loi spéciale de financement.",
  note="Majorité spéciale requise ; hors de portée en deux ans.")
M(79, "F22", "Relever les frais de perception des droits de douane", "P", comp="UE", veh="UE", dl=3,
  tf="Lors des négociations sur les nouvelles ressources propres, tenter de relever les 25 % de frais de perception des droits de douane",
  res="Négocier une hausse de la part des droits de douane conservée par l'État qui les perçoit (25 % aujourd'hui), avantageuse pour un pays portuaire comme la Belgique.",
  note="Décision des Vingt-Sept à l'unanimité : aucun effet unilatéral à deux ans.")
M(80, "F22", "Limiter la contribution belge au budget européen", "P", comp="UE", veh="UE", dl=2,
  tf="Suivre de près les discussions sur le nouveau cadre financier pluriannuel de l'Union pour limiter la contribution supplémentaire de la Belgique",
  res="Négocier le cadre financier pluriannuel 2028-2034 de façon à limiter la hausse de la contribution belge.",
  note="Négociation à vingt-sept : aucune économie unilatérale.")
M(81, "F10", "TVA : taux réduit de 7-8 % et normal de 22-23 %", "R", (2000, 3000, 4500), (0.9, 1.0), "D",
  tf="Réforme de la TVA : taux réduit de 7 à 8 % et taux normal de 22 à 23 %",
  res="Deux taux de TVA : un taux réduit de 7 à 8 % et un taux normal de 22 à 23 %.",
  note="Ordre de grandeur : hausse du taux normal (1,5 à 2 Md€ par point) et du taux de 6 %, baisse du taux de 12 %. Avant effets induits par l'indexation.")
M(82, "F24", "Lutter contre les abus en matière de droits d'auteur", "R", (30, 100, 200), (0.6, 1.0), "D",
  tf="S'attaquer aux abus en matière de droits d'auteur",
  res="Mettre fin à l'utilisation abusive du régime fiscal favorable des droits d'auteur.",
  note="Régime déjà resserré en 2023 : rendement additionnel limité.")
M(83, "F04", "Imposer les revenus locatifs privés", "R", (300, 676, 1000), (0.0, 0.6), "D", dl=2,
  tf="Imposer les revenus locatifs privés",
  res="Imposer les loyers perçus par les particuliers sur leur montant réel.",
  note="Même assiette que la mesure Vooruit chiffrée (BFP-020) : même ordre de grandeur.")
M(84, "F05", "Encadrer les cartes carburant des voitures de société", "R", (400, 700, 1200), (0.7, 1.0), "D",
  tf="L'usage des cartes carburant en lien avec les voitures de société",
  res="Revoir le traitement des cartes carburant accordées avec les voitures de société.",
  note="Variante partielle de la famille F05.", src=("bfp-wp-voitures",))
M(85, "F05c", "Intégrer chèques-repas et éco-chèques au salaire, taux en baisse", "N", (-500, 0, 1500), (0.5, 1.0), "E",
  tf="Supprimer éco-chèques et chèques-repas en les intégrant au salaire normal, avec une réforme de l'IPP et des taux en baisse",
  res="Supprimer éco-chèques et chèques-repas en les intégrant au salaire normal, en combinaison avec une réforme de l'IPP comprenant des taux en baisse.",
  note="Couplée à une baisse des taux : neutre par construction.")
M(86, "F07b", "Étendre le troisième pilier de pension", "C", (-300, -150, -50), (0.3, 1.0), "D",
  tf="Extension du troisième pilier de pension",
  res="Élargir l'avantage fiscal de l'épargne-pension individuelle.",
  note="Mesure coûteuse qui contredit la suppression de l'avantage (BFP-249, BFP-044) : exclue du paquet cohérent.")
M(87, "F23", "Poursuivre les ventes d'actifs fédéraux", "F", (0, 0, 0), (0.0, 0.0), "—",
  tf="Poursuivre la vente d'actifs fédéraux en tenant compte de leur intérêt stratégique",
  res="Vendre d'autres actifs fédéraux, en tenant compte de leur intérêt stratégique.",
  note="Opération financière : effet sur la dette, pas sur le déficit.")
M(88, "F14i", "Relever le ticket modérateur", "D", (150, 300, 500), (0.8, 1.0), "C",
  tf="Relever le ticket modérateur",
  res="Augmenter la part des soins payée par le patient.",
  note="Instrument de la norme santé : compté en sus seulement si l'option est activée. Ordre de grandeur (300 M€) repris de l'analyse de Fumée blanche.", src=("conclave",))
M(89, "F14i", "Franchise annuelle sur les frais médicaux", "D", (700, 1500, 2500), (0.5, 1.0), "D",
  tf="Instaurer une franchise sur les frais médicaux, avec correction sociale éventuelle : la mutualité n'intervient qu'au-delà d'un montant par année civile (par exemple 500 €)",
  res="La mutualité n'intervient qu'au-delà d'un montant annuel par patient, par exemple 500 €, avec une éventuelle correction sociale.",
  note="Ordre de grandeur. Risque de renoncement aux soins pour les ménages modestes si la correction sociale est faible.")
M(90, "F19", "Faire percevoir les cotisations par le SPF Finances", "P",
  tf="Économie administrative en confiant la perception des cotisations sociales au SPF Finances plutôt qu'à l'ONSS",
  res="Confier la perception des cotisations sociales au SPF Finances plutôt qu'à l'ONSS.",
  note="Gain administratif de long terme, non chiffrable à deux ans.")
M(91, "F16", "Passer à des pensions par capitalisation", "P", dl=3,
  tf="Long terme : transformer le système de pension par répartition en système par capitalisation",
  res="Remplacer progressivement la répartition par la capitalisation.",
  note="Pendant la transition, il faut payer les pensions en cours tout en alimentant les comptes individuels : coût de transition massif, de plusieurs points de PIB par an selon le rythme. Non modélisé sur deux ans.")
M(92, "F18", "Indexer une fois par an", "D", (300, 800, 1500), (1.0, 1.0), "D",
  tf="Faire courir désormais l'indexation pour tous après une année civile complète (par exemple 3 % d'inflation en 2026, indexation de ce pourcentage en février 2027)",
  res="Une seule indexation annuelle, pour tout le monde, après une année civile complète.",
  note="Le retard d'indexation réduit chaque année les dépenses sociales et salariales publiques, au prix d'une perte de pouvoir d'achat ; les recettes sur les salaires privés baissent aussi.")
M(93, "F18b", "Pas de suspension, même partielle, de l'indexation", "C", (-1200, -700, -300), (1.0, 1.0), "D",
  tf="Pas de suspension, même partielle, de l'indexation : elle réduit les recettes d'IPP et de cotisations, et l'indexation complète soutient le pouvoir d'achat",
  res="Ne pas suspendre l'indexation, même partiellement : cela réduit les recettes et le pouvoir d'achat.",
  note="Revenir sur le plafonnement de l'indexation décidé pour 2026 et 2028 coûte au budget. Contredit cinq propositions qui freinent l'indexation : exclue du paquet cohérent.", src=("lavenir-accord-2025",))
M(94, "F26", "Investissements militaires et industrie nationale", "P",
  tf="Utiliser la hausse des investissements militaires pour développer une industrie nationale, avec un effet de retour budgétaire",
  res="Orienter la hausse des investissements militaires vers une industrie de défense nationale.",
  note="Effet de retour possible mais non chiffré ; pas d'économie directe.")
M(95, "F19", "Réduire les coûts de fonctionnement : digitalisation", "D", (150, 400, 900), (0.2, 0.5), "D", inc="SP",
  res="Réduire de 10 % les coûts administratifs fédéraux (15 à 20 Md€) par la digitalisation complète des services, la fusion d'agences et le non-remplacement d'un départ à la retraite sur trois.",
  note="Les deux volets (digitalisation, fusions) se partagent l'objectif de 10 % : environ 0,8 Md€ à terme, montée en charge lente, coût d'investissement initial.")
M(96, "F19", "Réduire les coûts de fonctionnement : fusion d'agences", "D", (150, 400, 900), (0.2, 0.5), "D", inc="SP",
  res="Même objectif de 10 %, volet fusion d'agences et d'administrations.",
  note="Voir BFP-096. Recoupe le non-remplacement des départs (BFP-103).")
M(97, "F07", "Réduire de 5 % les dépenses fiscales inefficaces", "R", (800, 1500, 2500), (0.4, 0.9), "D",
  res="Supprimer ou réduire de 5 % les avantages fiscaux les moins efficaces, sur un total de 45 à 50 Md€ par an.",
  note="Hors voitures de société (comptées en F05) : ordre de grandeur de 1,5 Md€.")
M(98, "F17", "Mieux cibler les transferts sociaux et lutter contre la fraude sociale", "D", (200, 700, 2400), (0.3, 0.7), "E",
  res="Réduire de 2 % les dépenses sociales (plus de 120 Md€) par le ciblage et le contrôle, notamment contre la fraude sociale, estimée entre 1 et 3 Md€.",
  note="L'objectif de 2 % (2,4 Md€) paraît hors de portée en deux ans ; 0,7 Md€ retenu.")
M(99, "F17", "Limiter le cumul d'allocations", "D", (50, 200, 500), (0.5, 1.0), "D",
  res="Limiter certains cumuls d'allocations.",
  note="Ordre de grandeur.")
M(100, "F17", "Renforcer la dégressivité du chômage de longue durée", "D", (0, 100, 300), (0.5, 1.0), "D",
  res="Renforcer la dégressivité des allocations de chômage de longue durée.",
  note="Le chômage est limité dans le temps depuis le 1er janvier 2026 : le BFP note que ces mesures sont déjà largement adoptées. Gain résiduel faible.", src=("bfp-rapport",))
M(101, "F19", "Geler deux ans les salaires de la fonction publique fédérale", "D", (250, 400, 600), (0.5, 1.0), "C",
  res="Gel des salaires pendant deux ans, sans indexation ni augmentation barémique, mandataires politiques compris.",
  note="Masse salariale fédérale : 10,9 Md€ (2026). Deux ans sans index ni barème représentent 5 à 6 % de la masse, dont une partie revient en impôts et cotisations : 0,4 Md€ retenu.", src=("bfp-rapport",))
M(102, "F19", "Ne remplacer que deux départs à la retraite sur trois", "D", (150, 300, 500), (0.33, 0.67), "C",
  res="Remplacer seulement deux départs à la retraite sur trois pendant cinq ans.",
  note="Économie cumulative ; recoupe le volet non-remplacement de BFP-096.")
M(103, "F14i", "Budgets hospitaliers fermés", "P",
  res="Norme de croissance réduite (par exemple de 2,5 % à 1,5 %), baisse du prix des médicaments, moins d'actes inutiles ; concrètement, des budgets hospitaliers fermés.",
  note="Instrument de la norme de croissance (F14).")
M(104, "F14i", "Encadrer les prescriptions", "P",
  res="Même objectif de norme réduite, volet prescriptions encadrées.", note="Instrument de la norme de croissance (F14).")
M(105, "F14i", "Digitaliser le dossier patient", "P",
  res="Même objectif de norme réduite, volet digitalisation des dossiers patients.", note="Instrument de la norme de croissance (F14).")
M(106, "F24", "Croiser les bases de données contre la fraude", "R", (100, 400, 1000), (0.2, 0.6), "E",
  res="Croisement automatique des bases de données et contrôles ciblés sur la base des données.",
  note="Chiffrage hasardeux ; recoupe les autres mesures anti-fraude.")
M(107, "F09d", "Imposer à 20 % les pensions des non-résidents", "R", (30, 100, 200), (0.5, 1.0), "D", inc="EXT",
  res="Prélèvement libératoire de 20 % à la source sur les pensions belges versées à des non-résidents.",
  note="Limité par les conventions préventives de la double imposition.")
M(108, "F16b", "Cotisation santé des pensionnés non-résidents", "R", (30, 100, 200), (0.5, 1.0), "D",
  res="Cotisation santé spécifique (par exemple 4 % de la pension) pour les pensionnés belges vivant ailleurs dans l'UE et dont les soins sont financés par la Belgique.",
  note="Ordre de grandeur ; compatibilité avec la coordination européenne de sécurité sociale à vérifier.")
M(109, "F26", "Lutter contre les pièges au chômage", "P",
  res="Lutter contre les pièges au chômage et augmenter l'offre de travail.", note="Objectif sans modalités.")
M(110, "F24", "Combattre la fraude fiscale et sociale", "R", (100, 300, 800), (0.2, 0.6), "E",
  res="Combattre la fraude fiscale et sociale.", note="Sans modalités ; recoupe BFP-076 et BFP-107.")
M(111, "F01", "Dual income tax et mises en société", "R", (-1000, 1500, 4000), (0.0, 0.5), "E", dl=2,
  res="Mieux taxer les revenus les plus élevés, le patrimoine et les mises en société, par un système d'impôt dual.",
  note="Même architecture que BFP-069.")
M(112, "F21b", "Modifier la LSF et négocier des économies concertées", "P", comp="M", veh="LS", dl=3,
  res="Modifier la loi spéciale de financement, simplifier l'administration et négocier des économies concertées entre entités en comité de concertation.",
  note="Réforme institutionnelle : pas d'effet chiffrable à deux ans.")
M(113, "F07", "Élargir la base : dépenses fiscales et déductions spéciales", "P",
  res="Supprimer les avantages fiscaux, dont les voitures de société, les flexi-jobs, les jobs étudiants et le régime de l'intérêt substantiel dans la taxe sur les plus-values.",
  note="Mesure de synthèse : ses composantes sont comptées dans les familles F05, F06 et F03.")
M(114, "F08", "Au minimum, limiter la baisse d'impôt annoncée", "R", (1200, 1750, 2300), (0.143, 0.214), "D",
  tf="Au minimum, restreindre la baisse d'impôt annoncée",
  res="Restreindre au moins la baisse d'impôt annoncée, très coûteuse et mal ciblée.",
  note="Hypothèse : la moitié de la hausse de la quotité exemptée est abandonnée. Variante du paquet médian.", src=("oeccbb-quotite",))
M(115, "F25", "Raisonner en coût net de la fonction publique", "P",
  res="Évaluer les économies sur la fonction publique en coût net, hors IPP et cotisations qui reviennent à l'État.",
  note="Recommandation de méthode, pas une mesure d'économie. Fumée blanche lui attribue 1,2 Md€ (« Raboter le coût de la fonction publique ») : cette lecture n'est pas reprise ici.", src=("conclave",))
M(116, "F13d", "Cotisation sociale sur les revenus mobiliers", "R", (600, 1200, 2000), (0.8, 1.0), "D",
  res="Cotisation sociale de 5 % sur tous les revenus mobiliers des assujettis à la sécurité sociale belge, et de 10 % sur les revenus mobiliers que les dirigeants tirent de leur société.",
  note="Ordre de grandeur, sur une assiette de revenus mobiliers de 15 à 20 Md€. Se cumule avec la globalisation : l'érosion est alors plus forte.")
M(117, "F04", "Réviser la fiscalité immobilière (loyers réels ou RC actualisé)", "R", (200, 500, 900), (0.0, 0.6), "D", dl=2,
  res="Sortir du revenu cadastral périmé : taxer les loyers réels nets, ou au moins actualiser le RC sur la base de la valeur vénale.",
  note="Ordre de grandeur.")
M(118, "F21b", "Activer la concertation fiscale de la LSF", "P", comp="M", veh="-",
  res="Activer l'article 8 de la LSF, qui prévoit une concertation annuelle sur la politique fiscale entre entités.",
  note="Procédure.")
M(119, "F19", "Harmoniser IPP et cotisations sociales", "P",
  res="Unifier ou harmoniser les prélèvements IPP et cotisations sociales, ou au moins leur perception.",
  note="Réforme de structure ; pas d'effet direct.")
M(120, "F22", "Harmonisation européenne de l'impôt des sociétés", "P", comp="UE", veh="UE", dl=3,
  res="Harmoniser au niveau européen la base et le taux de l'impôt des sociétés.",
  note="Décision à l'unanimité ; hors de portée à deux ans.")
M(121, "F05", "Évaluer tous les avantages de toute nature à leur valeur réelle", "R", (600, 1200, 2000), (0.7, 1.0), "C",
  res="Valoriser tous les avantages de toute nature à leur valeur vénale (article 36 du CIR), en particulier les véhicules de société.",
  note="Variante partielle de F05.", src=("bfp-wp-voitures",))
M(122, "F05", "Revoir le budget mobilité", "R", (20, 50, 100), (0.8, 1.0), "D",
  res="Limiter la part du budget mobilité qui peut être consacrée au logement.",
  note="Variante très partielle de F05.")
M(123, "F01", "Un taux unique pour tous les revenus mobiliers", "R", (300, 600, 1200), (0.8, 1.0), "C", dl=0,
  res="Supprimer les différences de taux entre intérêts, dividendes, droits d'auteur… au profit d'un taux unique.",
  note="Variante « taux unique » de F01, incompatible avec la globalisation progressive.")
M(124, "F09d", "Taux par défaut sur les revenus non visés par le Code", "R", (0, 100, 300), (0.0, 0.8), "E",
  res="Imposer par défaut, par exemple à 30 %, les revenus que le Code des impôts ne vise pas et qui échappent aujourd'hui à l'impôt.",
  note="Assiette inconnue.")
M(125, "F09d", "Revenus distincts et exonérés pour les avantages fiscaux", "R", (50, 150, 300), (0.0, 0.8), "D",
  res="Tenir compte des revenus imposés distinctement et des revenus exonérés pour l'octroi des avantages fiscaux.",
  note="Ordre de grandeur.")
M(126, "F17b", "Revenus distincts et exonérés pour les avantages sociaux", "D", (100, 300, 600), (0.2, 0.6), "D",
  res="Tenir compte des revenus imposés distinctement et des revenus exonérés pour l'octroi des avantages sociaux.",
  note="Variante de la famille F17b.")
M(127, "F09d", "Impôt minimum sur les très hauts revenus", "R", (100, 400, 800), (0.0, 0.8), "D",
  res="Sur le modèle américain, un impôt moyen effectif d'au moins 30 %, par exemple au-delà de 200 000 € de revenus.",
  note="Ordre de grandeur ; dépend de la définition du revenu retenue.")
M(128, "F12e", "Étendre la taxe bancaire aux banques privées", "R", (20, 50, 100), (1.0, 1.0), "D",
  res="Étendre la taxe bancaire aux banques privées.", note="Ordre de grandeur.")
M(129, "F12a", "Supprimer la condition des 2,5 M€ pour les RDT", "R", (100, 300, 600), (0.8, 1.0), "D",
  res="Ne garder que le seuil de participation de 10 % pour la déduction RDT, en supprimant l'alternative d'une valeur d'acquisition de 2,5 M€.",
  note="Variante partielle de F12a.")
M(130, "F10b", "Taxe sur les services numériques", "R", (100, 200, 400), (0.5, 1.0), "D",
  res="Additionnel de 3 % à la TVA, non déductible, sur la publicité en ligne et le stockage de données, voire l'e-commerce.",
  note="Ordre de grandeur ; risque de mesures de rétorsion commerciales.")
