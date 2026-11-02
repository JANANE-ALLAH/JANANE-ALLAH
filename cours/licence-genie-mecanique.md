[⬅ Profil](../README.md) › Enseignement › **Méthodes numériques pour la mécanique**

<div align="center">

<img src="methodes-numeriques/images/banniere.jpg" alt="Méthodes numériques pour la mécanique — FSTM, Université Hassan II de Casablanca — Pr. Mohamed JANANE ALLAH" width="100%" />

<br/>

Résoudre sur ordinateur les problèmes que la mécanique ne sait pas résoudre à la main :<br/>
**systèmes linéaires et non linéaires**, **équations aux dérivées partielles** par différences finies,
**équations différentielles ordinaires**.

[![Commencer](https://img.shields.io/badge/▶_Commencer_le_cours-Chapitre_0-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_00_Introduction_generale/1_Cours_chapitre_00.pdf)
[![Vidéo d'accroche](https://img.shields.io/badge/🎬_Pourquoi_ce_module_%3F-Vidéo_d'accroche-C1121F?style=for-the-badge)](https://drive.google.com/file/d/1dc97-wJZVYQ1Gan3rmW4U6hYal3hQO9W/view)

<sub>🎓 Conçu pour les étudiants de la FSTM — Université Hassan II de Casablanca · 🔒 vidéos accessibles avec le compte universitaire UH2C</sub>

<table>
<tr>
<td align="center" width="20%"><b>📚 12 modules</b><br><sub>144 pages de cours</sub></td>
<td align="center" width="20%"><b>🎥 18 vidéos</b><br><sub>cours et ateliers TP</sub></td>
<td align="center" width="20%"><b>🔬 6 TP MATLAB</b><br><sub>6 corrigés en scripts</sub></td>
<td align="center" width="20%"><b>📝 8 sujets d'examen</b><br><sub>archive en accès libre</sub></td>
<td align="center" width="20%"><b>⏱️ 60 heures</b><br><sub>11 TD · en français</sub></td>
</tr>
</table>

[**À propos**](#-à-propos) · [**Programme**](#-programme-du-module) · [**Examens**](#-examens) · [**Enseignant**](#-enseignant) · [**Questions fréquentes**](#-questions-fréquentes)

</div>

---

## 📌 À propos

Ce module donne les outils numériques qui permettent de résoudre, sur ordinateur, les problèmes
que la mécanique ne sait pas résoudre à la main : **systèmes linéaires** (méthodes directes et
itératives), **systèmes non linéaires**, **équations aux dérivées partielles** par différences
finies, et **équations différentielles ordinaires**.

#### Ce que vous apprendrez

<table>
<tr><td width="50%" valign="top">✔️ Choisir une méthode adaptée à la taille et à la structure du problème</td><td width="50%" valign="top">✔️ Estimer la précision d'un résultat et reconnaître un calcul qui diverge</td></tr>
<tr><td width="50%" valign="top">✔️ Programmer ces méthodes en MATLAB et valider un schéma sur un cas test analytique</td><td width="50%" valign="top">✔️ Interpréter physiquement les conditions de stabilité (CFL, critères de convergence)</td></tr>
</table>

#### Compétences que vous allez acquérir

![MATLAB](https://img.shields.io/badge/MATLAB-E8EEF7?style=flat-square)
![Erreurs et conditionnement](https://img.shields.io/badge/Erreurs%20et%20conditionnement-E8EEF7?style=flat-square)
![Élimination de Gauss](https://img.shields.io/badge/%C3%89limination%20de%20Gauss-E8EEF7?style=flat-square)
![Jacobi · Gauss-Seidel · SOR](https://img.shields.io/badge/Jacobi%20%C2%B7%20Gauss--Seidel%20%C2%B7%20SOR-E8EEF7?style=flat-square)
![Méthode de Newton](https://img.shields.io/badge/M%C3%A9thode%20de%20Newton-E8EEF7?style=flat-square)
![Différences finies](https://img.shields.io/badge/Diff%C3%A9rences%20finies-E8EEF7?style=flat-square)
![Stabilité de von Neumann](https://img.shields.io/badge/Stabilit%C3%A9%20de%20von%20Neumann-E8EEF7?style=flat-square)
![Condition CFL](https://img.shields.io/badge/Condition%20CFL-E8EEF7?style=flat-square)
![Crank-Nicolson](https://img.shields.io/badge/Crank--Nicolson-E8EEF7?style=flat-square)
![Schéma décentré (upwind)](https://img.shields.io/badge/Sch%C3%A9ma%20d%C3%A9centr%C3%A9%20%28upwind%29-E8EEF7?style=flat-square)
![Euler et Runge-Kutta](https://img.shields.io/badge/Euler%20et%20Runge--Kutta-E8EEF7?style=flat-square)

#### Détails à connaître

| 🎓 Public | 🧩 Prérequis | 💻 Logiciel | 🗣️ Langue |
|---|---|---|---|
| LST Génie Mécanique · 1ʳᵉ année du Cycle d'Ingénieur Génie Énergétique (FSTM) | Algèbre linéaire, analyse (développements de Taylor), bases de MATLAB | MATLAB | Français |

---

## 📚 Programme du module

Il y a **12 modules** dans ce cours, en trois parties précédées d'une introduction. Ouvrez un module
pour voir son contenu et accéder à ses supports.

### 🚩 Introduction

<sub>1 module · 8 pages de cours</sub>

<details>
<summary><b>Module 00 · Introduction générale</b><br><sub>📄 8 pages · 🎥 1 vidéo</sub></summary>
<br>

Pourquoi le calcul numérique en mécanique, et à quoi il sert concrètement dans le métier d'ingénieur. Présentation des exemples fils conducteurs du module.

- 📄 [Cours — 8 pages (PDF)](methodes-numeriques/Chapitre_00_Introduction_generale/1_Cours_chapitre_00.pdf)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/18AdF62vRubU5swh_zy52d6AvmlzcVybn/view)

</details>

### 🧮 Partie I — Systèmes algébriques

<sub>4 modules · 59 pages de cours</sub>

Résoudre *Ax = b*, puis *F(x) = 0* : les briques sur lesquelles repose tout le reste du module.

<details>
<summary><b>Module 01 · Rappels numériques : erreurs, normes et conditionnement</b><br><sub>📄 13 pages · 🎥 1 vidéo · 📝 TD</sub></summary>
<br>

Un ordinateur ne calcule jamais exactement : erreurs d'arrondi, normes vectorielles et matricielles, conditionnement d'une matrice.

- 📄 [Cours — 13 pages (PDF)](methodes-numeriques/Chapitre_01_Rappels_numeriques/1_Cours_chapitre_01.pdf)
- 📝 [TD — énoncé (PDF)](methodes-numeriques/Chapitre_01_Rappels_numeriques/3_TD01_enonce.pdf)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/13uDHLzPXsp9XpujDGj60SXAgyNtyW84X/view)

</details>

<details>
<summary><b>Module 02 · Systèmes linéaires : méthodes directes</b><br><sub>📄 16 pages · 🎥 2 vidéos · 📝 TD · 🔬 TP1 · ✅ corrigé</sub></summary>
<br>

Résolution de Ax = b en un nombre fini d'opérations — la brique de base de tout calcul par éléments finis.

- 📄 [Cours — 16 pages (PDF)](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/1_Cours_chapitre_02.pdf)
- 📝 [TD — énoncé (PDF)](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/3_TD02_enonce.pdf)
- 🔬 [TP1 — énoncé (PDF)](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/4_TP1_enonce.pdf)
- ✅ [TP1 — scripts MATLAB (zip)](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/4_TP1_corrige_scripts_MATLAB.zip)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/19rK9Xc4acZQ77KQnYxwGSc7pkNBj1MKc/view)
- 🎥 [Vidéo TP1 — atelier MATLAB 🔒](https://drive.google.com/file/d/1kmhqkhzH1HCGq9E5eakniAzW5kthOiE-/view)

</details>

<details>
<summary><b>Module 03 · Systèmes linéaires : méthodes itératives</b><br><sub>📄 12 pages · 🎥 2 vidéos · 📝 TD · 🔬 TP2 · ✅ corrigé</sub></summary>
<br>

Pour les grands systèmes creux issus d'un maillage fin, là où l'élimination de Gauss coûte trop cher et détruit le caractère creux (fill-in).

- 📄 [Cours — 12 pages (PDF)](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/1_Cours_chapitre_03.pdf)
- 📝 [TD — énoncé (PDF)](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/3_TD03_enonce.pdf)
- 🔬 [TP2 — énoncé (PDF)](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/4_TP2_enonce.pdf)
- ✅ [TP2 — scripts MATLAB (zip)](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/4_TP2_corrige_scripts_MATLAB.zip)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/19Q7Vj94XDHRTuFz_X4l-3xFFBQQcJwZI/view)
- 🎥 [Vidéo TP2 — atelier MATLAB 🔒](https://drive.google.com/file/d/1dw82htm3bDXOKr3v-Jziv230Bs23vpe0/view)

</details>

<details>
<summary><b>Module 04 · Systèmes non linéaires</b><br><sub>📄 18 pages · 🎥 2 vidéos · 📝 TD · 🔬 TP3 · ✅ corrigé</sub></summary>
<br>

Résoudre F(x) = 0 quand la physique cesse d'être linéaire : pertes de charge quadratiques, ressort durcissant, grandes déformations.

- 📄 [Cours — 18 pages (PDF)](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/1_Cours_chapitre_04.pdf)
- 📝 [TD — énoncé (PDF)](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/3_TD04_enonce.pdf)
- 🔬 [TP3 — énoncé (PDF)](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/4_TP3_enonce.pdf)
- ✅ [TP3 — scripts MATLAB (zip)](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/4_TP3_corrige_scripts_MATLAB.zip)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/125--JQ7p31u2xEMZVsSO3x2MCeXNOXYA/view)
- 🎥 [Vidéo TP3 — programmation de Newton 🔒](https://drive.google.com/file/d/1b4vdrutxz_yeuuil7ytYzb3D7f6wrNUL/view)

</details>

### 🌡️ Partie II — EDP et différences finies

<sub>6 modules · 63 pages de cours</sub>

De la classification des EDP aux trois équations modèles de la mécanique : chaleur, Laplace-Poisson, ondes.

<details>
<summary><b>Module 05 · Généralités sur les EDP en mécanique et classification</b><br><sub>📄 10 pages · 🎥 1 vidéo · 📝 TD</sub></summary>
<br>

L'inconnue n'est plus un vecteur mais un champ. Classification elliptique / parabolique / hyperbolique et conditions aux limites associées.

- 📄 [Cours — 10 pages (PDF)](methodes-numeriques/Chapitre_05_Generalites_EDP/1_Cours_chapitre_05.pdf)
- 📝 [TD — énoncé (PDF)](methodes-numeriques/Chapitre_05_Generalites_EDP/3_TD05_enonce.pdf)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/1wxEG6bzlLQPGz-evjzRmrmuqnVQsqqgs/view)

</details>

<details>
<summary><b>Module 06 · Principe de la méthode des différences finies</b><br><sub>📄 10 pages · 🎥 1 vidéo · 📝 TD</sub></summary>
<br>

L'étape décisive : remplacer les dérivées, objets continus, par des quantités calculables sur ordinateur.

- 📄 [Cours — 10 pages (PDF)](methodes-numeriques/Chapitre_06_Principe_differences_finies/1_Cours_chapitre_06.pdf)
- 📝 [TD — énoncé (PDF)](methodes-numeriques/Chapitre_06_Principe_differences_finies/3_TD06_enonce.pdf)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/1F-IuYtpVuRNhaj7w13zxnSUldtZj1PoB/view)

</details>

<details>
<summary><b>Module 07 · Consistance, stabilité, convergence</b><br><sub>📄 10 pages · 🎥 1 vidéo · 📝 TD</sub></summary>
<br>

Pourquoi un schéma parfaitement construit sur le papier peut produire des résultats absurdes — des oscillations qui grandissent jusqu'à faire déborder les calculs.

- 📄 [Cours — 10 pages (PDF)](methodes-numeriques/Chapitre_07_Consistance_stabilite_convergence/1_Cours_chapitre_07.pdf)
- 📝 [TD — énoncé (PDF)](methodes-numeriques/Chapitre_07_Consistance_stabilite_convergence/3_TD07_enonce.pdf)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/1AT_64YZW3ebVt21abcGkxcZUoLHFnnkg/view)

</details>

<details>
<summary><b>Module 08 · Équation de la chaleur</b><br><sub>📄 11 pages · 🎥 1 vidéo · 📝 TD</sub></summary>
<br>

Un problème physique résolu de bout en bout : la paroi de four en régime transitoire, de l'état initial jusqu'à l'équilibre.

- 📄 [Cours — 11 pages (PDF)](methodes-numeriques/Chapitre_08_Equation_chaleur/1_Cours_chapitre_08.pdf)
- 📝 [TD — énoncé (PDF)](methodes-numeriques/Chapitre_08_Equation_chaleur/3_TD08_enonce.pdf)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/18wNa17e4CPXprrvWbSh1HTMUlAU2F5dD/view)

</details>

<details>
<summary><b>Module 09 · Équation de Laplace-Poisson et advection-diffusion</b><br><sub>📄 11 pages · 🎥 2 vidéos · 📝 TD · 🔬 TP5 · ✅ corrigé</sub></summary>
<br>

Discrétisation 2D complète (Dirichlet puis Neumann), validation sur un cas test analytique, puis introduction de l'advection-diffusion.

- 📄 [Cours — 11 pages (PDF)](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/1_Cours_chapitre_09.pdf)
- 📝 [TD — énoncé (PDF)](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/3_TD09_enonce.pdf)
- 🔬 [TP5 — énoncé (PDF)](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/4_TP5_enonce.pdf)
- ✅ [TP5 — scripts MATLAB (zip)](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/4_TP5_corrige_scripts_MATLAB.zip)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/1YinQ_oHGrndBm2nsGVBWTBDI62pUBbBE/view)
- 🎥 [Vidéo TP5 — correction 🔒](https://drive.google.com/file/d/1qhSEHFj44XbFneGbJCBylgvrMxVg7l5O/view)

</details>

<details>
<summary><b>Module 10 · Équation des ondes</b><br><sub>📄 11 pages · 🎥 1 vidéo · 📝 TD</sub></summary>
<br>

La corde vibrante et sa condition de stabilité — la condition CFL, avec son interprétation géométrique remarquable.

- 📄 [Cours — 11 pages (PDF)](methodes-numeriques/Chapitre_10_Equation_ondes/1_Cours_chapitre_10.pdf)
- 📝 [TD — énoncé (PDF)](methodes-numeriques/Chapitre_10_Equation_ondes/3_TD10_enonce.pdf)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/1IQh3d69BFptw47AmVj_zgeMaxRPnpFTB/view)

</details>

### 📈 Partie III — Équations différentielles ordinaires

<sub>1 module · 14 pages de cours</sub>

Retour au temps : Euler, Runge-Kutta et la question de la stabilité du pas de temps.

<details>
<summary><b>Module 11 · Résolution numérique des équations différentielles ordinaires</b><br><sub>📄 14 pages · 🎥 3 vidéos · 📝 TD · 🔬 TP4 · TP6 · ✅ corrigé</sub></summary>
<br>

L'évolution temporelle des systèmes à nombre fini de degrés de liberté : oscillateurs, mécanismes, circuits équivalents.

- 📄 [Cours — 14 pages (PDF)](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/1_Cours_chapitre_11.pdf)
- 📝 [TD — énoncé (PDF)](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/3_TD11_enonce.pdf)
- 🔬 [TP4 — énoncé (PDF)](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/4_TP4_enonce.pdf)
- 🔬 [TP6 — énoncé (PDF)](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/4_TP6_enonce.pdf)
- ✅ [TP4 — scripts MATLAB (zip)](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/4_TP4_corrige_scripts_MATLAB.zip)
- ✅ [TP6 — scripts MATLAB (zip)](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/4_TP6_corrige_scripts_MATLAB.zip)
- 🎥 [Vidéo du cours 🔒](https://drive.google.com/file/d/1OZqZkwXP--N1ZcmgipRbnzRsleo4AnD8/view)
- 🎥 [Vidéo TP4 — programmation complète 🔒](https://drive.google.com/file/d/1GeBDuM-bsHzrqXIGovBEPhuHptdbIkzp/view)
- 🎥 [Vidéo TP6 — programmation complète 🔒](https://drive.google.com/file/d/1FFd2tp73XQvZY2wPG-ukHws2T4iTNNlx/view)

</details>

<details>
<summary>📋 <b>Toutes les ressources en un tableau</b> (accès rapide)</summary>
<br/>

| # | Chapitre | 📄 Cours | 📝 TD | 🔬 TP | ✅ Corrigé | 🎥 Vidéo |
|:-:|----------|:--------:|:-----:|:-----:|:----------:|:--------:|
| **00** | Introduction générale | [PDF](methodes-numeriques/Chapitre_00_Introduction_generale/1_Cours_chapitre_00.pdf) | — | — | — | [▶ Voir](https://drive.google.com/file/d/18AdF62vRubU5swh_zy52d6AvmlzcVybn/view) |
| **01** | Rappels numériques : erreurs, normes et conditionnement | [PDF](methodes-numeriques/Chapitre_01_Rappels_numeriques/1_Cours_chapitre_01.pdf) | [TD](methodes-numeriques/Chapitre_01_Rappels_numeriques/3_TD01_enonce.pdf) | — | — | [▶ Voir](https://drive.google.com/file/d/13uDHLzPXsp9XpujDGj60SXAgyNtyW84X/view) |
| **02** | Systèmes linéaires : méthodes directes | [PDF](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/1_Cours_chapitre_02.pdf) | [TD](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/3_TD02_enonce.pdf) | [TP1](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/4_TP1_enonce.pdf) | [📦 TP1 — scripts MATLAB](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/4_TP1_corrige_scripts_MATLAB.zip) | [▶ Cours](https://drive.google.com/file/d/19rK9Xc4acZQ77KQnYxwGSc7pkNBj1MKc/view)<br>[▶ TP1 — atelier MATLAB](https://drive.google.com/file/d/1kmhqkhzH1HCGq9E5eakniAzW5kthOiE-/view) |
| **03** | Systèmes linéaires : méthodes itératives | [PDF](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/1_Cours_chapitre_03.pdf) | [TD](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/3_TD03_enonce.pdf) | [TP2](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/4_TP2_enonce.pdf) | [📦 TP2 — scripts MATLAB](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/4_TP2_corrige_scripts_MATLAB.zip) | [▶ Cours](https://drive.google.com/file/d/19Q7Vj94XDHRTuFz_X4l-3xFFBQQcJwZI/view)<br>[▶ TP2 — atelier MATLAB](https://drive.google.com/file/d/1dw82htm3bDXOKr3v-Jziv230Bs23vpe0/view) |
| **04** | Systèmes non linéaires | [PDF](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/1_Cours_chapitre_04.pdf) | [TD](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/3_TD04_enonce.pdf) | [TP3](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/4_TP3_enonce.pdf) | [📦 TP3 — scripts MATLAB](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/4_TP3_corrige_scripts_MATLAB.zip) | [▶ Cours](https://drive.google.com/file/d/125--JQ7p31u2xEMZVsSO3x2MCeXNOXYA/view)<br>[▶ TP3 — programmation de Newton](https://drive.google.com/file/d/1b4vdrutxz_yeuuil7ytYzb3D7f6wrNUL/view) |
| **05** | Généralités sur les EDP en mécanique et classification | [PDF](methodes-numeriques/Chapitre_05_Generalites_EDP/1_Cours_chapitre_05.pdf) | [TD](methodes-numeriques/Chapitre_05_Generalites_EDP/3_TD05_enonce.pdf) | — | — | [▶ Voir](https://drive.google.com/file/d/1wxEG6bzlLQPGz-evjzRmrmuqnVQsqqgs/view) |
| **06** | Principe de la méthode des différences finies | [PDF](methodes-numeriques/Chapitre_06_Principe_differences_finies/1_Cours_chapitre_06.pdf) | [TD](methodes-numeriques/Chapitre_06_Principe_differences_finies/3_TD06_enonce.pdf) | — | — | [▶ Voir](https://drive.google.com/file/d/1F-IuYtpVuRNhaj7w13zxnSUldtZj1PoB/view) |
| **07** | Consistance, stabilité, convergence | [PDF](methodes-numeriques/Chapitre_07_Consistance_stabilite_convergence/1_Cours_chapitre_07.pdf) | [TD](methodes-numeriques/Chapitre_07_Consistance_stabilite_convergence/3_TD07_enonce.pdf) | — | — | [▶ Voir](https://drive.google.com/file/d/1AT_64YZW3ebVt21abcGkxcZUoLHFnnkg/view) |
| **08** | Équation de la chaleur | [PDF](methodes-numeriques/Chapitre_08_Equation_chaleur/1_Cours_chapitre_08.pdf) | [TD](methodes-numeriques/Chapitre_08_Equation_chaleur/3_TD08_enonce.pdf) | — | — | [▶ Voir](https://drive.google.com/file/d/18wNa17e4CPXprrvWbSh1HTMUlAU2F5dD/view) |
| **09** | Équation de Laplace-Poisson et advection-diffusion | [PDF](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/1_Cours_chapitre_09.pdf) | [TD](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/3_TD09_enonce.pdf) | [TP5](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/4_TP5_enonce.pdf) | [📦 TP5 — scripts MATLAB](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/4_TP5_corrige_scripts_MATLAB.zip) | [▶ Cours](https://drive.google.com/file/d/1YinQ_oHGrndBm2nsGVBWTBDI62pUBbBE/view)<br>[▶ TP5 — correction](https://drive.google.com/file/d/1qhSEHFj44XbFneGbJCBylgvrMxVg7l5O/view) |
| **10** | Équation des ondes | [PDF](methodes-numeriques/Chapitre_10_Equation_ondes/1_Cours_chapitre_10.pdf) | [TD](methodes-numeriques/Chapitre_10_Equation_ondes/3_TD10_enonce.pdf) | — | — | [▶ Voir](https://drive.google.com/file/d/1IQh3d69BFptw47AmVj_zgeMaxRPnpFTB/view) |
| **11** | Résolution numérique des équations différentielles ordinaires | [PDF](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/1_Cours_chapitre_11.pdf) | [TD](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/3_TD11_enonce.pdf) | [TP4](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/4_TP4_enonce.pdf)<br>[TP6](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/4_TP6_enonce.pdf) | [📦 TP4 — scripts MATLAB](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/4_TP4_corrige_scripts_MATLAB.zip)<br>[📦 TP6 — scripts MATLAB](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/4_TP6_corrige_scripts_MATLAB.zip) | [▶ Cours](https://drive.google.com/file/d/1OZqZkwXP--N1ZcmgipRbnzRsleo4AnD8/view)<br>[▶ TP4 — programmation complète](https://drive.google.com/file/d/1GeBDuM-bsHzrqXIGovBEPhuHptdbIkzp/view)<br>[▶ TP6 — programmation complète](https://drive.google.com/file/d/1FFd2tp73XQvZY2wPG-ukHws2T4iTNNlx/view) |

</details>

---

## 📝 Examens

Sujets des sessions précédentes, en accès libre, pour s'entraîner dans les conditions de
l'épreuve (durée : 2 h). Les sujets **A** et **B** posent les mêmes questions avec des
données numériques différentes.

### 🗂️ Année universitaire 2025/2026

| Épreuve | Programme | 📄 Sujets |
|---|---|:-:|
| **Examen — Partie I** | Systèmes d'équations linéaires et non linéaires | [Sujet A](methodes-numeriques/Examens/examen_partie1_2025_2026_sujetA.pdf) · [Sujet B](methodes-numeriques/Examens/examen_partie1_2025_2026_sujetB.pdf) |
| **Examen — Partie II** | Méthodes des différences finies | [Sujet A](methodes-numeriques/Examens/examen_partie2_2025_2026_sujetA.pdf) · [Sujet B](methodes-numeriques/Examens/examen_partie2_2025_2026_sujetB.pdf) |
| **Examen de préparation n°1** | Parties I et II — niveau difficile | [PDF](methodes-numeriques/Examens/examens_preparation_2025_2026/examen_preparation_1_2025_2026.pdf) |
| **Examen de préparation n°2** | Parties I et II — niveau difficile | [PDF](methodes-numeriques/Examens/examens_preparation_2025_2026/examen_preparation_2_2025_2026.pdf) |

### 🗂️ Année universitaire 2024/2025

| Épreuve | Programme | 📄 Sujets |
|---|---|:-:|
| **Examen — Parties I et II** | Systèmes d'équations et méthodes des différences finies | [Sujet A](methodes-numeriques/Examens/examen_mixte_2024_2025_sujetA.pdf) · [Sujet B](methodes-numeriques/Examens/examen_mixte_2024_2025_sujetB.pdf) |

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

Commencez par la **[vidéo d'accroche](https://drive.google.com/file/d/1dc97-wJZVYQ1Gan3rmW4U6hYal3hQO9W/view)** : où le calcul numérique intervient réellement dans le
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
└── Examens/
```

Dans chaque dossier : `1_Cours_chapitre_XX.pdf`, `3_TDXX_enonce.pdf`, `4_TPX_enonce.pdf`,
et, quand il existe, `4_TPX_corrige_...` (corrigé librement téléchargeable).
Sujets d'examen dans `Examens/` : `examen_<partie1|partie2|mixte>_AAAA_AAAA_sujetX.pdf`,
`examen_preparation_N_AAAA_AAAA.pdf`.

</details>

---

<div align="center">

[![Email](https://img.shields.io/badge/mohamedjanane147@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mohamedjanane147@gmail.com)
[![Site](https://img.shields.io/badge/janane--allah.github.io-0A66C2?style=flat-square&logo=github-pages&logoColor=white)](https://janane-allah.github.io)
[![Retour au profil](https://img.shields.io/badge/⬅_Retour_au_profil-555555?style=flat-square)](../README.md)

<sub>Page générée par <code>tools/build_page.py</code> · Université Hassan II de Casablanca — FSTM</sub>

</div>
