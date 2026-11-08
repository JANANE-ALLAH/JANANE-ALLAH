# -*- coding: utf-8 -*-
# Regenere cours/licence-pro-hydraulique.md a partir des fichiers presents
# dans cours/hydraulique/.  Usage :  python tools/build_hydraulique.py
#
# Module 6 : Hydraulique - Licence Professionnelle IMPI, ENSAM Casablanca.
# Meme convention que tools/build_page.py : dans le dossier d'un chapitre,
# 1_ = cours, 3_ = TD, 4_ = TP, et "corrige" dans le nom = corrige.
# Les colonnes TD / TP / Corrige / Video n'apparaissent que si au moins un
# chapitre en a : on n'affiche pas de colonnes vides.
import io, os
from urllib.parse import quote

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cours")
B = "hydraulique"
PAGE = "licence-pro-hydraulique.md"

# Dossier, titre, descriptif (vide tant que le chapitre n'est pas publie).
CH = {
 "01": ("Chapitre_01_Generalites_systemes_hydrauliques", "Généralités sur les systèmes hydrauliques",
        "Hydraulique face au pneumatique et à l'électrique, chaîne d'énergie, grandeurs hydrauliques "
        "(pression, débit, force, puissance, rendement), Bernoulli, viscosité, régimes d'écoulement, "
        "compressibilité et pertes de charge. Durée indicative 6 à 8 h, applications chiffrées et "
        "TD corrigés intégrés, QCM d'auto-évaluation."),
 "02": ("Chapitre_02_Schemas_hydrauliques_pneumatiques", "Schémas hydrauliques et pneumatiques",
        "Symboles normalisés (ISO 1219) des pompes, vérins, distributeurs, clapets et limiteurs ; "
        "lecture d'un distributeur et chemin du fluide ; régulation de pression et de débit ; règles "
        "de représentation et de repérage ; construction d'un circuit simple à partir d'un cahier "
        "des charges. Exemple fil rouge : commande d'un vérin hydraulique à double effet. Durée "
        "indicative 5 à 7 h, exercices corrigés, QCM d'auto-évaluation."),
 "03": ("Chapitre_03_Technologie_systemes_hydrauliques", "Technologie des systèmes hydrauliques",
        "Les composants d'une installation, famille par famille : centrale, réservoirs, filtres, "
        "accumulateurs, pompes, moteurs, vérins, distributeurs, protection et régulation. Calculs de "
        "cylindrée, débit, couple et rendements, volume d'un accumulateur, effort et flambage d'un vérin, "
        "dimensionnement d'une centrale ; diagnostic des symptômes types (cavitation, colmatage, usure "
        "interne). Durée indicative 12 à 16 h hors TP, 9 exercices corrigés, fiches de formules, QCM "
        "d'auto-évaluation."),
 "04": ("Chapitre_04_Circuits_hydrauliques", "Circuits hydrauliques",
        "Les six familles de circuits : principe et lecture d'un schéma, circuits fermés (transmission "
        "hydrostatique, gavage, valve d'échange), circuits ouverts (série, parallèle, effet différentiel), "
        "maintien de pression (accumulateur et conjoncteur-disjoncteur, pompe autorégulatrice), commande de "
        "débit sous charge motrice et régulation de puissance (courbe à puissance constante). Calculs de "
        "débits, vitesses, couples, puissances et volume d'accumulateur ; symptômes types (échauffement à "
        "vide, patinage, chute de charge, perte de gavage). Durée indicative 8 à 10 h hors TP, 9 exercices "
        "corrigés, fiche de formules, QCM d'auto-évaluation."),
 "05": ("Chapitre_05_Maintenance_installations", "Maintenance des installations",
        "Une maintenance préventive planifiée : les huit vérifications journalières et les sept hebdomadaires, "
        "avec leurs critères (niveau, aspect et température de l'huile, filtres, pressions, fuites, "
        "accumulateurs, propreté ISO 4406), consignation et fiche d'historique ; durée de vie d'une pompe "
        "selon la vitesse, la pression (L₁₀ = (C/P)³), le fluide et l'alignement ; diagnostic des pannes de "
        "pompes, de l'aspect de la pièce à la cause ; cavitation, aération et budget de pression à "
        "l'aspiration. Durée indicative 6 à 8 h hors TP, 7 exercices corrigés, fiche de formules, QCM "
        "d'auto-évaluation et bilan du module."),
}

# Liens video par chapitre (meme regle d'acces que l'autre cours : compte UH2C).
VIDEOS = {
 "02": "https://drive.google.com/file/d/1kPl1OZvTW4uxDxojUoDT9yeFKKKwBmKj/view",
}

