# -*- coding: utf-8 -*-
import io, os, re
from urllib.parse import quote

# Regenere cours/licence-genie-mecanique.md a partir des PDF presents
# dans cours/methodes-numeriques/.  Usage :  python tools/build_page.py
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cours")
B = "methodes-numeriques"

CH = {
 "00": ("Chapitre_00_Introduction_generale", "Introduction générale", 8,
        "Pourquoi le calcul numérique en mécanique, et à quoi il sert concrètement dans le métier d'ingénieur. Présentation des exemples fils conducteurs du module."),
 "01": ("Chapitre_01_Rappels_numeriques", "Rappels numériques : erreurs, normes et conditionnement", 13,
        "Un ordinateur ne calcule jamais exactement : erreurs d'arrondi, normes vectorielles et matricielles, conditionnement d'une matrice."),
 "02": ("Chapitre_02_Systemes_lineaires_directs", "Systèmes linéaires : méthodes directes", 16,
        "Résolution de Ax = b en un nombre fini d'opérations — la brique de base de tout calcul par éléments finis."),
 "03": ("Chapitre_03_Systemes_lineaires_iteratifs", "Systèmes linéaires : méthodes itératives", 12,
        "Pour les grands systèmes creux issus d'un maillage fin, là où l'élimination de Gauss coûte trop cher et détruit le caractère creux (fill-in)."),
 "04": ("Chapitre_04_Systemes_non_lineaires", "Systèmes non linéaires", 18,
        "Résoudre F(x) = 0 quand la physique cesse d'être linéaire : pertes de charge quadratiques, ressort durcissant, grandes déformations."),
 "05": ("Chapitre_05_Generalites_EDP", "Généralités sur les EDP en mécanique et classification", 10,
        "L'inconnue n'est plus un vecteur mais un champ. Classification elliptique / parabolique / hyperbolique et conditions aux limites associées."),
 "06": ("Chapitre_06_Principe_differences_finies", "Principe de la méthode des différences finies", 10,
        "L'étape décisive : remplacer les dérivées, objets continus, par des quantités calculables sur ordinateur."),
 "07": ("Chapitre_07_Consistance_stabilite_convergence", "Consistance, stabilité, convergence", 10,
        "Pourquoi un schéma parfaitement construit sur le papier peut produire des résultats absurdes — des oscillations qui grandissent jusqu'à faire déborder les calculs."),
 "08": ("Chapitre_08_Equation_chaleur", "Équation de la chaleur", 11,
        "Un problème physique résolu de bout en bout : la paroi de four en régime transitoire, de l'état initial jusqu'à l'équilibre."),
 "09": ("Chapitre_09_Laplace_Poisson_advection", "Équation de Laplace-Poisson et advection-diffusion", 11,
        "Discrétisation 2D complète (Dirichlet puis Neumann), validation sur un cas test analytique, puis introduction de l'advection-diffusion."),
 "10": ("Chapitre_10_Equation_ondes", "Équation des ondes", 11,
        "La corde vibrante et sa condition de stabilité — la condition CFL, avec son interprétation géométrique remarquable."),
 "11": ("Chapitre_11_EDO_Euler_Runge_Kutta", "Résolution numérique des équations différentielles ordinaires", 14,
        "L'évolution temporelle des systèmes à nombre fini de degrés de liberté : oscillateurs, mécanismes, circuits équivalents."),
}

# Liens video par chapitre (YouTube, Google Drive...). Chapitre absent = 🚧 a venir.
VIDEOS = {
 "00": "https://drive.google.com/file/d/18AdF62vRubU5swh_zy52d6AvmlzcVybn/view",
 "01": "https://drive.google.com/file/d/13uDHLzPXsp9XpujDGj60SXAgyNtyW84X/view",
 "02": "https://drive.google.com/file/d/19rK9Xc4acZQ77KQnYxwGSc7pkNBj1MKc/view",
 "03": "https://drive.google.com/file/d/19Q7Vj94XDHRTuFz_X4l-3xFFBQQcJwZI/view",
 "04": "https://drive.google.com/file/d/125--JQ7p31u2xEMZVsSO3x2MCeXNOXYA/view",
 "05": "https://drive.google.com/file/d/1wxEG6bzlLQPGz-evjzRmrmuqnVQsqqgs/view",
 "06": "https://drive.google.com/file/d/1F-IuYtpVuRNhaj7w13zxnSUldtZj1PoB/view",
 "07": "https://drive.google.com/file/d/1AT_64YZW3ebVt21abcGkxcZUoLHFnnkg/view",
 "08": "https://drive.google.com/file/d/18wNa17e4CPXprrvWbSh1HTMUlAU2F5dD/view",
 "09": "https://drive.google.com/file/d/1YinQ_oHGrndBm2nsGVBWTBDI62pUBbBE/view",
 "10": "https://drive.google.com/file/d/1IQh3d69BFptw47AmVj_zgeMaxRPnpFTB/view",
 "11": "https://drive.google.com/file/d/1OZqZkwXP--N1ZcmgipRbnzRsleo4AnD8/view",
}

# Videos d atelier TP (ex. 7b_Video_TP1_atelier_MATLAB), affichees a cote de
# la video de cours du meme chapitre. Cle = numero du chapitre, valeur =
# (numero du TP, url[, description]) ou, si le chapitre a plusieurs TP filmes,
# une liste de ces tuples ; description par defaut : atelier MATLAB.
VIDEOS_TP = {
 "02": ("TP1", "https://drive.google.com/file/d/1kmhqkhzH1HCGq9E5eakniAzW5kthOiE-/view"),
 "03": ("TP2", "https://drive.google.com/file/d/1dw82htm3bDXOKr3v-Jziv230Bs23vpe0/view"),
 "04": ("TP3", "https://drive.google.com/file/d/1b4vdrutxz_yeuuil7ytYzb3D7f6wrNUL/view",
        "programmation de Newton"),
 "09": ("TP5", "https://drive.google.com/file/d/1qhSEHFj44XbFneGbJCBylgvrMxVg7l5O/view",
        "correction"),
 "11": [("TP4", "https://drive.google.com/file/d/1GeBDuM-bsHzrqXIGovBEPhuHptdbIkzp/view",
         "programmation complète"),
        ("TP6", "https://drive.google.com/file/d/1FFd2tp73XQvZY2wPG-ukHws2T4iTNNlx/view",
         "programmation complète")],
}


# Video d accroche, hors chapitres : montre a quoi sert le calcul numerique.
MOTIVATION = "https://drive.google.com/file/d/1dc97-wJZVYQ1Gan3rmW4U6hYal3hQO9W/view"

# Polycopie complet (cours, TD et TP du module en un seul PDF), publie le 23 nov. 2026. Version publique :
# le detail des heures (p. 13-14 : cours/TD/TP par filiere et par partie) y est masque a la demande de
# l'enseignant ; seuls restent 60 h / 48 h. L'original (Chapitres/Polycopie_MN.pdf) reste chez lui.
POLY = "Polycopie/Polycopie_Methodes_Numeriques.pdf"


