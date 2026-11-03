[⬅ Profil](../README.md) › Enseignement › Travaux pratiques › **Électricité**

<div align="center">

<img src="tp-electricite/images/bandeau.jpg" alt="Montages du TP d'électricité : sphères métalliques et haute tension, oscilloscope et bobine, transformateur" width="100%" />

# ⚡ Travaux pratiques d'électricité

**Modules P121 / P221 « Électricité »** · Tronc commun, 1<sup>re</sup> année · Semestres S1 et S2<br/>
Faculté des Sciences et Techniques de Mohammedia — Université Hassan II de Casablanca · Année universitaire 2025 – 2026

[![📥 Manuel de TP PDF · 25 pages](https://img.shields.io/badge/%F0%9F%93%A5%20Manuel%20de%20TP-PDF%20%C2%B7%2025%20pages-2E7D32?style=for-the-badge)](tp-electricite/Manuel_TP_Electricite_2025_2026.pdf)

<table>
<tr>
<td align="center" width="25%"><b>🔬 3 TP</b><br><sub>en salle de TP</sub></td>
<td align="center" width="25%"><b>🧑‍🎓 1<sup>re</sup> année</b><br><sub>GI · GESE · GP · MSD</sub></td>
<td align="center" width="25%"><b>📅 S1 + S2</b><br><sub>P121 · P221</sub></td>
<td align="center" width="25%"><b>📄 25 pages</b><br><sub>théorie et manipulations</sub></td>
</tr>
</table>

[**Les TP**](#-les-trois-tp) · [**Avant la séance**](#-avant-la-séance) · [**Mesures et incertitudes**](#-mesures-et-incertitudes) · [**Le compte rendu**](#-le-compte-rendu) · [**Équipe**](#-équipe-pédagogique)

</div>

---

## 🔬 Les trois TP

Trois expériences fondamentales d'électrocinétique, d'électromagnétisme et d'électrostatique. Chaque TP commence par un rappel de théorie, puis détaille la manipulation et les tableaux de mesures à remplir.

<table>
<tr>
<td width="33%" valign="top"><img src="tp-electricite/images/tp1-transformateur.jpg" width="100%" alt="TP1 : Étude d'un transformateur"><br/><b>TP1 · Étude d'un transformateur</b><br/><sub>Vérifier les lois des tensions et des intensités, puis calculer le rendement et les pertes (à vide et en charge) d'un transformateur monophasé.</sub><br/><br/><code>rapport de transformation m = N₂/N₁</code> · <code>loi des intensités</code> · <code>pertes Joule et pertes fer</code> · <code>rendement ρ = P₂/P₁</code><br/><br/><sub>📄 pages 7 – 13 du manuel</sub></td>
<td width="33%" valign="top"><img src="tp-electricite/images/tp2-faraday.jpg" width="100%" alt="TP2 : Vérification de la loi de Faraday"><br/><b>TP2 · Vérification de la loi de Faraday</b><br/><sub>Mesurer l'inductance propre et la résistance d'une bobine à la résonance, puis vérifier la loi de Faraday avec un signal triangulaire.</sub><br/><br/><code>induction électromagnétique</code> · <code>résonance LC : LCω₀² = 1</code> · <code>U<sub>L</sub> = ri + L di/dt</code> · <code>oscilloscope</code><br/><br/><sub>📄 pages 14 – 17 du manuel</sub></td>
<td width="33%" valign="top"><img src="tp-electricite/images/tp3-spheres.jpg" width="100%" alt="TP3 : Capacité des sphères métalliques et d'un condensateur sphérique"><br/><b>TP3 · Capacité des sphères métalliques et d'un condensateur sphérique</b><br/><sub>Mesurer la capacité de sphères de diamètres différents et d'un condensateur sphérique, et comparer à la théorie.</sub><br/><br/><code>C = Q/ΔV</code> · <code>sphère isolée : C = 4πε₀R</code> · <code>condensateur sphérique</code> · <code>moindres carrés</code><br/><br/><sub>📄 pages 18 – 24 du manuel</sub></td>
</tr>
</table>

<div align="center">

[![📥 Télécharger le manuel les 3 TP · 25 pages](https://img.shields.io/badge/%F0%9F%93%A5%20T%C3%A9l%C3%A9charger%20le%20manuel-les%203%20TP%20%C2%B7%2025%20pages-2E7D32?style=for-the-badge)](tp-electricite/Manuel_TP_Electricite_2025_2026.pdf)

</div>

**Matériel utilisé :** multimètres (voltmètre, ampèremètre) · générateur de tension sinusoïdale et générateur de signaux · oscilloscope · transformateur démontable (N₁ = 500, N₂ = 1000 spires) · bobine, boîte de condensateurs, résistances · alimentation haute tension 10 kV et amplificateur de mesure · sphères conductrices et hémisphères de Cavendish.

---

## 🦺 Avant la séance

<table>
<tr>
<td width="33%" valign="top"><b>Avant la manipulation</b><br/>• Vérifier câbles et connexions ; ne jamais utiliser de matériel endommagé.<br/>• Paillasse propre, sèche et dégagée.<br/>• Outils isolés ; lunettes et gants si nécessaire.</td>
<td width="33%" valign="top"><b>Pendant la manipulation</b><br/>• Ne jamais modifier un montage sous tension : couper l'alimentation d'abord.<br/>• Suivre le protocole, sans expérience non prévue.<br/>• Surveiller disjoncteurs et fusibles.</td>
<td width="33%" valign="top"><b>En cas d'incident</b><br/>• Couper immédiatement l'alimentation générale.<br/>• Prévenir l'enseignant responsable.<br/>• Savoir où sont les extincteurs et la trousse de secours.</td>
</tr>
</table>

> ⚡ **TP3 : haute tension (10 kV).** Ne touchez jamais les sphères pendant les mesures, déchargez-les avant chaque mesure et n'appliquez jamais la haute tension à l'entrée de l'amplificateur.

---

## 📏 Mesures et incertitudes

Le manuel rappelle, avant les TP, comment évaluer la fiabilité d'un résultat :

- **Type A (statistique)**, pour $n$ mesures : écart-type $\sigma_x = \sqrt{\frac{1}{n-1}\sum (x_i-\bar{x})^2}$ et incertitude sur la moyenne $u(\bar{x}) = \sigma_x/\sqrt{n}$.
- **Type B (appareil)**, classe $p$ et calibre $C$ : $u_B = \dfrac{p \times C}{100\sqrt{3}}$.
- **Propagation** : sommes et différences, $u_c = \sqrt{u^2(x)+u^2(y)}$ ; produits et quotients, $\dfrac{u_c}{f} = \sqrt{\left(\dfrac{u(x)}{x}\right)^2+\left(\dfrac{u(y)}{y}\right)^2}$.
- **Présentation** : $Q = (\text{valeur} \pm \text{incertitude})\ \text{unité}$, par exemple $R = (150 \pm 2)\ \Omega$.

Exemple du TP1 : pour le rapport de transformation $m = U_2/U_1$, $\dfrac{\Delta m}{m} = \sqrt{\left(\dfrac{\Delta U_1}{U_1}\right)^2+\left(\dfrac{\Delta U_2}{U_2}\right)^2}$.

---

## 📝 Le compte rendu

| ✅ À faire | Pourquoi |
|---|---|
| Au moins **3 mesures** par grandeur | réduire les erreurs aléatoires (type A) |
| Noter la **classe et le calibre** de chaque appareil | calculer l'incertitude de type B |
| **Détailler** les calculs d'incertitude | montrer d'où vient chaque barre d'erreur |
| **Comparer** mesure et théorie, incertitudes comprises | conclure honnêtement : accord ou écart significatif |
| Tracer les droites **ΔV = f(U)** (TP3) par les moindres carrés | en déduire la pente, puis la capacité |

🎯 **Compétences visées :** manipuler multimètres, oscilloscopes et générateurs ; interpréter les phénomènes observés ; calculer des incertitudes ; rédiger un compte rendu scientifique structuré. Les trois règles d'or : **sécurité, rigueur, ponctualité**.

---

## 👥 Équipe pédagogique

| Intervenants | Public | Département |
|---|---|---|
| Pr. Mohamed JANANE ALLAH<br/>Pr. Zouhaire SOFIANI<br/>Pr. Toufique TBATOU | 1<sup>re</sup> année FST : Génie Informatique (GI) · Génie Électronique et Systèmes Embarqués (GESE) · Génie des Procédés (GP) · Mathématiques et Science des Données (MSD) | Physique — FSTM |

📚 Autres enseignements : [Méthodes numériques pour la mécanique](licence-genie-mecanique.md) (LST GM · Cycle Ingénieur GE, FSTM) · [Systèmes hydrauliques](licence-pro-hydraulique.md) (Licence Pro IMPI, ENSAM Casablanca)

---

<div align="center">

[![Email](https://img.shields.io/badge/mohamedjanane147@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mohamedjanane147@gmail.com)
[![Site](https://img.shields.io/badge/janane--allah.github.io-0A66C2?style=flat-square&logo=github-pages&logoColor=white)](https://janane-allah.github.io)
[![Retour au profil](https://img.shields.io/badge/⬅_Retour_au_profil-555555?style=flat-square)](../README.md)

<sub>Page générée par <code>tools/build_tp_electricite.py</code> · Université Hassan II de Casablanca — FSTM</sub>

</div>