# Detail par chapitre (feuille de route et TP, tires du support de cours).
PARTIES = {}
TPS = {}
PARTIES["01"] = [
    ("Hydraulique et pneumatique", "Pourquoi choisir l'huile plutôt que l'air ?"),
    ("Énergie mécanique et hydraulique", "Comment l'énergie circule-t-elle de la source à la charge ?"),
    ("Grandeurs hydrauliques", "Comment calculer pression, débit, force, puissance ?"),
    ("Fluides en mouvement", "Que devient l'énergie le long d'une conduite ?"),
    ("Viscosité", "Pourquoi une huile trop épaisse ou trop fluide change tout ?"),
    ("Régimes d'écoulement", "L'écoulement est-il laminaire ou turbulent ?"),
    ("Compressibilité et dilatation", "L'huile est-elle vraiment incompressible ?"),
    ("Pertes de charge", "Combien de pression perd-on en route ?"),
]
TPS["01"] = [
    ("Lire la machine", "repérer moteur, pompes, distributeur, vérins ; lire plaques et symboles"),
    ("Pression et force", "lire un manomètre, relever la pression de tarage, calculer F = p · S"),
    ("Débit et vitesse", "chronométrer une course de vérin et en déduire Q = S · v"),
    ("Huile et température", "relever la température, lire la fiche d'huile, estimer le régime (Re)"),
    ("Pertes et diagnostic", "mesurer Δp d'un filtre ou d'un flexible, lire le vacuomètre d'aspiration"),
]
PARTIES["02"] = [
    ("Le langage du schéma", "Comment dessine-t-on des lignes, un réservoir, une source ?"),
    ("Régulation et protection", "Comment limiter la pression et régler le débit ?"),
    ("Distribution de l'énergie", "Comment aiguiller le fluide vers le bon actionneur ?"),
    ("Conversion de l'énergie", "Comment représenter pompes, moteurs et vérins ?"),
    ("Mesure et appareils complémentaires", "Comment voir ce qui se passe dans le circuit ?"),
    ("Lire et dessiner un schéma complet", "Comment lire, puis construire un circuit ?"),
]
TPS["02"] = [
    ("Lire la machine", "retrouver sur le schéma constructeur les symboles et leurs repères"),
    ("Identifier les composants", "associer chaque symbole à un composant du banc : plaques, orifices"),
    ("Câbler un circuit", "réaliser la commande d'un vérin double effet et vérifier les 3 positions"),
    ("Régler et mesurer", "tarer le limiteur de pression, régler la vitesse, lire les manomètres"),
    ("Dessiner et simuler", "dessiner le schéma d'une application et le valider, par simulation si possible"),
]
PARTIES["03"] = [
    ("Centrale hydraulique", "Comment est organisé le groupe de puissance ?"),
    ("Réservoirs", "Quel volume, quelles règles de conception ?"),
    ("Filtres", "Où placer le filtre et avec quelle finesse ?"),
    ("Accumulateurs", "Comment stocker l'énergie et l'amortir ?"),
    ("Pompes", "Quel type, quelle cylindrée, quel rendement ?"),
    ("Moteurs hydrauliques", "Quel couple, quelle vitesse ?"),
    ("Vérins", "Quel effort, quelle tige, quelle course ?"),
    ("Distributeurs", "Quelle taille, quelle commande ?"),
    ("Protection et régulation", "Comment limiter la pression et le débit ?"),
]
TPS["03"] = [
    ("Identifier", "nommer les composants d'une centrale ou d'une machine ; relever les plaques"),
    ("Mesurer une pompe", "relever Q, p, N et C ; calculer ηv, ηhm et ηg"),
    ("Accumulateur et filtre", "lire la précharge (hors pression), l'indicateur de colmatage, l'état du filtre"),
    ("Vérin et moteur", "chronométrer une course, calculer F, v et le débit ; repérer le gavage"),
    ("Distributeur et limiteur", "identifier la commande, câbler, tarer le limiteur et mesurer Δp"),
]
PARTIES["04"] = [
    ("Principe d'un circuit", "Quels blocs, dans quel ordre, et comment lit-on un schéma ?"),
    ("Circuits fermés", "Comment transmettre une puissance en boucle, dans les deux sens ?"),
    ("Circuits ouverts", "Comment manœuvrer vite, avec un ou plusieurs récepteurs ?"),
    ("Maintien de pression", "Comment garder la pression en attente sans gaspiller ?"),
    ("Commande de débit", "Comment régler une vitesse quand la charge est motrice ?"),
    ("Régulation de puissance", "Comment ne jamais dépasser la puissance disponible ?"),
]
TPS["04"] = [
    ("Lire et câbler", "relever le schéma d'un banc, repérer pression et retour, câbler un circuit simple"),
    ("Transmission hydrostatique", "mesurer la pression de gavage, Δp entre A et B, la vitesse du moteur ; inverser le sens"),
    ("Circuit ouvert à vérin", "chronométrer une course, calculer v et le débit, régler le limiteur, lire l'échauffement"),
    ("Accumulateur", "relever P₁ et P₂ du conjoncteur-disjoncteur, le temps de charge et de décharge"),
    ("Courbe p–Q", "tracer la caractéristique d'une pompe à régulation, repérer le tarage et la puissance limite"),
]
PARTIES["05"] = [
    ("Maintenance journalière", "Quels huit points regarder chaque jour, et avec quels critères ?"),
    ("Maintenance hebdomadaire", "Quels sept points demandent un arrêt et une vraie inspection ?"),
    ("Durée de vie d'une pompe", "De quoi dépend-elle, et de combien chaque facteur la réduit-il ?"),
    ("Diagnostic des pannes", "Comment remonter de l'aspect d'une pièce à la cause du défaut ?"),
    ("Cavitation", "Pourquoi se produit-elle, comment l'entend-on, comment l'éviter ?"),
]
TPS["05"] = [
    ("Ronde quotidienne", "parcourir une machine avec la checklist des huit points et remplir la fiche d'historique"),
    ("Propreté de l'huile", "prélever un échantillon, lire l'indicateur de colmatage et classer le fluide selon ISO 4406"),
    ("Précharge d'un accumulateur", "consigner, décharger puis mesurer la précharge avec le kit de gonflage"),
    ("Rendement d'une pompe", "mesurer Q et p, calculer ηv et le comparer à la valeur neuve"),
    ("Aspiration et cavitation", "lire la dépression à l'aspiration, comparer crépine propre et colmatée"),
]
NOMBRES = {2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 7: "sept", 8: "huit", 9: "neuf", 10: "dix"}

# Mini-projets (hors chapitres), dans cours/hydraulique/Mini_projet/ :
# la liste des sujets (PDF) et un exemple de presentation (PowerPoint).
MINI = "Mini_projet"
SUJETS = "Liste_28_sujets_mini_projets.pdf"
EXEMPLE = "Exemple_presentation_mini_projet_DOOSAN_Solar_225LC-V.pptx"
NB_SUJETS = 28