def poly_pages():
    chemin = os.path.join(ROOT, B, POLY)
    if not os.path.isfile(chemin):
        return 0
    try:
        import pypdf
        return len(pypdf.PdfReader(chemin).pages)
    except Exception:
        return 0

# Jeux interactifs des TP : pages HTML sur le site janane-allah.github.io (le Markdown de
# GitHub n'execute pas de JavaScript). Cle = chapitre ; valeur = liste de (TP, adresse,
# sous-titre, [(ancre, titre, notion)]). Vignettes : methodes-numeriques/images/jeux-<tp>/<ancre>.jpg
JEUX = {
 "02": [("TP1", "https://janane-allah.github.io/jeux/tp1/", "le banc d'amortisseurs (méthodes directes)", [
   ("jeu-1", "Le banc d'essai", "Assembler C, bâti mobile, matrice singulière"),
   ("jeu-2", "Gauss pas à pas", "Pivot partiel, multiplicateurs, remontée"),
   ("jeu-3", "Le compteur d'opérations", "n³/3 pour Gauss, n² par second membre"),
   ("jeu-4", "Les messages d'erreur", "Huit vrais messages de MATLAB"),
   ("jeu-5", "Détective du code", "Les bugs silencieux et le résidu"),
  ])],
 "03": [("TP2", "https://janane-allah.github.io/jeux/tp2/", "la paroi du four (méthodes itératives)", [
   ("jeu-1", "Jacobi contre Gauss-Seidel", "La course, une seule ligne d'écart, ρ_GS = ρ_J²"),
   ("jeu-2", "La paroi s'affine", "Le nombre d'itérations quand n augmente"),
   ("jeu-3", "La chasse au ω*", "SOR, formule de Young, courbe asymétrique"),
   ("jeu-4", "Incrément ou erreur ?", "Le critère d'arrêt et le facteur ρ/(1 − ρ)"),
   ("jeu-5", "Détective du code", "Reconnaître un bug à sa sortie console"),
  ])],
 "04": [("TP3", "https://janane-allah.github.io/jeux/tp3/", "le système de pompage (Newton)", [
   ("jeu-1", "Newton dans le plan des débits", "Convergence quadratique, deux racines, bassins"),
   ("jeu-2", "Newton contre le gradient", "5 itérations contre 295 923"),
   ("jeu-3", "Trois conduites", "Système 3 × 3, débits en 1/√R"),
   ("jeu-4", "La jacobienne à la main", "Dériver, vérifier par différences finies"),
   ("jeu-5", "Détective du code", "Signe, départ singulier, paramètre capturé"),
  ])],
 "09": [("TP5", "https://janane-allah.github.io/jeux/tp5/", "la salle de sport (Poisson 2D)", [
   ("jeu-1", "Numéro, s'il vous plaît !", "La numérotation k = (j − 1)·nx + i"),
   ("jeu-2", "Le pochoir à 5 points", "Assembler une ligne de A et de b"),
   ("jeu-3", "Thermostat de la salle", "T = A \\ b, principe du maximum, mur isolé"),
   ("jeu-4", "Course SOR", "Battre Gauss-Seidel, trouver le ω optimal"),
   ("jeu-5", "Détective du code", "Reconnaître un bug à sa sortie console"),
 ])],
 "11": [("TP4", "https://janane-allah.github.io/jeux/tp4/", "la paroi de four (EDO non linéaire)", [
   ("jeu-1", "Le pas de trop", "Euler explicite : précision, pas critique, implicite"),
   ("jeu-2", "Newton, pas à pas", "La boucle de Newton d'Euler implicite"),
   ("jeu-3", "Le duel des schémas", "Ordre de convergence et coût égal"),
   ("jeu-4", "Convection contre rayonnement", "Deux flux, un seul en T⁴"),
   ("jeu-5", "Détective du code", "Reconnaître un bug à sa sortie console"),
  ]),
  ("TP6", "https://janane-allah.github.io/jeux/tp6/", "l'attracteur de Lorenz (système d'EDO)", [
   ("jeu-1", "Le papillon de Lorenz", "RK4 pour un système, centres, rôle de ρ"),
   ("jeu-2", "L'effet papillon", "Sensibilité aux conditions initiales"),
   ("jeu-3", "Crash test : Euler contre RK4", "Pas de temps, explosion, coût égal"),
   ("jeu-4", "Instabilité, chaos ou erreur ?", "Classer huit courbes calculées"),
   ("jeu-5", "Détective du code", "Reconnaître un bug à sa sortie console"),
  ])],
}



PARTS = [
 ("🚩", "Introduction", ["00"], ""),
 ("🧮", "Partie I — Systèmes algébriques", ["01", "02", "03", "04"],
  "Résoudre *Ax = b*, puis *F(x) = 0* : les briques sur lesquelles repose tout le reste du module."),
 ("🌡️", "Partie II — EDP et différences finies", ["05", "06", "07", "08", "09", "10"],
  "De la classification des EDP aux trois équations modèles de la mécanique : chaleur, Laplace-Poisson, ondes."),
 ("📈", "Partie III — Équations différentielles ordinaires", ["11"],
  "Retour au temps : Euler, Runge-Kutta et la question de la stabilité du pas de temps."),
]


def fichiers(num):
    return sorted(os.listdir(os.path.join(ROOT, B, CH[num][0])))


def videos_tp(num):
    tp = VIDEOS_TP.get(num)
    if tp and isinstance(tp[0], str):
        tp = [tp]
    return tp or []


# Couleurs des boutons, par type de support
COULEURS = {"cours": "0056D2", "td": "6A4C93", "tp": "C1121F", "corrige": "2E7D32", "video": "E67E22",
            "jeu": "FFB300"}


def ressources(num):
    """Supports d'un module, dans l'ordre de travail : cours, TD, TP, corriges, videos.
    Chaque element : (type, libelle du bouton, message du bouton, lien)."""
    d, out = CH[num][0], []
    chemin = lambda f: "%s/%s/%s" % (B, d, f)
    fs = fichiers(num)
    out += [("cours", "📄 Cours", "%d pages" % CH[num][2], chemin(f)) for f in fs if f.startswith("1_")]
    out += [("td", "📝 TD", "énoncé", chemin(f)) for f in fs if f.startswith("3_") and "corrige" not in f.lower()]
    out += [("tp", "🔬 " + f.split("_")[1], "énoncé", chemin(f))
            for f in fs if f.startswith("4_") and "corrige" not in f.lower()]
    out += [("corrige", "✅ " + f.split("_")[1], "corrigé MATLAB" if f.lower().endswith(".zip") else "corrigé",
             chemin(f)) for f in fs if "corrige" in f.lower()]
    if num in VIDEOS:
        out.append(("video", "▶ Vidéo", "cours", VIDEOS[num]))
    out += [("video", "▶ Vidéo", t[0], t[1]) for t in videos_tp(num)]
    out += [("jeu", "🎮 Jeux", "%s · %d jeux" % (j[0], len(j[3])), j[1]) for j in JEUX.get(num, [])]
    return out


