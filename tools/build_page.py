# -*- coding: utf-8 -*-
import io, os, re

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


def module(num):
    """Un module en clair : titre, description, puis un bouton par support (rien a deplier)."""
    return "\n".join(["#### Module %s · %s" % (num, CH[num][1]), "", CH[num][3], "",
                      "\n".join(bouton(*r) for r in ressources(num)), ""])


def section_jeux():
    """Une carte par jeu (vignette, titre, notion, bouton), trois par rangee, puis une carte « Comment jouer »."""
    from urllib.parse import quote
    out = []
    for num, (tp, url, sous_titre, liste) in sorted(((n, j) for n in JEUX for j in JEUX[n]), key=lambda x: x[1][0]):
        dossier = "%s/images/jeux-%s" % (B, tp.lower())
        out.append("### %s · Module %s — %s\n" % (tp, num, sous_titre))
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

# Chiffres cles (bandeau sous l'en-tete), calcules sur les fichiers presents
NB_PAGES = sum(c[2] for c in CH.values())
NB_TD = sum(1 for n in CH for f in fichiers(n) if f.startswith("3_") and "corrige" not in f.lower())
NB_TP = sum(1 for n in CH for f in fichiers(n) if f.startswith("4_") and "corrige" not in f.lower())
NB_CORRIGES = sum(1 for n in CH for f in fichiers(n) if "corrige" in f.lower())
NB_VIDEOS = len(VIDEOS) + sum(len(videos_tp(n)) for n in CH)

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


def etiquette(texte):
    from urllib.parse import quote
    t = quote(texte.replace("-", "--").replace("_", "__"), safe="")
    return "![%s](https://img.shields.io/badge/%s-E8EEF7?style=flat-square)" % (texte, t)


apprendre = "<table>\n%s\n</table>" % "\n".join(
    "<tr>%s</tr>" % "".join('<td width="50%%" valign="top">✔️ %s</td>' % a.replace("**", "") for a in APPRENDRE[k:k + 2])
    for k in range(0, len(APPRENDRE), 2))

TPL = u"""[⬅ Profil](../README.md) › Enseignement › **Méthodes numériques pour la mécanique**

<div align="center">

<img src="methodes-numeriques/images/banniere.jpg" alt="Méthodes numériques pour la mécanique — FSTM, Université Hassan II de Casablanca — Pr. Mohamed JANANE ALLAH" width="100%%" />

<br/>

Résoudre sur ordinateur les problèmes que la mécanique ne sait pas résoudre à la main :<br/>
**systèmes linéaires et non linéaires**, **équations aux dérivées partielles** par différences finies,
**équations différentielles ordinaires**.

[![Commencer](https://img.shields.io/badge/▶_Commencer_le_cours-Chapitre_0-0056D2?style=for-the-badge)](%(ch0)s)
[![Vidéo d'accroche](https://img.shields.io/badge/🎬_Pourquoi_ce_module_%%3F-Vidéo_d'accroche-C1121F?style=for-the-badge)](%(motiv)s)

<sub>🎓 Conçu pour les étudiants de la FSTM — Université Hassan II de Casablanca · 🔒 vidéos accessibles avec le compte universitaire UH2C</sub>

<table>
<tr>
<td align="center" width="20%%"><b>📚 %(nb_ch)s modules</b><br><sub>%(nb_pages)s pages de cours</sub></td>
<td align="center" width="20%%"><b>🎥 %(nb_videos)s vidéos</b><br><sub>cours et ateliers TP</sub></td>
<td align="center" width="20%%"><b>🔬 %(nb_tp)s TP MATLAB</b><br><sub>%(nb_corriges)s corrigés en scripts</sub></td>
<td align="center" width="20%%"><b>📝 %(nb_exam)s sujets d'examen</b><br><sub>archive en accès libre</sub></td>
<td align="center" width="20%%"><b>⏱️ 60 heures</b><br><sub>%(nb_td)s TD · en français</sub></td>
</tr>
</table>

[**À propos**](#-à-propos) · [**Programme**](#-programme-du-module) · [**Examens**](#-examens) · [**Enseignant**](#-enseignant) · [**Questions fréquentes**](#-questions-fréquentes) · [**🎮 Jeux**](#-jeux-interactifs)

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

| 🎓 Public | 🧩 Prérequis | 💻 Logiciel | 🗣️ Langue |
|---|---|---|---|
| LST Génie Mécanique · 1ʳᵉ année du Cycle d'Ingénieur Génie Énergétique (FSTM) | Algèbre linéaire, analyse (développements de Taylor), bases de MATLAB | MATLAB | Français |

---

## 📚 Programme du module

Il y a **%(nb_ch)s modules** dans ce cours, en trois parties précédées d'une introduction. Chaque module
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
d'Ingénieur Génie Énergétique (GE)** : les outils numériques sont exactement les mêmes de part et d'autre,
seules changent les applications.

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

Tous les PDF — cours, TD, énoncés de TP, sujets d'examen — et les **corrigés de TP** (scripts MATLAB, en zip)
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
et, quand il existe, `4_TPX_corrige_...` (corrigé librement téléchargeable).
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
valeurs = {
    "programme": "\n".join(programme), "tree": tree,
    "motiv": MOTIVATION, "ch0": ch0, "examens": texte_examens, "nb_exam": str(nb_examens),
    "nb_ch": str(len(CH)), "nb_pages": str(NB_PAGES), "nb_td": str(NB_TD), "nb_tp": str(NB_TP),
    "nb_corriges": str(NB_CORRIGES), "nb_videos": str(NB_VIDEOS),
    "apprendre": apprendre, "competences": "\n".join(etiquette(c) for c in COMPETENCES),
    "jeux": section_jeux(),
}
page = TPL.replace("%%", "%")
for k, v in valeurs.items():
    page = page.replace("%%(%s)s" % k, v)
assert "%(" not in page, "champ non remplace"
io.open(os.path.join(ROOT, "licence-genie-mecanique.md"), "w", encoding="utf-8", newline="\n").write(page)
print("OK - %d lignes" % page.count("\n"))