# Photos de TP (cours/hydraulique/images/) : visages floutes et metadonnees (GPS...) retirees
# avant publication ; les originaux restent chez l'enseignant. Une photo absente du depot est ignoree.
IMG = "images"
BANDEAU = "bandeau.jpg"
GALERIE = [  # (titre, colonnes, [(fichier, legende)]) ; titre vide = suite du bloc precedent
 ("👷 Sur le terrain", 1, [
   ("terrain-promotion-sany.jpg", "Sur le site de TP, devant la pelle SANY : une séance de terrain avec plus de 30 participants."),
 ]),
 ("", 3, [
   ("terrain-pelle-cat.jpg", "Sur la pelle CAT : on monte sur la machine pour repérer ses organes."),
   ("terrain-sur-la-machine.jpg", "Sur le capot de la pelle SANY : on pointe, on identifie, on vérifie."),
   ("terrain-demontage-moteur.jpg", "Autour d'un moteur démonté, en blouse de TP."),
   ("terrain-inspection-sany.jpg", "Au pied de la flèche d'une pelle SANY : observation et discussion en petit groupe."),
   ("terrain-equipe-moteur.jpg", "Une équipe en blouse de TP, devant le moteur démonté."),
   ("terrain-seance-sany.jpg", "Séance sur la pelle SANY : un groupe au pied de la machine, deux participants sur la tourelle."),
 ]),
 ("🚜 Les machines", 3, [
   ("machine-sany-fleche.jpg", "Pelle SANY, flèche déployée : au TP, on commence par repérer vérins, pompes et distributeur."),
   ("machine-sany-sy215c.jpg", "Pelle SANY SY 215C, sujet n° 01 de la liste des mini-projets."),
   ("machine-parc.jpg", "Le parc de machines : plusieurs engins et plusieurs marques à comparer, dont une DOOSAN."),
 ]),
 ("🔩 Les composants", 3, [
   ("composant-pompe-en-place.jpg", "Pompe hydraulique dans son compartiment : bride, orifices et flexibles à repérer."),
   ("composant-compartiment-pompes.jpg", "Compartiment des pompes d'une SANY : pompe, filtre et flexibles réunis dans un même caisson."),
   ("composant-filtre-bol.jpg", "Filtre à bol transparent : le dépôt se voit sans rien démonter."),
   ("composant-pompe-demontee.jpg", "Pompe à pistons axiaux démontée : barillet, pistons à patins, arbre et plaques."),
   ("composant-pompe-double-coupe.jpg", "Pompe double à pistons axiaux en coupe : deux barillets et leurs organes de régulation."),
   ("composant-moteur-reducteur-coupe.jpg", "Ensemble moteur hydraulique et réducteur à engrenages, en coupe."),
 ]),
]

# Recopies des supports : page « Quatre enigmes », page « Synthese du chapitre » et « Memento ».
# Seuls les chapitres publies sont affiches ; a completer avec chaque nouveau chapitre.
ENIGMES = {
 "01": [
   ("Pourquoi un flexible de pelle est-il chaud au toucher alors qu'il ne fait que transporter de l'huile ?",
    "Partie 8 · pertes de charge"),
   ("Pourquoi une pompe « siffle » quand l'huile est froide ou la crépine encrassée ?",
    "Parties 4 et 5 · aspiration, viscosité"),
   ("Comment un vérin de 10 cm de diamètre soulève-t-il l'équivalent de 20 tonnes ?",
    "Partie 3 · pression × surface"),
   ("Pourquoi la pédale de frein devient-elle « spongieuse » quand il y a de l'air dans le circuit ?",
    "Partie 7 · compressibilité"),
 ],
 "02": [
   ("Pourquoi une pompe est-elle un cercle avec un triangle plein… et un moteur le même cercle avec le "
    "triangle à l'envers ?", "Partie 4 · conversion"),
   ("Un distributeur 4/3 : comment savoir, en 30 secondes, où va l'huile dans chaque position ?",
    "Partie 3 · distribution"),
   ("Le limiteur de pression protège le circuit, pourtant il est dessiné « fermé ». Pourquoi ?",
    "Partie 2 · régulation"),
   ("Pourquoi la source est-elle toujours en bas à gauche et les vérins en haut ?",
    "Partie 6 · lire un schéma"),
 ],
 "03": [
   ("Pourquoi une pompe à pistons axiaux exige-t-elle une huile filtrée à 10–20 µm ?", "Parties 3 et 5"),
   ("Pourquoi faut-il décharger un accumulateur avant de le démonter ?", "Partie 4"),
   ("Pourquoi la tige d'un vérin peut-elle se tordre alors que la pression est normale ?", "Partie 7"),
   ("Pourquoi un moteur hydraulique « avale-t-il » de l'air quand on coupe l'alimentation ?", "Partie 6"),
 ],
 "04": [
   ("Pourquoi un circuit fermé exige-t-il une seconde pompe, plus petite, en plus de la pompe principale ?",
    "Partie 2 · circuits fermés"),
   ("Pourquoi une pompe peut-elle tenir 200 bar au repos sans chauffer l'huile ?", "Partie 4 · maintien de pression"),
   ("Comment descendre une charge de 2 tonnes sans qu'elle ne s'emballe ?", "Partie 5 · commande de débit"),
   ("Pourquoi un moteur de 30 kW peut-il entraîner une pompe capable de 73 kW hydrauliques ?",
    "Partie 6 · régulation de puissance"),
 ],
 "05": [
   ("Pourquoi une pompe devient-elle bruyante alors que la pression affichée n'a pas changé ?", "Partie 5 · cavitation"),
   ("Pourquoi réduire la pression de 25 % peut-il multiplier par 2,4 la durée de vie d'une pompe ?",
    "Partie 3 · durée de vie"),
   ("Pourquoi faut-il décharger l'installation avant de toucher à un accumulateur ?", "Partie 2 · maintenance hebdomadaire"),
   ("Pourquoi une huile laiteuse ou noire doit-elle alerter, même si la machine fonctionne ?",
    "Partie 1 · maintenance journalière"),
 ],
}
SYNTHESE = {
 "01": [
   "La pompe crée le débit ; la pression naît de la résistance à l'écoulement.",
   "Vitesse ← débit (v = Q / S) · Force ← pression (F = p · S).",
   "Puissance = pression × débit ; l'énergie perdue devient de la chaleur.",
   "La viscosité dépend de la température : elle gouverne le régime, les pertes et le rendement.",
   "L'huile est quasi incompressible, pas totalement : air, dilatation et pertes de charge se calculent.",
 ],
 "02": [
   "Un symbole représente une fonction, jamais la forme du composant.",
   "Un distributeur se lit case par case : orifices, positions, commande, repos.",
   "Le limiteur de pression protège (fermé), le réducteur règle l'aval (ouvert), le limiteur de débit "
   "règle la vitesse.",
   "Triangle plein : hydraulique, creux : pneumatique ; le sens du triangle distingue pompe et moteur.",
   "On dessine le circuit au repos : source en bas à gauche, actionneurs en haut.",
 ],
 "03": [
   "La propreté de l'huile protège tout : filtre au retour, crépine à l'aspiration, β élevé, code ISO 4406 suivi.",
   "La pompe crée le débit (Cyl · N · ηv) ; le moteur et le vérin le transforment en vitesse, couple et effort.",
   "Tout rendement < 1 : la différence devient chaleur, à évacuer par le réservoir ou un échangeur.",
   "Un accumulateur stocke l'énergie dans l'azote : précharge ≈ 0,9 p₁, décharger avant d'intervenir.",
   "Un vérin se dimensionne deux fois : en pression (alésage) et au flambage (tige).",
 ],
 "04": [
   "Un circuit est une chaîne d'énergie (source, distribution, récepteur) doublée d'une boucle d'information.",
   "Fermé : le retour va à la pompe, il faut du gavage et un petit réservoir. Ouvert : la pompe aspire au "
   "réservoir, c'est la rapidité de manœuvre.",
   "Maintien de pression : l'énergie est en réserve (accumulateur, entre P₁ et P₂) ou la pompe réduit son débit au tarage.",
   "Commande de débit : la vitesse dépend du débit de la pompe ; le limiteur de vitesse retient une charge motrice.",
   "Régulation de puissance : la cylindrée baisse quand la pression monte, pour que p · q reste sous P₀.",
 ],
 "05": [
   "Huit points chaque jour, sept chaque semaine, avec un critère et une trace dans l'historique : sans critère, "
   "pas de décision.",
   "Consigner avant d'intervenir, décharger l'accumulateur, ne jamais chercher une fuite à la main.",
   "La pression est le premier facteur de durée de vie : × 1,5 de pression, ÷ 3,4 de durée ; × 1,33 de vitesse, − 25 %.",
   "Un défaut de pompe a une cause : filtration, cavitation, température, pression ou alignement ; on corrige la "
   "cause, pas seulement la pièce.",
   "La cavitation se joue à l'aspiration : niveau, crépine, tube, viscosité ; son signe est le bruit.",
 ],
}
MEMENTO = {
 "01": [
   ("≈ 870 kg/m³", "masse volumique de l'huile minérale"),
   ("≈ 46 mm²/s", "ISO VG 46, à 40 °C"),
   ("≈ 1 400 MPa", "module de compressibilité de l'huile"),
   ("≈ 0,7 × 10⁻³ /°C", "coefficient de dilatation de l'huile"),
   ("1 bar = 10⁵ Pa", "= 10 N par cm² ; 1 MPa = 10 bar"),
   ("1 L/min", "= 1,667 × 10⁻⁵ m³/s"),
   ("P [kW] = Q·p / 600", "Q en L/min, p en bar"),
   ("≈ 0,06 °C / bar", "échauffement par perte de charge"),
   ("p<sub>asp</sub> ≥ 0,8 bar abs", "limite usuelle à l'aspiration"),
   ("3 à 6 m/s", "vitesse au refoulement"),
   ("Re : 2 000 et 3 000", "seuils laminaire / turbulent"),
   ("1 ch = 736 W", "conversion de puissance"),
 ],
 "03": [
   ("3 à 4 × Q", "volume du réservoir (L)"),
   ("15 à 20 cm", "huile au-dessus de la crépine"),
   ("β = 200", "efficacité 99,5 %"),
   ("ISO 18/16/13", "pompes et moteurs à pistons"),
   ("p₀ ≈ 0,9 p₁", "précharge d'accumulateur"),
   ("p₂/p₀ ≤ 4", "limite pour une vessie"),
   ("70–98 %", "rendement volumétrique d'une pompe"),
   ("52,5–88,2 %", "rendement global d'une pompe"),
   ("0,85–0,95", "rendement d'un vérin"),
   ("K = 1 · 2 · 0,7 · 0,5", "coefficients de flambage"),
   ("Δp ∝ Q²", "perte de charge d'un distributeur"),
   ("≈ 10 bar/°C", "huile enfermée (chapitre 1)"),
 ],
}