def bouton(typ, libelle, message, url):
    from urllib.parse import quote
    q = lambda t: quote(t.replace("-", "--").replace("_", "__"), safe="")
    image = "https://img.shields.io/badge/%s-%s-%s?style=for-the-badge" % (q(libelle), q(message), COULEURS[typ])
    return "[![%s %s](%s)](%s)" % (libelle, message, image, url)


# Supports propres au Cycle GE : le cours reste celui de la GM, seuls les TD et TP changent (contexte
# energetique). Fichiers dans le sous-dossier GE/ de chaque chapitre, meme convention (3_ TD, 4_ TP,
# « corrige » = corrige). Mise a jour du 25 nov. 2026 : jusqu'au chapitre 2 (TD01, TD02, TP1).
GE = "GE"
MAJ_GE = u"25 nov. 2026"   # date de la derniere mise a jour des supports GE
# Videos GE sur Drive : cle = chapitre, valeur = liste de (TP, url[, description]).
# TP1 GE (25 nov. 2026) : publiee a la demande explicite de l'enseignant alors qu'elle etait ouverte a toute
# personne ayant le lien et telechargeable (non conforme a la regle UH2C) ; partage a corriger dans Drive.
VIDEOS_GE = {
 "02": [("TP1", "https://drive.google.com/file/d/1QIeu_jGI170irAdK-mF8Z9z8fKToSlZc/view", "correction")],
}


def fichiers_ge(num):
    d = os.path.join(ROOT, B, CH[num][0], GE)
    return sorted(os.listdir(d)) if os.path.isdir(d) else []


def ressources_ge(num):
    """Supports GE d'un module : TD, TP, corriges, videos (meme format que ressources)."""
    d, out = CH[num][0], []
    chemin = lambda f: "%s/%s/%s/%s" % (B, d, GE, f)
    fs = fichiers_ge(num)
    out += [("td", "⚡ TD GE", "énoncé", chemin(f)) for f in fs if f.startswith("3_") and "corrige" not in f.lower()]
    out += [("tp", "⚡ %s GE" % f.split("_")[1], "énoncé", chemin(f))
            for f in fs if f.startswith("4_") and "corrige" not in f.lower()]
    out += [("corrige", "✅ %s GE" % f.split("_")[1], "corrigé MATLAB" if f.lower().endswith(".zip") else "corrigé",
             chemin(f)) for f in fs if "corrige" in f.lower()]
    out += [("video", "▶ Vidéo GE", t[0] + (" · " + t[2] if len(t) > 2 else ""), t[1]) for t in VIDEOS_GE.get(num, [])]
    return out


CHAPITRES_GE = [n for n in sorted(CH) if ressources_ge(n)]


# Page du Cycle GE (meme cours, TD/TP/jeux GE) : cours/methodes-numeriques-ge.md, generee plus bas.
PAGE_GE = "methodes-numeriques-ge.md"


def module(num):
    """Un module en clair : titre, description, puis un bouton par support (rien a deplier) ;
    quand le module a des TD/TP propres au GE, un renvoi vers la page du Cycle GE."""
    lignes = ["#### Module %s · %s" % (num, CH[num][1]), "", CH[num][3], "",
              "\n".join(bouton(*r) for r in ressources(num)), ""]
    if ressources_ge(num):
        lignes += [u"<sub>⚡ <b>Cycle GE</b> : les TD et TP de ce module existent en version énergétique sur la "
                   u"[page du Cycle GE](%s).</sub>" % PAGE_GE, ""]
    return "\n".join(lignes)


def section_jeux(jeux=None, suffixe=""):
    """Une carte par jeu (vignette, titre, notion, bouton), trois par rangee, puis une carte « Comment jouer ».
    jeux : dictionnaire au format de JEUX (JEUX par defaut) ; suffixe : ajoute au dossier des vignettes (ex. « -ge »)."""
    from urllib.parse import quote
    jeux = JEUX if jeux is None else jeux
    out = []
    for num, (tp, url, sous_titre, liste) in sorted(((n, j) for n in jeux for j in jeux[n]), key=lambda x: x[1][0]):
        dossier = "%s/images/jeux-%s%s" % (B, tp.lower(), suffixe)
        out.append("### %s%s · Module %s — %s\n" % (tp, " GE" if suffixe else "", num, sous_titre))
        cartes = []
        for q, (ancre, titre, notion) in enumerate(liste):
            lien = "%s#%s" % (url, ancre)
            badge = "https://img.shields.io/badge/%s-%s?style=for-the-badge" % (quote("▶ Jouer", safe=""), COULEURS["jeu"])
            cartes.append('<td width="33%%" valign="top" align="center"><a href="%s"><img src="%s/%s.jpg" width="100%%" '
                          'alt="Jeu %d : %s"></a><br/><b>%d · %s</b><br/><sub>%s</sub><br/><a href="%s"><img src="%s" '
                          'alt="Jouer"></a></td>' % (lien, dossier, ancre, q + 1, titre, q + 1, titre, notion, lien, badge))
        cartes.append('<td width="33%" valign="top">🏆 <b>Comment jouer</b><br/><br/>'
                      '💻📱 Sur ordinateur ou sur téléphone, sans installation ni compte.<br/><br/>'
                      '⭐ Jusqu\'à 3 étoiles par jeu ; la progression reste dans votre navigateur.<br/><br/>'
                      '💡 Jouez <b>après</b> avoir lu l\'énoncé et <b>avant</b> d\'écrire votre code MATLAB.</td>')
        out.append("<table>")
        out += ["<tr>\n%s\n</tr>" % "\n".join(cartes[k:k + 3]) for k in range(0, len(cartes), 3)]
        out.append("</table>\n")
    return "\n".join(out)


programme = []
for icon, title, nums, blurb in PARTS:
    n_pages = sum(CH[n][2] for n in nums)
    programme.append("### %s %s\n" % (icon, title))
    programme.append("<sub>%d module%s · %d pages de cours</sub>\n" % (len(nums), "s" if len(nums) > 1 else "", n_pages))
    if blurb:
        programme.append("%s\n" % blurb)
    programme += [module(n) for n in nums]

tree = "\n".join("├── %s/" % CH[n][0] for n in sorted(CH))
if os.path.isfile(os.path.join(ROOT, B, POLY)):
    tree += "\n├── %s/   (polycopié complet)" % POLY.split("/")[0]

