# -*- coding: utf-8 -*-
import io, os

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
 "00": "https://drive.google.com/file/d/18AdF62vRubU5swh_zy52d6AvmlzcVybn/view?usp=drive_link",
}


def video(num):
    url = VIDEOS.get(num)
    return "[▶ Voir](%s)" % url if url else "🚧"


PARTS = [
 ("🚩", "Introduction", ["00"], ""),
 ("🧮", "Partie I — Systèmes algébriques", ["01", "02", "03", "04"],
  "Résoudre *Ax = b*, puis *F(x) = 0* : les briques sur lesquelles repose tout le reste du module."),
 ("🌡️", "Partie II — EDP et différences finies", ["05", "06", "07", "08", "09", "10"],
  "De la classification des EDP aux trois équations modèles de la mécanique : chaleur, Laplace-Poisson, ondes."),
 ("📈", "Partie III — Équations différentielles ordinaires", ["11"],
  "Retour au temps : Euler, Runge-Kutta et la question de la stabilité du pas de temps."),
]


def links(num, prefix, label):
    d = CH[num][0]
    hits = sorted(f for f in os.listdir(os.path.join(ROOT, B, d)) if f.startswith(prefix))
    if not hits:
        return "—"
    return "<br>".join(
        "[%s](%s/%s/%s)" % (f.split("_")[1] if prefix == "4_" else label, B, d, f)
        for f in hits)


body = []
for icon, title, nums, blurb in PARTS:
    body.append("### %s %s\n" % (icon, title))
    if blurb:
        body.append("%s\n" % blurb)
    body.append("| # | Chapitre | 📄 Cours | 📝 TD | 🔬 TP | 🎥 Vidéo |")
    body.append("|:-:|----------|:--------:|:-----:|:-----:|:--------:|")
    for n in nums:
        body.append("| **%s** | %s | %s | %s | %s | %s |" % (
            n, CH[n][1], links(n, "1_", "PDF"), links(n, "3_", "TD"), links(n, "4_", "TP"),
            video(n)))
    body.append("")
    body.append("<details>\n<summary><i>Descriptif des chapitres</i></summary>\n<br/>\n")
    for n in nums:
        body.append("**%s — %s** · %d pages  \n%s\n" % (n, CH[n][1], CH[n][2], CH[n][3]))
    body.append("</details>\n")

tree = "\n".join("├── %s/" % CH[n][0] for n in sorted(CH))

TPL = u"""<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=3500&pause=1000&color=2E86AB&center=true&vCenter=true&width=780&lines=M%C3%A9thodes+Num%C3%A9riques+pour+la+M%C3%A9canique;LST+G%C3%A9nie+M%C3%A9canique+%E2%80%94+FSTM%2C+UH2C;12+chapitres+%C2%B7+11+TD+%C2%B7+6+TP+MATLAB" alt="Methodes Numeriques pour la Mecanique" />

**Pr. Mohamed JANANE ALLAH**, PhD — Maître de Conférence<br/>
Faculté des Sciences et Techniques de Mohammedia — Université Hassan II de Casablanca

<br/>

![Volume](https://img.shields.io/badge/Volume-60_heures-2E86AB?style=for-the-badge)
![Chapitres](https://img.shields.io/badge/Chapitres-12-4C9A2A?style=for-the-badge)
![TD](https://img.shields.io/badge/TD-11-6A4C93?style=for-the-badge)
![TP](https://img.shields.io/badge/TP-6-C1121F?style=for-the-badge)
![MATLAB](https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white)

[**Plan du cours**](#-plan-du-cours) · [**Méthode de travail**](#-comment-travailler-ce-module) · [**Vidéos**](#-vidéos) · [**Contact**](#-contact)

[![Retour au profil](https://img.shields.io/badge/⬅_Retour_au_profil-555555?style=flat-square)](../README.md)

</div>

---

## 🎯 Objectifs du module

Ce module donne les outils numériques qui permettent de résoudre, sur ordinateur, les problèmes
que la mécanique ne sait pas résoudre à la main : **systèmes linéaires** (méthodes directes et
itératives), **systèmes non linéaires**, **équations aux dérivées partielles** par différences
finies, et **équations différentielles ordinaires**.

À l'issue du module, vous saurez :

- ✅ choisir une méthode adaptée à la taille et à la structure du problème ;
- ✅ estimer la précision d'un résultat et reconnaître un calcul qui diverge ;
- ✅ programmer ces méthodes en **MATLAB** et valider un schéma sur un cas test analytique ;
- ✅ interpréter physiquement les conditions de stabilité (CFL, critères de convergence).

> 📌 Module **mutualisé** entre la **LST Génie Mécanique** et le **Cycle d'Ingénieur Génie Énergétique** :
> les outils numériques sont exactement les mêmes de part et d'autre, seules changent les applications.

---

## 📚 Plan du cours

%(body)s
---

## 🧭 Comment travailler ce module

| Étape | Support | Objectif |
|:-:|---|---|
| 1️⃣ | 📄 **Cours** | Lire le chapitre avant la séance — les notions s'enchaînent, chaque chapitre s'appuie sur le précédent. |
| 2️⃣ | 📝 **TD** | Faire les exercices à la main : c'est là que les méthodes se comprennent vraiment. |
| 3️⃣ | 🔬 **TP** | Programmer la méthode en MATLAB et la confronter à un cas test dont on connaît la solution. |

**Prérequis :** algèbre linéaire, analyse (développements de Taylor), bases de MATLAB.

<details>
<summary>📂 <i>Organisation des fichiers</i></summary>
<br/>

```
cours/methodes-numeriques/
%(tree)s
```

Dans chaque dossier : `1_Cours_chapitre_XX.pdf`, `3_TDXX_enonce.pdf`, `4_TPX_enonce.pdf`.

</details>

---

## 🎥 Vidéos

%(videos)s

Les capsules sont ajoutées au fur et à mesure : la colonne 🎥 du plan donne accès à celles
qui sont en ligne, 🚧 signale un chapitre dont la vidéo n'est pas encore disponible.

> 🔒 **Accès réservé aux étudiants de l'Université Hassan II de Casablanca.**
> Connectez-vous à votre **compte universitaire** avant d'ouvrir un lien vidéo : depuis un
> compte personnel, Google affichera une demande d'autorisation. Si l'accès vous est refusé
> alors que vous êtes bien inscrit au module, écrivez-moi.

---

## 📫 Contact

<div align="center">

[![Email](https://img.shields.io/badge/mohamedjanane147@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mohamedjanane147@gmail.com)
[![Site](https://img.shields.io/badge/janane--allah.github.io-0A66C2?style=flat-square&logo=github-pages&logoColor=white)](https://janane-allah.github.io)

📍 FSTM — BP 146, Mohammedia 28806, Maroc

</div>
"""

compteur = u"🎬 **%d capsule(s) en ligne** sur %d chapitres." % (len(VIDEOS), len(CH))
page = TPL.replace("%(body)s", "\n".join(body)).replace("%(tree)s", tree).replace("%(videos)s", compteur)
io.open(os.path.join(ROOT, "licence-genie-mecanique.md"), "w", encoding="utf-8", newline="\n").write(page)
print("OK - %d lignes" % page.count("\n"))