# Journal des mises a jour, du plus recent au plus ancien (le premier s'affiche en haut de page).
NOUVEAUTES = [
 ("8 nov. 2026", "chapitres 4 « Circuits hydrauliques » (71 pages, 9 exercices corrigés) et 5 « Maintenance des "
                 "installations » (90 pages, 7 exercices corrigés) en ligne : les cinq chapitres du module sont publiés"),
 ("7 nov. 2026", "5e simulation 3D : les filtres et le rapport β (efficacité, colmatage, by-pass, exercice 2)"),
 ("7 nov. 2026", "simulations 3D : distributeurs, vérins, pompes et accumulateur à manipuler en coupe"),
 ("2 nov. 2026", "chapitre 3 « Technologie des systèmes hydrauliques » en ligne : 115 pages, 9 exercices corrigés, 5 TP"),
 ("2 nov. 2026", "galerie de photos de TP, énigmes de terrain et mémento du technicien"),
 ("1er nov. 2026", "liste des 28 sujets de mini-projets et exemple de présentation"),
 ("27 oct. 2026", "vidéo du chapitre 2"),
 ("26 oct. 2026", "chapitre 2 « Schémas hydrauliques et pneumatiques » en ligne"),
 ("24 oct. 2026", "ouverture de la page, chapitre 1 « Généralités sur les systèmes hydrauliques »"),
]


# Simulations 3D (pages statiques du site, three.js) : (ancre, vignette dans IMG, titre, partie du ch. 3, resume, missions)
SIMUL = "https://janane-allah.github.io/simulations/hydraulique/"
SIMULATIONS = [
 ("jeu-1", "sim3d-distributeurs.jpg", "Les distributeurs", "Partie 8",
  "Le tiroir en coupe relié à un vérin chargé : déplacez-le au levier, le symbole ISO suit.",
  ["2/2, 3/2, 4/2 et les quatre centres du 4/3", "tenir une charge, décharger la pompe", "lire la case active"]),
 ("jeu-2", "sim3d-verins.jpg", "Les vérins", "Partie 7",
  "Simple effet, double effet, double tige, télescopique et rotatif, sous pression et chronométrés.",
  ["nommer les pièces en 3D", "F = η p S, Vs = Q/S, Ve = Q/S'", "l'exercice 7 : pousser 100 kN"]),
 ("jeu-3", "sim3d-pompes.jpg", "Les pompes", "Partie 5",
  "Engrenages, palettes et pistons axiaux en mouvement, sur un banc d'essai.",
  ["le chemin de l'huile", "cylindrée, fuites et ηv", "exercices 4 et 5 : bilan de puissance"]),
 ("jeu-4", "sim3d-accumulateur.jpg", "L'accumulateur", "Partie 4",
  "Vessie, piston ou membrane : précharge d'azote, remplissage, restitution.",
  ["p₀ = 0,9 p₁", "isotherme ou adiabatique (exercice 3)", "les règles de sécurité"]),
 ("jeu-5", "sim3d-filtres.jpg", "Les filtres", "Partie 3",
  "Un filtre en coupe entre deux compteurs de particules : rapport β, colmatage et by-pass.",
  ["β = N amont / N aval, η = 1 − 1/β", "colmatage, indicateur, by-pass", "exercice 2 et les quatre emplacements"]),
]