# Chiffres cles (bandeau sous l'en-tete), calcules sur les fichiers presents
NB_PAGES = sum(c[2] for c in CH.values())
NB_TD = sum(1 for n in CH for f in fichiers(n) if f.startswith("3_") and "corrige" not in f.lower())
NB_TP = sum(1 for n in CH for f in fichiers(n) if f.startswith("4_") and "corrige" not in f.lower())
NB_CORRIGES = sum(1 for n in CH for f in fichiers(n) if "corrige" in f.lower())
NB_VIDEOS = len(VIDEOS) + sum(len(videos_tp(n)) for n in CH)   # page LST GM (les videos GE sont sur la page GE)

# Ce que vous apprendrez, competences (etiquettes), questions frequentes
APPRENDRE = [
 "Choisir une méthode adaptée à la taille et à la structure du problème",
 "Estimer la précision d'un résultat et reconnaître un calcul qui diverge",
 "Programmer ces méthodes en **MATLAB** et valider un schéma sur un cas test analytique",
 "Interpréter physiquement les conditions de stabilité (CFL, critères de convergence)",
]
COMPETENCES = ["MATLAB", "Erreurs et conditionnement", "Élimination de Gauss", "Jacobi · Gauss-Seidel · SOR",
               "Méthode de Newton", "Différences finies", "Stabilité de von Neumann", "Condition CFL",
               "Crank-Nicolson", "Schéma décentré (upwind)", "Euler et Runge-Kutta"]


# Deux parcours, GM et GE. Sources : chapitre 0 (tableau 1, plan du module de 60 h) pour la LST GM ;
# document de travail « Programme_GE_48h.pdf » (nov. 2026) pour le Cycle d'Ingenieur GE.
# L'evaluation et les mini-projets du GE, encore a valider, ne sont pas publies.
# Le detail des heures (cours, TD, TP, par partie et par module) n'est plus publie, pour les deux parcours,
# a la demande de l'enseignant (13 nov. 2026) : seuls les totaux 60 h / 48 h restent sur la page.
PROGRAMME_GE = [  # (module, applications en energetique)
 ("00", "Quatre cas chiffrés : pompage, solaire, four, réseau."),
 ("01", "Bilans d'énergie et rendements : soustraction de grandeurs voisines, arrondi, conditionnement d'un bilan thermique."),
 ("02", "Réseau thermique nodal d'un bâtiment multizone ; réseau hydraulique maillé."),
 ("03", "Conduction 2D dans un four ou une plaque : grands systèmes creux (Jacobi, Gauss-Seidel, SOR)."),
 ("04", "Colebrook (pertes de charge), bilan radiatif en T⁴, point de fonctionnement pompe-réseau : Newton."),
 ("05", "Chaleur, convection-diffusion, Poisson, ondes : un phénomène énergétique pour chaque type d'EDP."),
 ("06", "Paroi de four (fil rouge), ailette : de l'équation au système A T = b."),
 ("07", "Seuil r ≤ 1/2 sur la paroi réfractaire ; CFL pour le transport de chaleur par un fluide."),
 ("08", "Paroi, ailette, stockage thermique ; schémas explicite, implicite, θ."),
 ("09", "Champ de température d'un bâtiment (2D) ; échangeur et nombre de Péclet."),
 ("10", "Vibrations de tuyauteries et d'aubes ; acoustique d'un conduit."),
 ("11", "Dynamique thermique d'un four ou d'un ballon de stockage ; raideur et choix du pas."),
]
TP_PARCOURS = [  # (TP, methode, LST GM, Cycle GE)
 ("TP1", "Méthode directe : Gauss avec pivotage, Gauss-Jordan", "le banc d'amortisseurs",
  "réseau thermique d'un bâtiment à trois zones ⚡ en ligne"),
 ("TP2", "Méthodes itératives", "la paroi d'un four", "identique"),
 ("TP3", "Newton", "le système de pompage", "identique (pompage et Colebrook)"),
 ("TP4", "EDO non linéaire : Euler et Runge-Kutta", "le refroidissement d'une paroi de four", "identique"),
 ("TP5", "Poisson 2D", "la salle de sport", "champ de température d'une salle ou d'un bâtiment, conditions aux limites mixtes"),
 ("TP6", "Système d'EDO", "les attracteurs de Lorenz", "— (pas de TP6)"),
]


# Intitule du module dans chaque filiere (demande de l'enseignant, 16 nov. 2026).
INTITULE_GM = u"Méthodes numériques pour la mécanique"
INTITULE_GE = u"Introduction aux méthodes numériques"


def deux_parcours():
    """Section « Deux parcours : GM et GE » : intitules, TP compares, applications du GE module par module."""
    out = [u"## 🎓 Deux parcours : GM et GE\n",
           u"Le module est suivi par deux publics de la FSTM, chacun avec son intitulé :\n",
           u"| | 🔧 LST Génie Mécanique | ⚡ Cycle d'Ingénieur GE, 1ʳᵉ année |", u"|---|---|---|",
           u"| **Intitulé du module** | **%s** | **%s** |" % (INTITULE_GM, INTITULE_GE),
           u"| **Volume** | 60 h | 48 h |",
           u"| **TP** | six : TP1 à TP6 | cinq : TP1 à TP5 |", u"",
           u"**Le contenu scientifique est le même** : les douze modules, les démonstrations, les méthodes et les "
           u"critères de validation. En Cycle GE, les exemples sont tirés de l'énergétique.\n"]
    if CHAPITRES_GE:
        out += [u"> ⚡ **Étudiants du Cycle GE : votre page est [ici](%s).** Même cours et mêmes vidéos de cours ; "
                u"TD, TP et jeux en contexte énergétique, **jusqu'au chapitre %d** pour l'instant (mise à jour du %s).\n"
                % (PAGE_GE, int(CHAPITRES_GE[-1]), MAJ_GE),
                u'<div align="center">\n\n[![Page du Cycle GE](https://img.shields.io/badge/%s-%s-E67E22?style=for-the-badge)](%s)\n\n</div>\n'
                % (quote(u"⚡ Page du Cycle GE", safe=""), quote(INTITULE_GE, safe=""), PAGE_GE)]
    out += [u"#### Les TP de chaque parcours\n",
            u"| TP | Méthode | 🔧 LST GM | ⚡ Cycle GE |", u"|:-:|---|---|---|"]
    out += [u"| **%s** | %s | %s | %s |" % t for t in TP_PARCOURS]
    tp_ge = sorted(set(f.split("_")[1] for n in CHAPITRES_GE for f in fichiers_ge(n) if f.startswith("4_")))
    out += [u"", u"<sub>Les énoncés de TP sont communs aux deux parcours, sauf ceux qui ont leur version GE (⚡)%s ; "
            u"les autres versions énergétiques suivront.</sub>"
            % ((u" : " + u", ".join(tp_ge)) if tp_ge else u"")]
    out += [u"", u"<details>", u"<summary><b>⚡ Le Cycle GE, module par module : les applications en énergétique</b></summary>",
            u"<br/>\n", u"| Module | Applications en énergétique |", u"|---|---|"]
    out += [u"| **%s** · %s | %s |" % (n, CH[n][1], a) for n, a in PROGRAMME_GE]
    out += [u"", u"Le cours est commun ; les TD et TP GE déjà en ligne sont sur la [page du Cycle GE](%s).\n" % PAGE_GE, u"</details>\n"]
    return u"\n".join(out) + u"\n---\n\n"


