<div align="center">

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

### 🚩 Introduction

| # | Chapitre | 📄 Cours | 📝 TD | 🔬 TP | 🎥 Vidéo |
|:-:|----------|:--------:|:-----:|:-----:|:--------:|
| **00** | Introduction générale | [PDF](methodes-numeriques/Chapitre_00_Introduction_generale/1_Cours_chapitre_00.pdf) | — | — | [▶ Voir](https://drive.google.com/file/d/18AdF62vRubU5swh_zy52d6AvmlzcVybn/view) |

<details>
<summary><i>Descriptif des chapitres</i></summary>
<br/>

**00 — Introduction générale** · 8 pages  
Pourquoi le calcul numérique en mécanique, et à quoi il sert concrètement dans le métier d'ingénieur. Présentation des exemples fils conducteurs du module.

</details>

### 🧮 Partie I — Systèmes algébriques

Résoudre *Ax = b*, puis *F(x) = 0* : les briques sur lesquelles repose tout le reste du module.

| # | Chapitre | 📄 Cours | 📝 TD | 🔬 TP | 🎥 Vidéo |
|:-:|----------|:--------:|:-----:|:-----:|:--------:|
| **01** | Rappels numériques : erreurs, normes et conditionnement | [PDF](methodes-numeriques/Chapitre_01_Rappels_numeriques/1_Cours_chapitre_01.pdf) | [TD](methodes-numeriques/Chapitre_01_Rappels_numeriques/3_TD01_enonce.pdf) | — | 🚧 |
| **02** | Systèmes linéaires : méthodes directes | [PDF](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/1_Cours_chapitre_02.pdf) | [TD](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/3_TD02_enonce.pdf) | [TP1](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/4_TP1_enonce.pdf) | 🚧 |
| **03** | Systèmes linéaires : méthodes itératives | [PDF](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/1_Cours_chapitre_03.pdf) | [TD](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/3_TD03_enonce.pdf) | [TP2](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/4_TP2_enonce.pdf) | 🚧 |
| **04** | Systèmes non linéaires | [PDF](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/1_Cours_chapitre_04.pdf) | [TD](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/3_TD04_enonce.pdf) | [TP3](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/4_TP3_enonce.pdf) | 🚧 |

<details>
<summary><i>Descriptif des chapitres</i></summary>
<br/>

**01 — Rappels numériques : erreurs, normes et conditionnement** · 13 pages  
Un ordinateur ne calcule jamais exactement : erreurs d'arrondi, normes vectorielles et matricielles, conditionnement d'une matrice.

**02 — Systèmes linéaires : méthodes directes** · 16 pages  
Résolution de Ax = b en un nombre fini d'opérations — la brique de base de tout calcul par éléments finis.

**03 — Systèmes linéaires : méthodes itératives** · 12 pages  
Pour les grands systèmes creux issus d'un maillage fin, là où l'élimination de Gauss coûte trop cher et détruit le caractère creux (fill-in).

**04 — Systèmes non linéaires** · 18 pages  
Résoudre F(x) = 0 quand la physique cesse d'être linéaire : pertes de charge quadratiques, ressort durcissant, grandes déformations.

</details>

### 🌡️ Partie II — EDP et différences finies

De la classification des EDP aux trois équations modèles de la mécanique : chaleur, Laplace-Poisson, ondes.

| # | Chapitre | 📄 Cours | 📝 TD | 🔬 TP | 🎥 Vidéo |
|:-:|----------|:--------:|:-----:|:-----:|:--------:|
| **05** | Généralités sur les EDP en mécanique et classification | [PDF](methodes-numeriques/Chapitre_05_Generalites_EDP/1_Cours_chapitre_05.pdf) | [TD](methodes-numeriques/Chapitre_05_Generalites_EDP/3_TD05_enonce.pdf) | — | 🚧 |
| **06** | Principe de la méthode des différences finies | [PDF](methodes-numeriques/Chapitre_06_Principe_differences_finies/1_Cours_chapitre_06.pdf) | [TD](methodes-numeriques/Chapitre_06_Principe_differences_finies/3_TD06_enonce.pdf) | — | 🚧 |
| **07** | Consistance, stabilité, convergence | [PDF](methodes-numeriques/Chapitre_07_Consistance_stabilite_convergence/1_Cours_chapitre_07.pdf) | [TD](methodes-numeriques/Chapitre_07_Consistance_stabilite_convergence/3_TD07_enonce.pdf) | — | 🚧 |
| **08** | Équation de la chaleur | [PDF](methodes-numeriques/Chapitre_08_Equation_chaleur/1_Cours_chapitre_08.pdf) | [TD](methodes-numeriques/Chapitre_08_Equation_chaleur/3_TD08_enonce.pdf) | — | 🚧 |
| **09** | Équation de Laplace-Poisson et advection-diffusion | [PDF](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/1_Cours_chapitre_09.pdf) | [TD](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/3_TD09_enonce.pdf) | [TP5](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/4_TP5_enonce.pdf) | 🚧 |
| **10** | Équation des ondes | [PDF](methodes-numeriques/Chapitre_10_Equation_ondes/1_Cours_chapitre_10.pdf) | [TD](methodes-numeriques/Chapitre_10_Equation_ondes/3_TD10_enonce.pdf) | — | 🚧 |

<details>
<summary><i>Descriptif des chapitres</i></summary>
<br/>

**05 — Généralités sur les EDP en mécanique et classification** · 10 pages  
L'inconnue n'est plus un vecteur mais un champ. Classification elliptique / parabolique / hyperbolique et conditions aux limites associées.

**06 — Principe de la méthode des différences finies** · 10 pages  
L'étape décisive : remplacer les dérivées, objets continus, par des quantités calculables sur ordinateur.

**07 — Consistance, stabilité, convergence** · 10 pages  
Pourquoi un schéma parfaitement construit sur le papier peut produire des résultats absurdes — des oscillations qui grandissent jusqu'à faire déborder les calculs.

**08 — Équation de la chaleur** · 11 pages  
Un problème physique résolu de bout en bout : la paroi de four en régime transitoire, de l'état initial jusqu'à l'équilibre.

**09 — Équation de Laplace-Poisson et advection-diffusion** · 11 pages  
Discrétisation 2D complète (Dirichlet puis Neumann), validation sur un cas test analytique, puis introduction de l'advection-diffusion.

**10 — Équation des ondes** · 11 pages  
La corde vibrante et sa condition de stabilité — la condition CFL, avec son interprétation géométrique remarquable.

</details>

### 📈 Partie III — Équations différentielles ordinaires

Retour au temps : Euler, Runge-Kutta et la question de la stabilité du pas de temps.

| # | Chapitre | 📄 Cours | 📝 TD | 🔬 TP | 🎥 Vidéo |
|:-:|----------|:--------:|:-----:|:-----:|:--------:|
| **11** | Résolution numérique des équations différentielles ordinaires | [PDF](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/1_Cours_chapitre_11.pdf) | [TD](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/3_TD11_enonce.pdf) | [TP4](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/4_TP4_enonce.pdf)<br>[TP6](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/4_TP6_enonce.pdf) | 🚧 |

<details>
<summary><i>Descriptif des chapitres</i></summary>
<br/>

**11 — Résolution numérique des équations différentielles ordinaires** · 14 pages  
L'évolution temporelle des systèmes à nombre fini de degrés de liberté : oscillateurs, mécanismes, circuits équivalents.

</details>

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
├── Chapitre_00_Introduction_generale/
├── Chapitre_01_Rappels_numeriques/
├── Chapitre_02_Systemes_lineaires_directs/
├── Chapitre_03_Systemes_lineaires_iteratifs/
├── Chapitre_04_Systemes_non_lineaires/
├── Chapitre_05_Generalites_EDP/
├── Chapitre_06_Principe_differences_finies/
├── Chapitre_07_Consistance_stabilite_convergence/
├── Chapitre_08_Equation_chaleur/
├── Chapitre_09_Laplace_Poisson_advection/
├── Chapitre_10_Equation_ondes/
├── Chapitre_11_EDO_Euler_Runge_Kutta/
```

Dans chaque dossier : `1_Cours_chapitre_XX.pdf`, `3_TDXX_enonce.pdf`, `4_TPX_enonce.pdf`.

</details>

---

## 🎥 Vidéos

🎬 **1 capsule(s) en ligne** sur 12 chapitres.

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