def simulations():
    """Section 'Simulations 3D' : une carte par banc virtuel, deux par rangee."""
    items = [s for s in SIMULATIONS if fichier_image(s[1])]
    if not items:
        return ""
    bouton = "https://img.shields.io/badge/%s-FFB300?style=for-the-badge" % quote("▶ Manipuler en 3D", safe="")
    t = ["<table>"]
    for k in range(0, len(items), 2):
        t.append("<tr>")
        for ancre, img, titre, partie, resume, points in items[k:k + 2]:
            lien = SIMUL + "#" + ancre
            t.append('<td width="50%%" valign="top" align="center"><a href="%s"><img src="%s/%s/%s" width="100%%" alt="Simulation 3D : %s"></a><br/>'
                     '<b>%s</b> · <sub>chapitre 3, %s</sub><br/><sub>%s</sub><br/><br/><sub>%s</sub><br/><br/><a href="%s"><img src="%s" alt="Manipuler en 3D"></a></td>'
                     % (lien, B, IMG, img, titre, titre, partie.lower(), resume, " · ".join(points), lien, bouton))
        t.append("</tr>")
    t.append("</table>\n")
    nombre = {1: u"Un banc virtuel", 2: u"Deux bancs virtuels", 3: u"Trois bancs virtuels", 4: u"Quatre bancs virtuels",
              5: u"Cinq bancs virtuels", 6: u"Six bancs virtuels"}.get(len(items), u"%d bancs virtuels" % len(items))
    return (u"## 🧊 Simulations 3D\n\n" + nombre + u" pour manipuler les composants du chapitre 3 avant le TP : on fait tourner les pièces "
            u"**en coupe**, on déplace le tiroir, on met les vérins sous pression, on règle les pompes, on gonfle l'accumulateur "
            u"et on compte les particules qu'arrête un filtre. "
            u"Chaque banc propose des missions (jusqu'à 3 étoiles) ; les valeurs affichées viennent des formules du cours.\n\n"
            + "\n".join(t) + u"\n💻📱 Sur ordinateur ou sur téléphone, sans installation ni compte · 🖱 glisser pour tourner, molette pour zoomer · "
            u"🎨 huile en rouge sous pression, en bleu vers le réservoir, en orange emprisonnée sous charge.\n\n---\n\n")


def fichiers(num):
    d = os.path.join(ROOT, B, CH[num][0])
    return sorted(os.listdir(d)) if os.path.isdir(d) else []


def pages(num):
    f = [x for x in fichiers(num) if x.startswith("1_")]
    if not f:
        return None
    try:
        import pypdf
        return len(pypdf.PdfReader(os.path.join(ROOT, B, CH[num][0], f[0])).pages)
    except Exception:
        return None


def liens_chapitre(num):
    """Liens HTML d'un chapitre : cours, TD, TP, corriges, video."""
    out = []
    for f in fichiers(num):
        chemin = "%s/%s/%s" % (B, CH[num][0], f)
        if f.startswith("1_"):
            out.append(("📄 Cours", chemin))
        elif "corrige" in f.lower():
            out.append(("✅ Corrigé", chemin))
        elif f.startswith("3_"):
            out.append(("📝 TD", chemin))
        elif f.startswith("4_"):
            out.append(("🔬 " + f.split("_")[1], chemin))
    if num in VIDEOS:
        out.append(("▶ Vidéo", VIDEOS[num]))
    return " · ".join('<a href="%s">%s</a>' % (u, t) for t, u in out)


publies = [n for n in sorted(CH) if any(f.startswith("1_") for f in fichiers(n))]

desc = []
for n in publies:
    np_ = pages(n)
    desc.append("**%s — %s**%s  \n%s\n" % (n, CH[n][1], " · %d pages" % np_ if np_ else "", CH[n][2]))
    if n in PARTIES:
        k = len(PARTIES[n])
        desc.append("*Les %s parties du chapitre, une question chacune :*\n" % NOMBRES.get(k, k))
        desc += ["%d. **%s** — %s" % (i + 1, t, q) for i, (t, q) in enumerate(PARTIES[n])]
    if n in TPS:
        desc.append("\n*Les TP associés, sur machine :*\n")
        desc += ["- **TP %d — %s** : %s" % (i + 1, t, d) for i, (t, d) in enumerate(TPS[n])]
    if n in SYNTHESE:
        desc.append("\n*À retenir :*\n")
        desc += ["> %d. %s  " % (i + 1, s) for i, s in enumerate(SYNTHESE[n])]
    desc.append("")
descriptif = "\n".join(desc)


def chapitres_absents():
    """', dont les chapitres 4 et 5 ne sont pas encore en ligne' ; vide si tout est publie."""
    ns = [str(int(n)) for n in sorted(CH) if n not in publies]
    if not ns:
        return ""
    if len(ns) == 1:
        return ", dont le chapitre %s n'est pas encore en ligne" % ns[0]
    return ", dont les chapitres %s ne sont pas encore en ligne" % (
        "%s et %s" % tuple(ns) if len(ns) == 2 else "%s à %s" % (ns[0], ns[-1]))