def etiquette(texte):
    from urllib.parse import quote
    t = quote(texte.replace("-", "--").replace("_", "__"), safe="")
    return "![%s](https://img.shields.io/badge/%s-E8EEF7?style=flat-square)" % (texte, t)


apprendre = "<table>\n%s\n</table>" % "\n".join(
    "<tr>%s</tr>" % "".join('<td width="50%%" valign="top">✔️ %s</td>' % a.replace("**", "") for a in APPRENDRE[k:k + 2])
    for k in range(0, len(APPRENDRE), 2))

TPL = u"""[⬅ Profil](../README.md) › Enseignement › **Méthodes numériques**

<div align="center">

<img src="methodes-numeriques/images/banniere-gm-ge.jpg" alt="Méthodes numériques — LST Génie Mécanique : %(intitule_gm)s ; 1re année du Cycle d'Ingénieur Génie Énergétique : %(intitule_ge)s — FSTM, Université Hassan II de Casablanca — Pr. Mohamed JANANE ALLAH" width="100%%" />

<br/>

Résoudre sur ordinateur les problèmes que la mécanique ne sait pas résoudre à la main :<br/>
**systèmes linéaires et non linéaires**, **équations aux dérivées partielles** par différences finies,
**équations différentielles ordinaires**.

[![Commencer](https://img.shields.io/badge/▶_Commencer_le_cours-Chapitre_0-0056D2?style=for-the-badge)](%(ch0)s)
%(poly_bouton)s[![Vidéo d'accroche](https://img.shields.io/badge/🎬_Pourquoi_ce_module_%%3F-Vidéo_d'accroche-C1121F?style=for-the-badge)](%(motiv)s)

<sub>🎓 Conçu pour les étudiants de la FSTM — Université Hassan II de Casablanca · 🔒 vidéos accessibles avec le compte universitaire UH2C</sub>

<table>
<tr>
<td align="center" width="20%%"><b>📚 %(nb_ch)s modules</b><br><sub>%(nb_pages)s pages de cours</sub></td>
<td align="center" width="20%%"><b>🎥 %(nb_videos)s vidéos</b><br><sub>cours et ateliers TP</sub></td>
<td align="center" width="20%%"><b>🔬 %(nb_tp)s TP MATLAB</b><br><sub>%(nb_corriges)s corrigés en scripts</sub></td>
<td align="center" width="20%%"><b>📝 %(nb_exam)s sujets d'examen</b><br><sub>archive en accès libre</sub></td>
<td align="center" width="20%%"><b>⏱️ 60 h · 48 h</b><br><sub>LST GM · Cycle GE · %(nb_td)s TD</sub></td>
</tr>
</table>

[**À propos**](#-à-propos) · [**GM / GE**](#-deux-parcours--gm-et-ge) · [**Programme**](#-programme-du-module) · [**Examens**](#-examens) · [**Enseignant**](#-enseignant) · [**Questions fréquentes**](#-questions-fréquentes) · [**🎮 Jeux**](#-jeux-interactifs)

</div>

---

## 📌 À propos

Ce module donne les outils numériques qui permettent de résoudre, sur ordinateur, les problèmes
que la mécanique ne sait pas résoudre à la main : **systèmes linéaires** (méthodes directes et
itératives), **systèmes non linéaires**, **équations aux dérivées partielles** par différences
finies, et **équations différentielles ordinaires**.

#### Ce que vous apprendrez

%(apprendre)s

#### Compétences que vous allez acquérir

%(competences)s

#### Détails à connaître

| 🎓 Public | ⏱️ Volume | 🧩 Prérequis | 💻 Logiciel | 🗣️ Langue |
|---|---|---|---|---|
| LST Génie Mécanique (*%(intitule_gm)s*) · 1ʳᵉ année du Cycle d'Ingénieur Génie Énergétique (*%(intitule_ge)s*), FSTM | 60 h en LST GM · 48 h en Cycle GE ([détail](#-deux-parcours--gm-et-ge)) | Algèbre linéaire, analyse (développements de Taylor), bases de MATLAB | MATLAB | Français |

---

%(parcours)s## 📚 Programme du module

%(poly_texte)sIl y a **%(nb_ch)s modules** dans ce cours, en trois parties précédées d'une introduction. Chaque module
donne accès directement à ses supports : un clic sur un bouton ouvre le document ou la vidéo.

<sub>🔵 cours (PDF) · 🟣 TD · 🔴 énoncé de TP · 🟢 corrigé (scripts MATLAB) · 🟠 vidéo (compte UH2C) · 🟡 jeux interactifs</sub>

%(programme)s
---

## 📝 Examens

Sujets des sessions précédentes, en accès libre, pour s'entraîner dans les conditions de
l'épreuve (durée : 2 h). Les sujets **A** et **B** posent les mêmes questions avec des
données numériques différentes.

%(examens)s
> 💡 **Conseil :** traitez un sujet en temps limité avant de relire le cours, puis comparez avec
> vos TD. Les examens de préparation sont de **niveau difficile** : un bon test avant l'épreuve.

---

## 👤 Enseignant

<table>
<tr>
<td width="130" align="center" valign="top"><img src="methodes-numeriques/images/enseignant.png" width="96" alt="Monogramme de l'enseignant" /></td>
<td valign="top">
<b>Pr. Mohamed JANANE ALLAH</b>, PhD — Maître de Conférence<br/>
Faculté des Sciences et Techniques de Mohammedia (FSTM) — Université Hassan II de Casablanca<br/><br/>
🔬 Recherche : modélisation numérique des structures — plaques à gradient fonctionnel (FGM), méthodes hybrides éléments finis – sans maillage, réseaux de neurones.<br/>
📚 Autre cours : <a href="licence-pro-hydraulique.md">Systèmes hydrauliques</a> — Licence Professionnelle IMPI, ENSAM Casablanca.<br/>
🌐 <a href="https://janane-allah.github.io">Site personnel</a> · <a href="https://janane-allah.github.io/publications/">Publications</a> · <a href="mailto:mohamedjanane147@gmail.com">mohamedjanane147@gmail.com</a>
</td>
</tr>
</table>

🏛️ **Proposé par** la Faculté des Sciences et Techniques de Mohammedia — Université Hassan II de Casablanca · 📍 BP 146, Mohammedia 28806, Maroc

---

## ❓ Questions fréquentes

<details>
<summary><b>À qui s'adresse ce module ?</b></summary>
<br/>

Le module est **mutualisé**, à la FSTM — UH2C, entre la **LST Génie Mécanique** et la **1ʳᵉ année du Cycle
d'Ingénieur Génie Énergétique (GE)** : les outils numériques sont exactement les mêmes de part et d'autre.
Il s'intitule *%(intitule_gm)s* en LST GM et *%(intitule_ge)s* en Cycle GE.
Changent aussi les applications, le volume horaire et les TP : 60 h et six TP en LST GM, 48 h et cinq TP en Cycle GE
([détail des deux parcours](#-deux-parcours--gm-et-ge)).

</details>

<details>
<summary><b>Comment accéder aux vidéos ?</b></summary>
<br/>

🔒 Les vidéos sont **réservées aux étudiants de l'Université Hassan II de Casablanca**. Connectez-vous à votre
**compte universitaire** avant d'ouvrir un lien vidéo : depuis un compte personnel, Google affichera une
demande d'autorisation. Si l'accès vous est refusé alors que vous êtes bien inscrit au module, écrivez-moi.

Commencez par la **[vidéo d'accroche](%(motiv)s)** : où le calcul numérique intervient réellement dans le
métier d'ingénieur mécanicien.

</details>

<details>
<summary><b>Quels supports puis-je télécharger ?</b></summary>
<br/>

Tous les PDF — %(poly_faq)scours, TD, énoncés de TP, sujets d'examen — et les **corrigés de TP** (scripts MATLAB, en zip)
sont en accès libre sur cette page. Les vidéos se regardent en ligne, avec le compte universitaire.

</details>

<details>
<summary><b>Comment travailler un chapitre ?</b></summary>
<br/>

| Étape | Support | Objectif |
|:-:|---|---|
| 1️⃣ | 📄 **Cours** | Lire le chapitre avant la séance — les notions s'enchaînent, chaque chapitre s'appuie sur le précédent. |
| 2️⃣ | 📝 **TD** | Faire les exercices à la main : c'est là que les méthodes se comprennent vraiment. |
| 3️⃣ | 🔬 **TP** | Programmer la méthode en MATLAB et la confronter à un cas test dont on connaît la solution. |

</details>

<details>
<summary><b>Comment préparer l'examen ?</b></summary>
<br/>

Traitez un sujet de l'[archive](#-examens) en temps limité (2 h) avant de relire le cours, puis comparez avec
vos TD. Les examens de préparation sont de niveau difficile : un bon test avant l'épreuve.

</details>

<details>
<summary><b>Comment les fichiers sont-ils organisés ?</b></summary>
<br/>

```
cours/methodes-numeriques/
%(tree)s
└── Examens/
```

Dans chaque dossier : `1_Cours_chapitre_XX.pdf`, `3_TDXX_enonce.pdf`, `4_TPX_enonce.pdf`,
et, quand il existe, `4_TPX_corrige_...` (corrigé librement téléchargeable). Le sous-dossier `GE/` d'un chapitre
contient les TD et TP du Cycle GE (même convention, avec `GE` dans le nom).
Sujets d'examen dans `Examens/` : `examen_<partie1|partie2|mixte>_AAAA_AAAA_sujetX.pdf`,
`examen_preparation_N_AAAA_AAAA.pdf`.

</details>

---

## 🎮 Jeux interactifs

Des jeux, dans le navigateur, pour **manipuler un TP avant de le programmer** : chaque jeu correspond à une
manipulation de l'énoncé. Tous les nombres affichés sont calculés en direct par le code MATLAB du TP, porté
ligne pour ligne en JavaScript : ce sont les mêmes que dans MATLAB.

%(jeux)s
---

<div align="center">

[![Email](https://img.shields.io/badge/mohamedjanane147@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mohamedjanane147@gmail.com)
[![Site](https://img.shields.io/badge/janane--allah.github.io-0A66C2?style=flat-square&logo=github-pages&logoColor=white)](https://janane-allah.github.io)
[![Retour au profil](https://img.shields.io/badge/⬅_Retour_au_profil-555555?style=flat-square)](../README.md)

<sub>Page générée par <code>tools/build_page.py</code> · Université Hassan II de Casablanca — FSTM</sub>

</div>
"""

