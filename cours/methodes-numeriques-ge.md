[⬅ Profil](../README.md) › Enseignement › **Introduction aux méthodes numériques** · Cycle d'Ingénieur GE

<div align="center">

<img src="methodes-numeriques/images/banniere-ge.jpg" alt="Introduction aux méthodes numériques — 1re année du Cycle d'Ingénieur Génie Énergétique — FSTM, Université Hassan II de Casablanca — Pr. Mohamed JANANE ALLAH" width="100%" />

<br/>

Résoudre sur ordinateur les problèmes de l'énergétique qu'on ne sait pas résoudre à la main :<br/>
**systèmes linéaires et non linéaires** (réseaux thermiques et hydrauliques), **équations aux dérivées partielles**
par différences finies (conduction, convection), **équations différentielles ordinaires** (dynamique thermique).

[![Commencer](https://img.shields.io/badge/▶_Commencer_le_cours-Chapitre_0-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_00_Introduction_generale/1_Cours_chapitre_00.pdf)
[![Polycopié du cours](https://img.shields.io/badge/%F0%9F%93%98%20Polycopi%C3%A9%20du%20cours-203%20pages%20%C2%B7%20PDF-2E7D32?style=for-the-badge)](methodes-numeriques/Polycopie/Polycopie_Methodes_Numeriques.pdf)

<sub>🎓 1ʳᵉ année du Cycle d'Ingénieur Génie Énergétique (GE) — FSTM, Université Hassan II de Casablanca · 🔒 vidéos accessibles avec le compte universitaire UH2C</sub>

<table>
<tr>
<td align="center" width="20%"><b>📚 12 modules</b><br><sub>144 pages de cours</sub></td>
<td align="center" width="20%"><b>🎥 14 vidéos</b><br><sub>cours et TP GE</sub></td>
<td align="center" width="20%"><b>⚡ 3 TD · 2 TP GE</b><br><sub>jusqu'au chapitre 3</sub></td>
<td align="center" width="20%"><b>🎮 10 jeux</b><br><sub>TP1 et TP2 GE</sub></td>
<td align="center" width="20%"><b>⏱️ 48 h</b><br><sub>5 TP MATLAB</sub></td>
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
> Mise à jour du 25 nov. 2026 : **jusqu'au chapitre 3** ; les modules suivants recevront leurs TD et TP GE au fur et à mesure.

#### Ce que vous apprendrez

<table>
<tr><td width="50%" valign="top">✔️ Choisir une méthode adaptée à la taille et à la structure du problème</td><td width="50%" valign="top">✔️ Estimer la précision d'un résultat et reconnaître un calcul qui diverge</td></tr>
<tr><td width="50%" valign="top">✔️ Programmer ces méthodes en MATLAB et valider un schéma sur un cas test analytique</td><td width="50%" valign="top">✔️ Interpréter physiquement les conditions de stabilité (CFL, critères de convergence)</td></tr>
</table>

#### Détails à connaître

| 🎓 Public | ⏱️ Volume | 🧩 Prérequis | 💻 Logiciel | 🗣️ Langue |
|---|---|---|---|---|
| 1ʳᵉ année du Cycle d'Ingénieur Génie Énergétique (GE), FSTM | 48 h · 5 TP (TP1 à TP5) | Algèbre linéaire, analyse (développements de Taylor), bases de MATLAB | MATLAB | Français |

---

## 📚 Programme du module

Il y a **12 modules**, en trois parties précédées d'une introduction. Pour chaque module : le cours et sa vidéo
(communs), puis, quand ils sont en ligne, le TD, le TP, son corrigé, sa vidéo et ses jeux en version GE (⚡).

<sub>🔵 cours (PDF) · 🟣 TD GE · 🔴 énoncé de TP GE · 🟢 corrigé (scripts MATLAB) · 🟠 vidéo (compte UH2C) · 🟡 jeux interactifs</sub>

### 🚩 Introduction

<sub>1 module · 8 pages de cours</sub>

#### Module 00 · Introduction générale

Pourquoi le calcul numérique en mécanique, et à quoi il sert concrètement dans le métier d'ingénieur. Présentation des exemples fils conducteurs du module.

<sub>⚡ En énergétique : Quatre cas chiffrés : pompage, solaire, four, réseau.</sub>

[![📄 Cours 8 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-8%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_00_Introduction_generale/1_Cours_chapitre_00.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/18AdF62vRubU5swh_zy52d6AvmlzcVybn/view)

### 🧮 Partie I — Systèmes algébriques

<sub>4 modules · 59 pages de cours</sub>

#### Module 01 · Rappels numériques : erreurs, normes et conditionnement

Un ordinateur ne calcule jamais exactement : erreurs d'arrondi, normes vectorielles et matricielles, conditionnement d'une matrice.

<sub>⚡ En énergétique : Bilans d'énergie et rendements : soustraction de grandeurs voisines, arrondi, conditionnement d'un bilan thermique.</sub>

[![📄 Cours 13 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-13%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_01_Rappels_numeriques/1_Cours_chapitre_01.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/13uDHLzPXsp9XpujDGj60SXAgyNtyW84X/view)
[![⚡ TD GE énoncé](https://img.shields.io/badge/%E2%9A%A1%20TD%20GE-%C3%A9nonc%C3%A9-6A4C93?style=for-the-badge)](methodes-numeriques/Chapitre_01_Rappels_numeriques/GE/3_TD01_GE_enonce.pdf)

#### Module 02 · Systèmes linéaires : méthodes directes

Résolution de Ax = b en un nombre fini d'opérations — la brique de base de tout calcul par éléments finis.

<sub>⚡ En énergétique : Réseau thermique nodal d'un bâtiment multizone ; réseau hydraulique maillé.</sub>

[![📄 Cours 16 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-16%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/1_Cours_chapitre_02.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/19rK9Xc4acZQ77KQnYxwGSc7pkNBj1MKc/view)
[![⚡ TD GE énoncé](https://img.shields.io/badge/%E2%9A%A1%20TD%20GE-%C3%A9nonc%C3%A9-6A4C93?style=for-the-badge)](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/GE/3_TD02_GE_enonce.pdf)
[![⚡ TP1 GE énoncé](https://img.shields.io/badge/%E2%9A%A1%20TP1%20GE-%C3%A9nonc%C3%A9-C1121F?style=for-the-badge)](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/GE/4_TP1_GE_enonce.pdf)
[![✅ TP1 GE corrigé MATLAB](https://img.shields.io/badge/%E2%9C%85%20TP1%20GE-corrig%C3%A9%20MATLAB-2E7D32?style=for-the-badge)](methodes-numeriques/Chapitre_02_Systemes_lineaires_directs/GE/4_TP1_GE_corrige_scripts_MATLAB.zip)
[![▶ Vidéo GE TP1 · correction](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o%20GE-TP1%20%C2%B7%20correction-E67E22?style=for-the-badge)](https://drive.google.com/file/d/1QIeu_jGI170irAdK-mF8Z9z8fKToSlZc/view)
[![🎮 Jeux TP1 GE · 5 jeux](https://img.shields.io/badge/%F0%9F%8E%AE%20Jeux-TP1%20GE%20%C2%B7%205%20jeux-FFB300?style=for-the-badge)](https://janane-allah.github.io/jeux/tp1-ge/)

#### Module 03 · Systèmes linéaires : méthodes itératives

Pour les grands systèmes creux issus d'un maillage fin, là où l'élimination de Gauss coûte trop cher et détruit le caractère creux (fill-in).

<sub>⚡ En énergétique : Conduction 2D dans un four ou une plaque : grands systèmes creux (Jacobi, Gauss-Seidel, SOR).</sub>

[![📄 Cours 12 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-12%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/1_Cours_chapitre_03.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/19Q7Vj94XDHRTuFz_X4l-3xFFBQQcJwZI/view)
[![⚡ TD GE énoncé](https://img.shields.io/badge/%E2%9A%A1%20TD%20GE-%C3%A9nonc%C3%A9-6A4C93?style=for-the-badge)](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/GE/3_TD03_GE_enonce.pdf)
[![⚡ TP2 GE énoncé](https://img.shields.io/badge/%E2%9A%A1%20TP2%20GE-%C3%A9nonc%C3%A9-C1121F?style=for-the-badge)](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/GE/4_TP2_GE_enonce.pdf)
[![✅ TP2 GE corrigé MATLAB](https://img.shields.io/badge/%E2%9C%85%20TP2%20GE-corrig%C3%A9%20MATLAB-2E7D32?style=for-the-badge)](methodes-numeriques/Chapitre_03_Systemes_lineaires_iteratifs/GE/4_TP2_GE_corrige_scripts_MATLAB.zip)
[![▶ Vidéo GE TP2 · programmation](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o%20GE-TP2%20%C2%B7%20programmation-E67E22?style=for-the-badge)](https://drive.google.com/file/d/1pxjMcqifEjZVbGEjYPjbjyaYpnnEdPBp/view)
[![🎮 Jeux TP2 GE · 5 jeux](https://img.shields.io/badge/%F0%9F%8E%AE%20Jeux-TP2%20GE%20%C2%B7%205%20jeux-FFB300?style=for-the-badge)](https://janane-allah.github.io/jeux/tp2-ge/)

#### Module 04 · Systèmes non linéaires

Résoudre F(x) = 0 quand la physique cesse d'être linéaire : pertes de charge quadratiques, ressort durcissant, grandes déformations.

<sub>⚡ En énergétique : Colebrook (pertes de charge), bilan radiatif en T⁴, point de fonctionnement pompe-réseau : Newton.</sub>

[![📄 Cours 18 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-18%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_04_Systemes_non_lineaires/1_Cours_chapitre_04.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/125--JQ7p31u2xEMZVsSO3x2MCeXNOXYA/view)

### 🌡️ Partie II — EDP et différences finies

<sub>6 modules · 63 pages de cours</sub>

#### Module 05 · Généralités sur les EDP en mécanique et classification

L'inconnue n'est plus un vecteur mais un champ. Classification elliptique / parabolique / hyperbolique et conditions aux limites associées.

<sub>⚡ En énergétique : Chaleur, convection-diffusion, Poisson, ondes : un phénomène énergétique pour chaque type d'EDP.</sub>

[![📄 Cours 10 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-10%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_05_Generalites_EDP/1_Cours_chapitre_05.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/1wxEG6bzlLQPGz-evjzRmrmuqnVQsqqgs/view)

#### Module 06 · Principe de la méthode des différences finies

L'étape décisive : remplacer les dérivées, objets continus, par des quantités calculables sur ordinateur.

<sub>⚡ En énergétique : Paroi de four (fil rouge), ailette : de l'équation au système A T = b.</sub>

[![📄 Cours 10 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-10%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_06_Principe_differences_finies/1_Cours_chapitre_06.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/1F-IuYtpVuRNhaj7w13zxnSUldtZj1PoB/view)

#### Module 07 · Consistance, stabilité, convergence

Pourquoi un schéma parfaitement construit sur le papier peut produire des résultats absurdes — des oscillations qui grandissent jusqu'à faire déborder les calculs.

<sub>⚡ En énergétique : Seuil r ≤ 1/2 sur la paroi réfractaire ; CFL pour le transport de chaleur par un fluide.</sub>

[![📄 Cours 10 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-10%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_07_Consistance_stabilite_convergence/1_Cours_chapitre_07.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/1AT_64YZW3ebVt21abcGkxcZUoLHFnnkg/view)

#### Module 08 · Équation de la chaleur

Un problème physique résolu de bout en bout : la paroi de four en régime transitoire, de l'état initial jusqu'à l'équilibre.

<sub>⚡ En énergétique : Paroi, ailette, stockage thermique ; schémas explicite, implicite, θ.</sub>

[![📄 Cours 11 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-11%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_08_Equation_chaleur/1_Cours_chapitre_08.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/18wNa17e4CPXprrvWbSh1HTMUlAU2F5dD/view)

#### Module 09 · Équation de Laplace-Poisson et advection-diffusion

Discrétisation 2D complète (Dirichlet puis Neumann), validation sur un cas test analytique, puis introduction de l'advection-diffusion.

<sub>⚡ En énergétique : Champ de température d'un bâtiment (2D) ; échangeur et nombre de Péclet.</sub>

[![📄 Cours 11 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-11%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_09_Laplace_Poisson_advection/1_Cours_chapitre_09.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/1YinQ_oHGrndBm2nsGVBWTBDI62pUBbBE/view)

#### Module 10 · Équation des ondes

La corde vibrante et sa condition de stabilité — la condition CFL, avec son interprétation géométrique remarquable.

<sub>⚡ En énergétique : Vibrations de tuyauteries et d'aubes ; acoustique d'un conduit.</sub>

[![📄 Cours 11 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-11%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_10_Equation_ondes/1_Cours_chapitre_10.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/1IQh3d69BFptw47AmVj_zgeMaxRPnpFTB/view)

### 📈 Partie III — Équations différentielles ordinaires

<sub>1 module · 14 pages de cours</sub>

#### Module 11 · Résolution numérique des équations différentielles ordinaires

L'évolution temporelle des systèmes à nombre fini de degrés de liberté : oscillateurs, mécanismes, circuits équivalents.

<sub>⚡ En énergétique : Dynamique thermique d'un four ou d'un ballon de stockage ; raideur et choix du pas.</sub>

[![📄 Cours 14 pages](https://img.shields.io/badge/%F0%9F%93%84%20Cours-14%20pages-0056D2?style=for-the-badge)](methodes-numeriques/Chapitre_11_EDO_Euler_Runge_Kutta/1_Cours_chapitre_11.pdf)
[![▶ Vidéo cours](https://img.shields.io/badge/%E2%96%B6%20Vid%C3%A9o-cours-E67E22?style=for-the-badge)](https://drive.google.com/file/d/1OZqZkwXP--N1ZcmgipRbnzRsleo4AnD8/view)

---

## 🎮 Jeux interactifs

Des jeux, dans le navigateur, pour **manipuler un TP avant de le programmer**. Tous les nombres affichés sont calculés
en direct par le code MATLAB du TP, porté ligne pour ligne en JavaScript : ce sont les mêmes que dans MATLAB.

### TP1 GE · Module 02 — le réseau thermique d'un bâtiment (méthodes directes)

<table>
<tr>
<td width="33%" valign="top" align="center"><a href="https://janane-allah.github.io/jeux/tp1-ge/#jeu-1"><img src="methodes-numeriques/images/jeux-tp1-ge/jeu-1.jpg" width="100%" alt="Jeu 1 : Le réseau thermique"></a><br/><b>1 · Le réseau thermique</b><br/><sub>Assembler G, local voisin chauffé, zone isolée</sub><br/><a href="https://janane-allah.github.io/jeux/tp1-ge/#jeu-1"><img src="https://img.shields.io/badge/%E2%96%B6%20Jouer-FFB300?style=for-the-badge" alt="Jouer"></a></td>
<td width="33%" valign="top" align="center"><a href="https://janane-allah.github.io/jeux/tp1-ge/#jeu-2"><img src="methodes-numeriques/images/jeux-tp1-ge/jeu-2.jpg" width="100%" alt="Jeu 2 : Gauss pas à pas"></a><br/><b>2 · Gauss pas à pas</b><br/><sub>Pivot partiel, multiplicateurs, remontée</sub><br/><a href="https://janane-allah.github.io/jeux/tp1-ge/#jeu-2"><img src="https://img.shields.io/badge/%E2%96%B6%20Jouer-FFB300?style=for-the-badge" alt="Jouer"></a></td>
<td width="33%" valign="top" align="center"><a href="https://janane-allah.github.io/jeux/tp1-ge/#jeu-3"><img src="methodes-numeriques/images/jeux-tp1-ge/jeu-3.jpg" width="100%" alt="Jeu 3 : Le compteur d'opérations"></a><br/><b>3 · Le compteur d'opérations</b><br/><sub>n³/3 pour Gauss, n² par scénario de chauffage</sub><br/><a href="https://janane-allah.github.io/jeux/tp1-ge/#jeu-3"><img src="https://img.shields.io/badge/%E2%96%B6%20Jouer-FFB300?style=for-the-badge" alt="Jouer"></a></td>
</tr>
<tr>
<td width="33%" valign="top" align="center"><a href="https://janane-allah.github.io/jeux/tp1-ge/#jeu-4"><img src="methodes-numeriques/images/jeux-tp1-ge/jeu-4.jpg" width="100%" alt="Jeu 4 : Les messages d'erreur"></a><br/><b>4 · Les messages d'erreur</b><br/><sub>Huit vrais messages de MATLAB</sub><br/><a href="https://janane-allah.github.io/jeux/tp1-ge/#jeu-4"><img src="https://img.shields.io/badge/%E2%96%B6%20Jouer-FFB300?style=for-the-badge" alt="Jouer"></a></td>
<td width="33%" valign="top" align="center"><a href="https://janane-allah.github.io/jeux/tp1-ge/#jeu-5"><img src="methodes-numeriques/images/jeux-tp1-ge/jeu-5.jpg" width="100%" alt="Jeu 5 : Détective du code"></a><br/><b>5 · Détective du code</b><br/><sub>Les bugs silencieux et le résidu</sub><br/><a href="https://janane-allah.github.io/jeux/tp1-ge/#jeu-5"><img src="https://img.shields.io/badge/%E2%96%B6%20Jouer-FFB300?style=for-the-badge" alt="Jouer"></a></td>
<td width="33%" valign="top">🏆 <b>Comment jouer</b><br/><br/>💻📱 Sur ordinateur ou sur téléphone, sans installation ni compte.<br/><br/>⭐ Jusqu'à 3 étoiles par jeu ; la progression reste dans votre navigateur.<br/><br/>💡 Jouez <b>après</b> avoir lu l'énoncé et <b>avant</b> d'écrire votre code MATLAB.</td>
</tr>
</table>

### TP2 GE · Module 03 — la paroi d'une étuve (méthodes itératives)

<table>
<tr>
<td width="33%" valign="top" align="center"><a href="https://janane-allah.github.io/jeux/tp2-ge/#jeu-1"><img src="methodes-numeriques/images/jeux-tp2-ge/jeu-1.jpg" width="100%" alt="Jeu 1 : Jacobi contre Gauss-Seidel"></a><br/><b>1 · Jacobi contre Gauss-Seidel</b><br/><sub>La course, ρ_GS = ρ_J², le flux de chaleur</sub><br/><a href="https://janane-allah.github.io/jeux/tp2-ge/#jeu-1"><img src="https://img.shields.io/badge/%E2%96%B6%20Jouer-FFB300?style=for-the-badge" alt="Jouer"></a></td>
<td width="33%" valign="top" align="center"><a href="https://janane-allah.github.io/jeux/tp2-ge/#jeu-2"><img src="methodes-numeriques/images/jeux-tp2-ge/jeu-2.jpg" width="100%" alt="Jeu 2 : La paroi s'affine"></a><br/><b>2 · La paroi s'affine</b><br/><sub>Le nombre d'itérations quand n augmente</sub><br/><a href="https://janane-allah.github.io/jeux/tp2-ge/#jeu-2"><img src="https://img.shields.io/badge/%E2%96%B6%20Jouer-FFB300?style=for-the-badge" alt="Jouer"></a></td>
<td width="33%" valign="top" align="center"><a href="https://janane-allah.github.io/jeux/tp2-ge/#jeu-3"><img src="methodes-numeriques/images/jeux-tp2-ge/jeu-3.jpg" width="100%" alt="Jeu 3 : La chasse au ω*"></a><br/><b>3 · La chasse au ω*</b><br/><sub>SOR, formule de Young, courbe asymétrique</sub><br/><a href="https://janane-allah.github.io/jeux/tp2-ge/#jeu-3"><img src="https://img.shields.io/badge/%E2%96%B6%20Jouer-FFB300?style=for-the-badge" alt="Jouer"></a></td>
</tr>
<tr>
<td width="33%" valign="top" align="center"><a href="https://janane-allah.github.io/jeux/tp2-ge/#jeu-4"><img src="methodes-numeriques/images/jeux-tp2-ge/jeu-4.jpg" width="100%" alt="Jeu 4 : Incrément ou erreur ?"></a><br/><b>4 · Incrément ou erreur ?</b><br/><sub>Le critère d'arrêt et le facteur ρ/(1 − ρ)</sub><br/><a href="https://janane-allah.github.io/jeux/tp2-ge/#jeu-4"><img src="https://img.shields.io/badge/%E2%96%B6%20Jouer-FFB300?style=for-the-badge" alt="Jouer"></a></td>
<td width="33%" valign="top" align="center"><a href="https://janane-allah.github.io/jeux/tp2-ge/#jeu-5"><img src="methodes-numeriques/images/jeux-tp2-ge/jeu-5.jpg" width="100%" alt="Jeu 5 : Détective du code"></a><br/><b>5 · Détective du code</b><br/><sub>Avertissements, ω périmé, étuve à l'envers</sub><br/><a href="https://janane-allah.github.io/jeux/tp2-ge/#jeu-5"><img src="https://img.shields.io/badge/%E2%96%B6%20Jouer-FFB300?style=for-the-badge" alt="Jouer"></a></td>
<td width="33%" valign="top">🏆 <b>Comment jouer</b><br/><br/>💻📱 Sur ordinateur ou sur téléphone, sans installation ni compte.<br/><br/>⭐ Jusqu'à 3 étoiles par jeu ; la progression reste dans votre navigateur.<br/><br/>💡 Jouez <b>après</b> avoir lu l'énoncé et <b>avant</b> d'écrire votre code MATLAB.</td>
</tr>
</table>

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
s'intitule *Introduction aux méthodes numériques* (48 h, cinq TP) ; ses TD, ses TP et ses jeux sont propres au GE. La page de la
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