def mini_projet():
    """Section 'Mini-projets' ; vide tant que ni la liste ni l'exemple ne sont dans le depot."""
    import re, zipfile
    liste = os.path.join(ROOT, B, MINI, SUJETS)
    exemple = os.path.join(ROOT, B, MINI, EXEMPLE)
    lignes = []
    if os.path.isfile(liste):
        try:
            import pypdf
            n = len(pypdf.PdfReader(liste).pages)
            detail = "%d pages · " % n
        except Exception:
            detail = ""
        ko = "%d" % round(os.path.getsize(liste) / 1e3)
        lignes.append("| **📋 Les 28 sujets** | [Liste des mini-projets (PDF)](%s/%s/%s) · %s%s Ko |"
                      % (B, MINI, SUJETS, detail, ko))
    if os.path.isfile(exemple):
        diapos = sum(1 for n in zipfile.ZipFile(exemple).namelist() if re.match(r"ppt/slides/slide\d+\.xml$", n))
        mo = ("%.1f" % (os.path.getsize(exemple) / 1e6)).replace(".", ",")
        lignes.append("| **📊 Un exemple** | [Présentation de 15 min : pelle DOOSAN Solar 225LC-V (PowerPoint)](%s/%s/%s)"
                      " · %d diapositives · %s Mo |" % (B, MINI, EXEMPLE, diapos, mo))
    if not lignes:
        return ""
    texte = u"""## 🧩 Mini-projets

Chaque étudiant (ou chaque groupe) étudie **une machine réelle** et décrit son système hydraulique complet : le circuit, le réservoir et sa filtration, les pompes, puis les autres composants. Le travail mobilise les cinq chapitres du cours et les TP.

| | |
|---|---|
%s

""" % "\n".join(lignes)
    if os.path.isfile(liste):
        texte += u"""**Les 28 sujets**, en six familles : terrassement et BTP (7), levage et manutention (6), véhicules utilitaires et poids lourds (5), agriculture (2), industrie (5), énergie, eau et air (3). Les architectures indiquées sont des cas courants, à confirmer sur le schéma constructeur du modèle choisi ; les valeurs chiffrées se relèvent sur la plaque, la fiche technique ou le manuel.

"""
    if os.path.isfile(exemple):
        texte += u"""**Dans l'exemple de présentation** : 18 diapositives minutées (plus une annexe et les crédits hors minutage), sur le plan Introduction · Réservoir · Filtration · Pompes · Autres composants · Circuit · Maintenance · Conclusion. Il montre comment rattacher chaque partie à un chapitre du cours et à une section du manuel de service, recouper des fiches techniques et refaire sur une machine réelle les calculs du cours (volume du réservoir, régulation de puissance, effort d'un vérin, bilan de puissance). C'est un exemple pédagogique : ses valeurs viennent de fiches publiques et sont à remplacer par les relevés de la machine étudiée ; il renvoie aux chapitres 1 à 5 du cours%s.

""" % chapitres_absents()
    return texte + u"---\n\n"


mini = mini_projet()


def fichier_image(nom):
    return os.path.isfile(os.path.join(ROOT, B, IMG, nom))


def bandeau():
    if not fichier_image(BANDEAU):
        return ""
    return (u'<img src="%s/%s/%s" alt="Pelle SANY, pompe hydraulique en place, pompe double en coupe et pompe démontée" '
            u'width="100%%" />\n\n' % (B, IMG, BANDEAU))


def parcours():
    """Schema Mermaid du module : chapitres en ligne, chapitres a venir, mini-projets."""
    court = {"01": "Généralités", "02": "Schémas", "03": "Technologie", "04": "Circuits", "05": "Maintenance"}
    noeuds = ['    C%s["%s<br/>%s"]' % (n, n, court.get(n, CH[n][1])) for n in sorted(CH)]
    noeuds.append('    MP["🧩<br/>Mini-projets"]')
    chaine = " --> ".join(["C%s" % n for n in sorted(CH)] + ["MP"])
    en_ligne = ",".join("C%s" % n for n in sorted(CH) if n in publies)
    a_venir = ",".join("C%s" % n for n in sorted(CH) if n not in publies)
    lignes = ["flowchart LR"] + noeuds + ["    " + chaine,
              "    classDef ok fill:#2E86AB,stroke:#1d5d7a,color:#fff",
              "    classDef soon fill:#eeeeee,stroke:#aaaaaa,color:#555555,stroke-dasharray: 4 3",
              "    classDef goal fill:#8E44AD,stroke:#6c3483,color:#fff"]
    if en_ligne:
        lignes.append("    class %s ok" % en_ligne)
    if a_venir:
        lignes.append("    class %s soon" % a_venir)
    lignes.append("    class MP goal")
    return "```mermaid\n%s\n```\n\n🟦 chapitre en ligne · ⬜ à venir · 🟪 mini-projets\n\n" % "\n".join(lignes)


def badges_stats():
    """Badges chiffres : pages de cours en ligne, mini-projets, TP."""
    out = []
    total = sum(p or 0 for p in (pages(n) for n in publies))
    if total:
        out.append("![Cours](https://img.shields.io/badge/Cours_en_ligne-%d_pages-1F6FEB?style=for-the-badge)" % total)
    if os.path.isfile(os.path.join(ROOT, B, MINI, SUJETS)):
        out.append("![Mini-projets](https://img.shields.io/badge/Mini--projets-%d_sujets-8E44AD?style=for-the-badge)" % NB_SUJETS)
    out.append("![TP](https://img.shields.io/badge/TP-sur_machines_r%C3%A9elles-C0392B?style=for-the-badge)")
    if any(fichier_image(x[1]) for x in SIMULATIONS):
        out.append("[![Simulations 3D](https://img.shields.io/badge/Simulations_3D-%d_bancs_virtuels-FFB300?style=for-the-badge)](%s)" % (len(SIMULATIONS), SIMUL))
    return "\n".join(out) + "\n"