# Examens (archive) : tous les PDF de cours/methodes-numeriques/Examens/,
# sous-dossiers compris, regroupes par annee universitaire (la plus recente
# d'abord). Type d'epreuve, numero de preparation et sujet A/B sont lus dans
# le nom du fichier ; un nom non reconnu est quand meme publie, sous son nom.
EXAMENS = "Examens"
TYPES_EXAMEN = [  # (motif dans le nom, epreuve, programme)
    ("partie1", u"Examen — Partie I", u"Systèmes d'équations linéaires et non linéaires"),
    ("partie2", u"Examen — Partie II", u"Méthodes des différences finies"),
    ("mixte", u"Examen — Parties I et II", u"Systèmes d'équations et méthodes des différences finies"),
    ("preparation", u"Examen de préparation n°%s", u"Parties I et II — niveau difficile"),
]


def examens():
    racine = os.path.join(ROOT, B, EXAMENS)
    annees, total = {}, 0
    for dossier, _, noms in os.walk(racine):
        for nom in sorted(noms):
            if not nom.lower().endswith(".pdf"):
                continue
            total += 1
            rel = os.path.relpath(os.path.join(dossier, nom), ROOT).replace(os.sep, "/")
            m = re.search(r"(\d{4})_(\d{4})", nom)
            annee = "%s/%s" % m.groups() if m else u"Autres"
            typ = next((i for i, t in enumerate(TYPES_EXAMEN) if t[0] in nom.lower()), None)
            if typ is None:
                cle, epreuve, prog = (99, nom), nom, u""
            else:
                _, epreuve, prog = TYPES_EXAMEN[typ]
                if "%s" in epreuve:
                    num = re.search(r"preparation_(\d+)", nom.lower())
                    epreuve = epreuve % (num.group(1) if num else "")
                cle = (typ, epreuve)
            sujet = re.search(r"sujet([A-Z])", nom)
            ligne = annees.setdefault(annee, {}).setdefault(
                cle, {"epreuve": epreuve, "prog": prog, "sujets": []})
            ligne["sujets"].append((sujet.group(1) if sujet else u"", rel))
    if not total:
        return u"*Aucun sujet archivé pour l'instant.*\n", 0
    ordre = sorted((a for a in annees if a != u"Autres"), reverse=True)
    ordre += [u"Autres"] if u"Autres" in annees else []
    out = []
    for annee in ordre:
        out.append(u"### 🗂️ Année universitaire %s\n" % annee)
        out.append(u"| Épreuve | Programme | 📄 Sujets |")
        out.append(u"|---|---|:-:|")
        for cle in sorted(annees[annee]):
            l = annees[annee][cle]
            liens = u" · ".join(u"[Sujet %s](%s)" % (s_, r) if s_ else u"[PDF](%s)" % r
                                for s_, r in sorted(l["sujets"]))
            out.append(u"| **%s** | %s | %s |" % (l["epreuve"], l["prog"], liens))
        out.append(u"")
    return u"\n".join(out), total


texte_examens, nb_examens = examens()
ch0 = "%s/%s/%s" % (B, CH["00"][0], next(f for f in fichiers("00") if f.startswith("1_")))
NB_POLY = poly_pages()
if NB_POLY:
    from urllib.parse import quote as _q
    _lien_poly = "%s/%s" % (B, POLY)
    poly_bouton = ("[![Polycopié complet](https://img.shields.io/badge/%s-%s-2E7D32?style=for-the-badge)](%s)\n"
                   % (_q(u"📘 Polycopié complet", safe=""), _q(u"%d pages · PDF" % NB_POLY, safe=""), _lien_poly))
    poly_texte = (u"> 📘 **Tout le module en un seul PDF** : [le polycopié](%s) (%d pages) réunit l'introduction, les onze "
                  u"chapitres, les 11 TD et les 6 TP MATLAB, dans l'ordre où l'on travaille (chaque chapitre suivi de son TD "
                  u"et de ses TP). Il sert aux deux parcours, LST GM et Cycle GE.\n\n" % (_lien_poly, NB_POLY))
    poly_faq = u"[polycopié complet](%s), " % _lien_poly
else:
    poly_bouton = poly_texte = poly_faq = ""
valeurs = {
    "programme": "\n".join(programme), "tree": tree,
    "motiv": MOTIVATION, "ch0": ch0, "examens": texte_examens, "nb_exam": str(nb_examens),
    "nb_ch": str(len(CH)), "nb_pages": str(NB_PAGES), "nb_td": str(NB_TD), "nb_tp": str(NB_TP),
    "nb_corriges": str(NB_CORRIGES), "nb_videos": str(NB_VIDEOS),
    "apprendre": apprendre, "competences": "\n".join(etiquette(c) for c in COMPETENCES),
    "jeux": section_jeux(), "parcours": deux_parcours(),
    "poly_bouton": poly_bouton, "poly_texte": poly_texte, "poly_faq": poly_faq,
    "intitule_gm": INTITULE_GM, "intitule_ge": INTITULE_GE,
}
page = TPL.replace("%%", "%")
for k, v in valeurs.items():
    page = page.replace("%%(%s)s" % k, v)
assert "%(" not in page, "champ non remplace"
io.open(os.path.join(ROOT, "licence-genie-mecanique.md"), "w", encoding="utf-8", newline="\n").write(page)
print("OK - %d lignes" % page.count("\n"))


# ============================================================================================================
# Page du Cycle d'Ingenieur GE (cours/methodes-numeriques-ge.md), demandee le 25 nov. 2026 : « GE seulement ».
# Meme cours et memes videos de cours que la LST GM ; TD, TP, corriges, videos de TP et jeux propres au GE,
# jusqu'au dernier chapitre de CHAPITRES_GE. Au-dela : « TD et TP GE a venir » (pas de supports GM).
# ============================================================================================================
JEUX_GE = {
 "02": [("TP1", "https://janane-allah.github.io/jeux/tp1-ge/", "le réseau thermique d'un bâtiment (méthodes directes)", [
   ("jeu-1", "Le réseau thermique", "Assembler G, local voisin chauffé, zone isolée"),
   ("jeu-2", "Gauss pas à pas", "Pivot partiel, multiplicateurs, remontée"),
   ("jeu-3", "Le compteur d'opérations", "n³/3 pour Gauss, n² par scénario de chauffage"),
   ("jeu-4", "Les messages d'erreur", "Huit vrais messages de MATLAB"),
   ("jeu-5", "Détective du code", "Les bugs silencieux et le résidu"),
  ])],
}
APPLI_GE = dict(PROGRAMME_GE)
DERNIER_GE = CHAPITRES_GE[-1] if CHAPITRES_GE else None


def module_ge(num):
    """Module de la page GE : cours et video de cours communs, puis TD/TP/corriges/videos/jeux GE ou « a venir »."""
    res = [r for r in ressources(num) if r[0] == "cours"]
    if num in VIDEOS:
        res.append(("video", "▶ Vidéo", "cours", VIDEOS[num]))
    ge = ressources_ge(num) + [("jeu", "🎮 Jeux", "%s GE · %d jeux" % (j[0], len(j[3])), j[1]) for j in JEUX_GE.get(num, [])]
    lignes = ["#### Module %s · %s" % (num, CH[num][1]), "", CH[num][3], ""]
    if APPLI_GE.get(num):
        lignes += [u"<sub>⚡ En énergétique : %s</sub>" % APPLI_GE[num], ""]
    lignes += ["\n".join(bouton(*r) for r in res + ge), ""]
    if num != "00" and not ge:
        lignes += [u"<sub>⏳ TD et TP en version GE : à venir.</sub>", ""]
    return "\n".join(lignes)


programme_ge = []
for icon, title, nums, blurb in PARTS:
    programme_ge.append("### %s %s\n" % (icon, title))
    programme_ge.append("<sub>%d module%s · %d pages de cours</sub>\n" % (len(nums), "s" if len(nums) > 1 else "", sum(CH[n][2] for n in nums)))
    programme_ge += [module_ge(n) for n in nums]

NB_TD_GE = sum(1 for n in CH for f in fichiers_ge(n) if f.startswith("3_") and "corrige" not in f.lower())
NB_TP_GE = sum(1 for n in CH for f in fichiers_ge(n) if f.startswith("4_") and "corrige" not in f.lower())
NB_VIDEOS_GE = len(VIDEOS) + sum(len(v) for v in VIDEOS_GE.values())
NB_JEUX_GE = sum(len(j[3]) for n in JEUX_GE for j in JEUX_GE[n])
poly_bouton_ge = (u"[![Polycopié du cours](https://img.shields.io/badge/%s-%s-2E7D32?style=for-the-badge)](%s/%s)\n"
                  % (quote(u"📘 Polycopié du cours", safe=""), quote(u"%d pages · PDF" % NB_POLY, safe=""), B, POLY)) if NB_POLY else ""