def galerie():
    """Section 'Le module en images' : grilles de photos avec legendes."""
    import html
    blocs = []
    for titre, cols, items in GALERIE:
        items = [i for i in items if fichier_image(i[0])]
        if not items:
            continue
        t = (["### %s\n" % titre] if titre else []) + ["<table>"]
        for k in range(0, len(items), cols):
            t.append("<tr>")
            for f, legende in items[k:k + cols]:
                t.append('<td width="%d%%" valign="top"><img src="%s/%s/%s" alt="%s" width="100%%"><br>'
                         '<sub>%s</sub></td>' % (100 // cols, B, IMG, f, html.escape(legende, quote=True), legende))
            t.append("</tr>")
        t.append("</table>\n")
        blocs.append("\n".join(t))
    if not blocs:
        return ""
    return (u"## 📸 Le module en images\n\nLe module se vit sur machines réelles : lire la machine, mesurer, démonter, "
            u"vérifier. *Visages floutés pour respecter l'image des étudiants.*\n\n" + "\n".join(blocs) + u"\n---\n\n")


def enregistrer_jpeg(im, nom):
    os.makedirs(os.path.join(ROOT, B, IMG), exist_ok=True)
    im.convert("RGB").save(os.path.join(ROOT, B, IMG, nom), "JPEG", quality=82, optimize=True, progressive=True)


def rendre_page1(pdf, nom, ratio=None):
    """Page 1 d'un PDF en JPEG de 800 px (pymupdf) ; ratio : recadrage par le haut. None si impossible."""
    try:
        import pymupdf
        from PIL import Image
    except Exception:
        return None
    pg = pymupdf.open(pdf)[0]
    z = 800.0 / pg.rect.width
    pix = pg.get_pixmap(matrix=pymupdf.Matrix(z, z))
    im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    if ratio:
        im = im.crop((0, 0, im.width, min(im.height, int(im.width / ratio))))
    enregistrer_jpeg(im, nom)
    return nom


def couverture(num):
    """Couverture d'un chapitre (page 1 du cours). Generee une seule fois : supprimer l'image pour la refaire."""
    nom = "couverture-chapitre-%s.jpg" % num
    if fichier_image(nom):
        return nom
    f = [x for x in fichiers(num) if x.startswith("1_")]
    return rendre_page1(os.path.join(ROOT, B, CH[num][0], f[0]), nom) if f else None


def couverture_mini():
    nom = "couverture-mini-projets.jpg"
    if fichier_image(nom):
        return nom
    p = os.path.join(ROOT, B, MINI, SUJETS)
    return rendre_page1(p, nom, ratio=16 / 9.0) if os.path.isfile(p) else None


def couverture_a_venir():
    """Vignette commune des chapitres pas encore en ligne, aux couleurs des supports."""
    nom = "couverture-a-venir.jpg"
    if fichier_image(nom):
        return nom
    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception:
        return None
    im = Image.new("RGB", (800, 450))
    d = ImageDraw.Draw(im)
    for y in range(450):
        t = y / 449.0
        d.line([(0, y), (800, y)], fill=(int(14 + 16 * t), int(35 + 22 * t), int(66 + 30 * t)))

    def police(noms, taille):
        for n in noms:
            try:
                return ImageFont.truetype(n, taille)
            except Exception:
                pass
        return ImageFont.load_default()
    d.text((400, 205), u"À VENIR", anchor="mm", fill=(242, 169, 0), font=police(["georgiab.ttf", "arialbd.ttf"], 72))
    d.text((400, 275), u"Chapitre publié prochainement", anchor="mm", fill=(220, 228, 240),
           font=police(["arial.ttf"], 28))
    enregistrer_jpeg(im, nom)
    return nom


def cartes():
    """Cartes des supports : couverture cliquable, titre, chiffres, liens ; puis la carte des mini-projets."""
    cells = []
    for n in sorted(CH):
        titre = "<b>%s · %s</b>" % (n, CH[n][1])
        if n in publies:
            pdf = "%s/%s/%s" % (B, CH[n][0], [x for x in fichiers(n) if x.startswith("1_")][0])
            img = couverture(n)
            infos = [x for x in ("%d pages" % pages(n) if pages(n) else "",
                                 "%d parties" % len(PARTIES[n]) if n in PARTIES else "",
                                 "%d TP" % len(TPS[n]) if n in TPS else "") if x]
            vignette = ('<a href="%s"><img src="%s/%s/%s" width="100%%" alt="Couverture du chapitre %s"></a><br>'
                        % (pdf, B, IMG, img, n)) if img else ""
            cells.append('%s%s<br><sub>%s</sub><br>%s' % (vignette, titre, " · ".join(infos), liens_chapitre(n)))
        else:
            img = couverture_a_venir()
            vignette = ('<img src="%s/%s/%s" width="100%%" alt="Chapitre à venir"><br>' % (B, IMG, img)) if img else ""
            cells.append('%s%s<br><sub>🚧 À venir</sub>' % (vignette, titre))
    if os.path.isfile(os.path.join(ROOT, B, MINI, SUJETS)):
        img = couverture_mini()
        liste = "%s/%s/%s" % (B, MINI, SUJETS)
        vignette = ('<a href="%s"><img src="%s/%s/%s" width="100%%" alt="Liste des mini-projets"></a><br>'
                    % (liste, B, IMG, img)) if img else ""
        liens = ['<a href="%s">📋 Les %d sujets</a>' % (liste, NB_SUJETS)]
        if os.path.isfile(os.path.join(ROOT, B, MINI, EXEMPLE)):
            liens.append('<a href="%s/%s/%s">📊 Un exemple</a>' % (B, MINI, EXEMPLE))
        cells.append('%s<b>🧩 Mini-projets</b><br><sub>une machine réelle à analyser</sub><br>%s'
                     % (vignette, " · ".join(liens)))
    rows = ["<tr>%s</tr>" % "".join('<td width="33%%" valign="top" align="center">%s</td>' % c for c in cells[k:k + 3])
            for k in range(0, len(cells), 3)]
    return "<table>\n%s\n</table>\n\n" % "\n".join(rows)


def enigmes():
    lignes = ["| **%s** | %s | %s |" % (n, q, r) for n in publies for q, r in ENIGMES.get(n, [])]
    if not lignes:
        return ""
    return (u"## 🧠 Énigmes de terrain\n\nChaque chapitre s'ouvre sur quatre questions d'atelier. Cherchez la réponse, "
            u"puis vérifiez-la dans la partie indiquée du chapitre.\n\n"
            u"| Ch. | L'énigme | La réponse est dans… |\n|:-:|---|---|\n" + "\n".join(lignes) + u"\n\n---\n\n")


def memento():
    blocs = []
    for n in publies:
        if n not in MEMENTO:
            continue
        cells = ['<td align="center" width="25%%"><b>%s</b><br><sub>%s</sub></td>' % (v, d) for v, d in MEMENTO[n]]
        rows = ["<tr>%s</tr>" % "".join(cells[k:k + 4]) for k in range(0, len(cells), 4)]
        blocs.append("### Chapitre %s · %s\n\n<table>\n%s\n</table>\n" % (n, CH[n][1], "\n".join(rows)))
    if not blocs:
        return ""
    return (u"## 📌 Mémento du technicien\n\nLes valeurs à connaître par cœur, telles que les donnent les fiches "
            u"de synthèse des chapitres.\n\n" + "\n".join(blocs) + u"\n---\n\n")


def nouveaute():
    return (u"🆕 **Nouveau · %s** — %s.\n\n" % NOUVEAUTES[0]) if NOUVEAUTES else ""


def historique():
    if not NOUVEAUTES:
        return ""
    return (u"## 🗓️ Mises à jour\n\n<details>\n<summary><i>Historique de la page</i></summary>\n<br/>\n\n"
            + "\n".join("- **%s** — %s" % e for e in NOUVEAUTES) + u"\n\n</details>\n\n---\n\n")


TPL = u"""<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=3500&pause=1000&color=2E86AB&center=true&vCenter=true&width=780&lines=Syst%C3%A8mes+Hydrauliques;Licence+Professionnelle+IMPI+%E2%80%94+ENSAM+Casablanca;Module+6+%3A+Hydraulique+%C2%B7+5+chapitres" alt="Systemes Hydrauliques" />

%(bandeau)s**Pr. Mohamed JANANE ALLAH**, PhD<br/>
École Nationale Supérieure d'Arts et Métiers (ENSAM) — Casablanca

🎓 **Public :** Licence Professionnelle Universitaire *Ingénierie Mécanique et Productique Industrielle* (IMPI)

<br/>

![Formation](https://img.shields.io/badge/Licence_Pro-IMPI-2E86AB?style=for-the-badge)
![Module](https://img.shields.io/badge/Module_6-Hydraulique-4C9A2A?style=for-the-badge)
![Chapitres](https://img.shields.io/badge/Chapitres_en_ligne-%(publies)s_%%2F_5-E67E22?style=for-the-badge)
%(stats)s
%(nouveaute)s[**Plan du module**](#-plan-du-module) · %(nav_simul)s%(nav_enigmes)s%(nav_memento)s%(nav_mini)s%(nav_images)s[**Prérequis et évaluation**](#-prérequis-et-évaluation) · [**Contact**](#-contact)

[![Retour au profil](https://img.shields.io/badge/⬅_Retour_au_profil-555555?style=flat-square)](../README.md)

</div>

---

## 🎯 Compétences visées par le module

À l'issue des cinq chapitres, vous saurez :

1. ✅ **comprendre les bases de l'hydraulique** ;
2. ✅ **connaître les composants** d'un circuit ;
3. ✅ **concevoir un circuit** de base ;
4. ✅ **découvrir la technologie** des systèmes hydrauliques ;
5. ✅ **assurer la maintenance** des installations.

---

%(enigmes)s## 📚 Plan du module

%(parcours)s%(cartes)s> 📘 Cliquez sur une couverture pour ouvrir le chapitre ; %(etat_plan)s.

<details>
<summary><i>Descriptif des chapitres publiés : parties, TP et points à retenir</i></summary>
<br/>

%(descriptif)s
</details>

---

%(simul)s%(memento)s%(mini)s%(galerie)s## 🧭 Prérequis et évaluation

| | |
|---|---|
| **Prérequis** | Mécanique générale (forces, travail, puissance) et mathématiques de base — aucun acquis en hydraulique n'est supposé. |
| **Niveau** | Débutant → intermédiaire. |
| **Chaque chapitre** | Quatre énigmes d'accroche → feuille de route → cours et exercices corrigés → synthèse et pièges à éviter → QCM d'auto-évaluation → checklist « Prêt pour le TP ? ». |
| **Évaluation** | QCM d'auto-évaluation en fin de chapitre, TD corrigés, manipulations en TP. |
| **TP** | Sur banc d'essai ou sur machine : le repère **TP** en haut à droite des diapos signale la notion que vous manipulerez. |

---

%(historique)s## 📫 Contact

<div align="center">

[![Email](https://img.shields.io/badge/mohamedjanane147@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mohamedjanane147@gmail.com)
[![Site](https://img.shields.io/badge/janane--allah.github.io-0A66C2?style=flat-square&logo=github-pages&logoColor=white)](https://janane-allah.github.io)

%(maj)s
</div>
"""

page = TPL.replace("%%", "%").replace("%(cartes)s", cartes()).replace("%(descriptif)s", descriptif) \
          .replace("%(enigmes)s", enigmes()).replace("%(memento)s", memento()) \
          .replace("%(nav_enigmes)s", "[**Énigmes**](#-énigmes-de-terrain) · " if enigmes() else "") \
          .replace("%(nav_memento)s", "[**Mémento**](#-mémento-du-technicien) · " if memento() else "") \
          .replace("%(nouveaute)s", nouveaute()).replace("%(historique)s", historique()) \
          .replace("%(maj)s", "<sub>Page générée par <code>tools/build_hydraulique.py</code> · dernière mise à jour : %s</sub>\n"
                   % NOUVEAUTES[0][0] if NOUVEAUTES else "") \
          .replace("%(publies)s", str(len(publies))).replace("%(mini)s", mini) \
          .replace("%(etat_plan)s", u"les cinq chapitres du module sont en ligne" if len(publies) == len(CH)
                   else u"les chapitres sont publiés au fur et à mesure") \
          .replace("%(nav_mini)s", "[**Mini-projets**](#-mini-projets) · " if mini else "") \
          .replace("%(parcours)s", parcours()).replace("%(stats)s", badges_stats()) \
          .replace("%(bandeau)s", bandeau()) \
          .replace("%(nav_images)s", "[**En images**](#-le-module-en-images) · " if galerie() else "") \
          .replace("%(galerie)s", galerie()).replace("%(simul)s", simulations()) \
          .replace("%(nav_simul)s", "[**🧊 Simulations 3D**](#-simulations-3d) · " if simulations() else "")
io.open(os.path.join(ROOT, PAGE), "w", encoding="utf-8", newline="\n").write(page)
print("OK - %s : %d lignes, %d/%d chapitre(s) publie(s)" % (PAGE, page.count("\n"), len(publies), len(CH)))