TPL_GE = u"""[⬅ Profil](../README.md) › Enseignement › **%(intitule_ge)s** · Cycle d'Ingénieur GE

<div align="center">

<img src="methodes-numeriques/images/banniere-ge.jpg" alt="%(intitule_ge)s — 1re année du Cycle d'Ingénieur Génie Énergétique — FSTM, Université Hassan II de Casablanca — Pr. Mohamed JANANE ALLAH" width="100%%" />

<br/>

Résoudre sur ordinateur les problèmes de l'énergétique qu'on ne sait pas résoudre à la main :<br/>
**systèmes linéaires et non linéaires** (réseaux thermiques et hydrauliques), **équations aux dérivées partielles**
par différences finies (conduction, convection), **équations différentielles ordinaires** (dynamique thermique).

[![Commencer](https://img.shields.io/badge/▶_Commencer_le_cours-Chapitre_0-0056D2?style=for-the-badge)](%(ch0)s)
%(poly_bouton)s
<sub>🎓 1ʳᵉ année du Cycle d'Ingénieur Génie Énergétique (GE) — FSTM, Université Hassan II de Casablanca · 🔒 vidéos accessibles avec le compte universitaire UH2C</sub>

<table>
<tr>
<td align="center" width="20%%"><b>📚 %(nb_ch)s modules</b><br><sub>%(nb_pages)s pages de cours</sub></td>
<td align="center" width="20%%"><b>🎥 %(nb_videos)s vidéos</b><br><sub>cours et TP GE</sub></td>
<td align="center" width="20%%"><b>⚡ %(nb_td)s TD · %(nb_tp)s TP GE</b><br><sub>jusqu'au chapitre %(dernier)s</sub></td>
<td align="center" width="20%%"><b>🎮 %(nb_jeux)s jeux</b><br><sub>TP1 GE</sub></td>
<td align="center" width="20%%"><b>⏱️ 48 h</b><br><sub>5 TP MATLAB</sub></td>
</tr>
</table>

[**À propos**](#-à-propos) · [**Programme**](#-programme-du-module) · [**🎮 Jeux**](#-jeux-interactifs) · [**Enseignant**](#-enseignant) · [**Questions fréquentes**](#-questions-fréquentes)

</div>

---

## 📌 À propos

Ce module donne à l'ingénieur énergéticien les outils numériques qui permettent de résoudre, sur ordinateur, ce
qu'on ne sait pas résoudre à la main : **systèmes linéaires** (méthodes directes et itératives), **systèmes non
linéaires**, **équations aux dérivées partielles** par différences finies, et **équations différentielles ordinaires**.

> ⚡ **Ce qui est propre au Cycle GE** : le cours (PDF et vidéos) est le même que celui de la LST Génie Mécanique ;
> les **TD**, les **TP** et les **jeux** sont écrits dans un contexte énergétique (bâtiments, fours, réseaux de chaleur).
> Mise à jour du %(maj)s : **jusqu'au chapitre %(dernier)s** ; les modules suivants recevront leurs TD et TP GE au fur et à mesure.

#### Ce que vous apprendrez

%(apprendre)s

#### Détails à connaître

| 🎓 Public | ⏱️ Volume | 🧩 Prérequis | 💻 Logiciel | 🗣️ Langue |
|---|---|---|---|---|
| 1ʳᵉ année du Cycle d'Ingénieur Génie Énergétique (GE), FSTM | 48 h · 5 TP (TP1 à TP5) | Algèbre linéaire, analyse (développements de Taylor), bases de MATLAB | MATLAB | Français |

---

## 📚 Programme du module

Il y a **%(nb_ch)s modules**, en trois parties précédées d'une introduction. Pour chaque module : le cours et sa vidéo
(communs), puis, quand ils sont en ligne, le TD, le TP, son corrigé, sa vidéo et ses jeux en version GE (⚡).

<sub>🔵 cours (PDF) · 🟣 TD GE · 🔴 énoncé de TP GE · 🟢 corrigé (scripts MATLAB) · 🟠 vidéo (compte UH2C) · 🟡 jeux interactifs</sub>

%(programme)s
---

## 🎮 Jeux interactifs

Des jeux, dans le navigateur, pour **manipuler un TP avant de le programmer**. Tous les nombres affichés sont calculés
en direct par le code MATLAB du TP, porté ligne pour ligne en JavaScript : ce sont les mêmes que dans MATLAB.

%(jeux)s
---

## 👤 Enseignant

<b>Pr. Mohamed JANANE ALLAH</b>, PhD — Maître de Conférence · Faculté des Sciences et Techniques de Mohammedia (FSTM) — Université Hassan II de Casablanca<br/>
🌐 <a href="https://janane-allah.github.io">Site personnel</a> · <a href="mailto:mohamedjanane147@gmail.com">mohamedjanane147@gmail.com</a>

---

## ❓ Questions fréquentes

<details>
<summary><b>Pourquoi le cours est-il le même qu'en LST Génie Mécanique ?</b></summary>
<br/>

Le module est mutualisé : les méthodes numériques sont les mêmes de part et d'autre. En Cycle GE, le module
s'intitule *%(intitule_ge)s* (48 h, cinq TP) ; ses TD, ses TP et ses jeux sont propres au GE. La page de la
LST Génie Mécanique reste [ici](licence-genie-mecanique.md).

</details>

<details>
<summary><b>Comment accéder aux vidéos ?</b></summary>
<br/>

🔒 Connectez-vous à votre **compte universitaire UH2C** avant d'ouvrir un lien vidéo. Si l'accès vous est refusé alors
que vous êtes bien inscrit au module, écrivez-moi.

</details>

<details>
<summary><b>Quels supports puis-je télécharger ?</b></summary>
<br/>

Les PDF du cours, les énoncés des TD et TP GE et les corrigés de TP (scripts MATLAB, en zip) sont en accès libre.
Le polycopié réunit tout le cours ; ses TD et TP sont ceux de la LST GM : en GE, utilisez les énoncés ⚡ de cette page.

</details>

---

<div align="center">

[![Email](https://img.shields.io/badge/mohamedjanane147@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mohamedjanane147@gmail.com)
[![Site](https://img.shields.io/badge/janane--allah.github.io-0A66C2?style=flat-square&logo=github-pages&logoColor=white)](https://janane-allah.github.io)
[![Retour au profil](https://img.shields.io/badge/⬅_Retour_au_profil-555555?style=flat-square)](../README.md)

<sub>Page générée par <code>tools/build_page.py</code> · Université Hassan II de Casablanca — FSTM</sub>

</div>
"""

valeurs_ge = {
    "intitule_ge": INTITULE_GE, "ch0": ch0, "poly_bouton": poly_bouton_ge, "nb_ch": str(len(CH)), "nb_pages": str(NB_PAGES),
    "nb_videos": str(NB_VIDEOS_GE), "nb_td": str(NB_TD_GE), "nb_tp": str(NB_TP_GE), "nb_jeux": str(NB_JEUX_GE),
    "dernier": str(int(DERNIER_GE)) if DERNIER_GE else "0", "maj": MAJ_GE, "apprendre": apprendre,
    "programme": "\n".join(programme_ge), "jeux": section_jeux(JEUX_GE, "-ge"),
}
page_ge = TPL_GE.replace("%%", "%")
for k, v in valeurs_ge.items():
    page_ge = page_ge.replace("%%(%s)s" % k, v)
assert "%(" not in page_ge, "champ non remplace (page GE)"
io.open(os.path.join(ROOT, PAGE_GE), "w", encoding="utf-8", newline="\n").write(page_ge)
print("OK - %s : %d lignes" % (PAGE_GE, page_ge.count("\n")))
