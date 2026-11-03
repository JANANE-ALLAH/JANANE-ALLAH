# -*- coding: utf-8 -*-
# Genere cours/tp-electricite.md (travaux pratiques d'electricite, FSTM) a partir du manuel PDF
# range dans cours/tp-electricite/.  Usage :  python tools/build_tp_electricite.py
# Les images (bandeau, une vignette par TP) sont extraites une fois du PDF : supprimer une image pour la refaire.
import io, os
from urllib.parse import quote

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cours")
D = "tp-electricite"
PDF = "Manuel_TP_Electricite_2025_2026.pdf"
IMG = "images"
ANNEE = "2025 – 2026"
INTERVENANTS = ["Pr. Mohamed JANANE ALLAH", "Pr. Zouhaire SOFIANI", "Pr. Toufique TBATOU"]
PARCOURS = ["Génie Informatique (GI)", "Génie Électronique et Systèmes Embarqués (GESE)", "Génie des Procédés (GP)",
            "Mathématiques et Science des Données (MSD)"]

# (numero, titre, buts, notions, pages du manuel, image : (xref de l'image dans le PDF, fichier))
TPS = [
 (1, "Étude d'un transformateur", "Vérifier les lois des tensions et des intensités, puis calculer le rendement et les pertes (à vide et en charge) d'un transformateur monophasé.",
  ["rapport de transformation m = N₂/N₁", "loi des intensités", "pertes Joule et pertes fer", "rendement ρ = P₂/P₁"], "7 – 13", (64, "tp1-transformateur.jpg")),
 (2, "Vérification de la loi de Faraday", "Mesurer l'inductance propre et la résistance d'une bobine à la résonance, puis vérifier la loi de Faraday avec un signal triangulaire.",
  ["induction électromagnétique", "résonance LC : LCω₀² = 1", "U<sub>L</sub> = ri + L di/dt", "oscilloscope"], "14 – 17", (96, "tp2-faraday.jpg")),
 (3, "Capacité des sphères métalliques et d'un condensateur sphérique", "Mesurer la capacité de sphères de diamètres différents et d'un condensateur sphérique, et comparer à la théorie.",
  ["C = Q/ΔV", "sphère isolée : C = 4πε₀R", "condensateur sphérique", "moindres carrés"], "18 – 24", (122, "tp3-spheres.jpg")),
]
MATERIEL = ["multimètres (voltmètre, ampèremètre)", "générateur de tension sinusoïdale et générateur de signaux", "oscilloscope",
            "transformateur démontable (N₁ = 500, N₂ = 1000 spires)", "bobine, boîte de condensateurs, résistances",
            "alimentation haute tension 10 kV et amplificateur de mesure", "sphères conductrices et hémisphères de Cavendish"]


def preparer_images():
    """Bandeau (collage de la couverture) et une image par TP, tirees du PDF, sans metadonnees."""
    dossier = os.path.join(ROOT, D, IMG)
    os.makedirs(dossier, exist_ok=True)
    besoins = [(7, "bandeau.jpg", 1600)] + [(t[5][0], t[5][1], 1200) for t in TPS]
    if all(os.path.exists(os.path.join(dossier, f)) for _, f, _ in besoins):
        return
    import pymupdf
    from PIL import Image
    doc = pymupdf.open(os.path.join(ROOT, D, PDF))
    for xref, nom, largeur in besoins:
        chemin = os.path.join(dossier, nom)
        if os.path.exists(chemin):
            continue
        im = Image.open(io.BytesIO(doc.extract_image(xref)["image"])).convert("RGB")
        if nom != "bandeau.jpg":                          # carte : image entiere, centree sur fond blanc 2:1
            k = min(largeur * 0.94 / im.width, largeur * 0.47 / im.height)
            im = im.resize((round(im.width * k), round(im.height * k)), Image.LANCZOS)
            fond = Image.new("RGB", (largeur, largeur // 2), (255, 255, 255))
            fond.paste(im, ((fond.width - im.width) // 2, (fond.height - im.height) // 2))
            im = fond
        elif im.width > largeur:
            im = im.resize((largeur, round(im.height * largeur / im.width)), Image.LANCZOS)
        im.save(chemin, "JPEG", quality=85, optimize=True, progressive=True)   # sans exif


def badge(libelle, message, couleur, url, logo=""):
    q = lambda t: quote(t.replace("-", "--").replace("_", "__"), safe="")
    return "[![%s %s](https://img.shields.io/badge/%s-%s-%s?style=for-the-badge%s)](%s)" % (
        libelle, message, q(libelle), q(message), couleur, "&logo=%s&logoColor=white" % logo if logo else "", url)


def pages_pdf():
    try:
        import pymupdf
        return pymupdf.open(os.path.join(ROOT, D, PDF)).page_count
    except Exception:
        return 25


def carte(t):
    n, titre, buts, notions, pages, (_, image) = t
    return ('<td width="33%%" valign="top"><img src="%s/%s/%s" width="100%%" alt="TP%d : %s"><br/>'
            '<b>TP%d · %s</b><br/><sub>%s</sub><br/><br/>%s<br/><br/><sub>📄 pages %s du manuel</sub></td>'
            % (D, IMG, image, n, titre, n, titre, buts, " · ".join("<code>%s</code>" % x for x in notions), pages))


def main():
    preparer_images()
    nb = pages_pdf(), len(TPS)
    pdf = "%s/%s" % (D, PDF)
    s = []
    s.append("[⬅ Profil](../README.md) › Enseignement › Travaux pratiques › **Électricité**\n")
    s.append('<div align="center">\n')
    s.append('<img src="%s/%s/bandeau.jpg" alt="Montages du TP d\'électricité : sphères métalliques et haute tension, oscilloscope et bobine, transformateur" width="100%%" />\n' % (D, IMG))
    s.append("# ⚡ Travaux pratiques d'électricité\n")
    s.append("**Modules P121 / P221 « Électricité »** · Tronc commun, 1<sup>re</sup> année · Semestres S1 et S2<br/>")
    s.append("Faculté des Sciences et Techniques de Mohammedia — Université Hassan II de Casablanca · Année universitaire %s\n" % ANNEE)
    s.append(badge("📥 Manuel de TP", "PDF · %d pages" % nb[0], "2E7D32", pdf) + "\n")
    s.append("<table>\n<tr>")
    for case in [("🔬 %d TP" % nb[1], "en salle de TP"), ("🧑‍🎓 1<sup>re</sup> année", "GI · GESE · GP · MSD"), ("📅 S1 + S2", "P121 · P221"), ("📄 %d pages" % nb[0], "théorie et manipulations")]:
        s.append('<td align="center" width="25%%"><b>%s</b><br><sub>%s</sub></td>' % case)
    s.append("</tr>\n</table>\n")
    s.append("[**Les TP**](#-les-trois-tp) · [**Avant la séance**](#-avant-la-séance) · [**Mesures et incertitudes**](#-mesures-et-incertitudes) · [**Le compte rendu**](#-le-compte-rendu) · [**Équipe**](#-équipe-pédagogique)\n")
    s.append("</div>\n\n---\n")

    s.append("## 🔬 Les trois TP\n")
    s.append("Trois expériences fondamentales d'électrocinétique, d'électromagnétisme et d'électrostatique. Chaque TP commence "
             "par un rappel de théorie, puis détaille la manipulation et les tableaux de mesures à remplir.\n")
    s.append("<table>\n<tr>\n" + "\n".join(carte(t) for t in TPS) + "\n</tr>\n</table>\n")
    s.append("<div align=\"center\">\n\n" + badge("📥 Télécharger le manuel", "les 3 TP · %d pages" % nb[0], "2E7D32", pdf) + "\n\n</div>\n")
    s.append("**Matériel utilisé :** " + " · ".join(MATERIEL) + ".\n\n---\n")

    s.append("## 🦺 Avant la séance\n")
    s.append("<table>\n<tr>")
    for titre, points in [("Avant la manipulation", ["Vérifier câbles et connexions ; ne jamais utiliser de matériel endommagé.", "Paillasse propre, sèche et dégagée.", "Outils isolés ; lunettes et gants si nécessaire."]),
                          ("Pendant la manipulation", ["Ne jamais modifier un montage sous tension : couper l'alimentation d'abord.", "Suivre le protocole, sans expérience non prévue.", "Surveiller disjoncteurs et fusibles."]),
                          ("En cas d'incident", ["Couper immédiatement l'alimentation générale.", "Prévenir l'enseignant responsable.", "Savoir où sont les extincteurs et la trousse de secours."])]:
        s.append('<td width="33%%" valign="top"><b>%s</b><br/>%s</td>' % (titre, "<br/>".join("• " + p for p in points)))
    s.append("</tr>\n</table>\n")
    s.append("> ⚡ **TP3 : haute tension (10 kV).** Ne touchez jamais les sphères pendant les mesures, déchargez-les avant chaque mesure "
             "et n'appliquez jamais la haute tension à l'entrée de l'amplificateur.\n\n---\n")

    s.append("## 📏 Mesures et incertitudes\n")
    s.append("Le manuel rappelle, avant les TP, comment évaluer la fiabilité d'un résultat :\n")
    s.append("- **Type A (statistique)**, pour $n$ mesures : écart-type $\\sigma_x = \\sqrt{\\frac{1}{n-1}\\sum (x_i-\\bar{x})^2}$ et incertitude sur la moyenne $u(\\bar{x}) = \\sigma_x/\\sqrt{n}$.")
    s.append("- **Type B (appareil)**, classe $p$ et calibre $C$ : $u_B = \\dfrac{p \\times C}{100\\sqrt{3}}$.")
    s.append("- **Propagation** : sommes et différences, $u_c = \\sqrt{u^2(x)+u^2(y)}$ ; produits et quotients, $\\dfrac{u_c}{f} = \\sqrt{\\left(\\dfrac{u(x)}{x}\\right)^2+\\left(\\dfrac{u(y)}{y}\\right)^2}$.")
    s.append("- **Présentation** : $Q = (\\text{valeur} \\pm \\text{incertitude})\\ \\text{unité}$, par exemple $R = (150 \\pm 2)\\ \\Omega$.\n")
    s.append("Exemple du TP1 : pour le rapport de transformation $m = U_2/U_1$, $\\dfrac{\\Delta m}{m} = \\sqrt{\\left(\\dfrac{\\Delta U_1}{U_1}\\right)^2+\\left(\\dfrac{\\Delta U_2}{U_2}\\right)^2}$.\n\n---\n")

    s.append("## 📝 Le compte rendu\n")
    s.append("| ✅ À faire | Pourquoi |\n|---|---|")
    for a, b in [("Au moins **3 mesures** par grandeur", "réduire les erreurs aléatoires (type A)"), ("Noter la **classe et le calibre** de chaque appareil", "calculer l'incertitude de type B"),
                 ("**Détailler** les calculs d'incertitude", "montrer d'où vient chaque barre d'erreur"), ("**Comparer** mesure et théorie, incertitudes comprises", "conclure honnêtement : accord ou écart significatif"),
                 ("Tracer les droites **ΔV = f(U)** (TP3) par les moindres carrés", "en déduire la pente, puis la capacité")]:
        s.append("| %s | %s |" % (a, b))
    s.append("\n🎯 **Compétences visées :** manipuler multimètres, oscilloscopes et générateurs ; interpréter les phénomènes observés ; "
             "calculer des incertitudes ; rédiger un compte rendu scientifique structuré. Les trois règles d'or : **sécurité, rigueur, ponctualité**.\n\n---\n")

    s.append("## 👥 Équipe pédagogique\n")
    s.append("| Intervenants | Public | Département |\n|---|---|---|")
    s.append("| %s | 1<sup>re</sup> année FST : %s | Physique — FSTM |\n" % ("<br/>".join(INTERVENANTS), " · ".join(PARCOURS)))
    s.append("📚 Autres enseignements : [Méthodes numériques pour la mécanique](licence-genie-mecanique.md) (LST GM · Cycle Ingénieur GE, FSTM) · "
             "[Systèmes hydrauliques](licence-pro-hydraulique.md) (Licence Pro IMPI, ENSAM Casablanca)\n\n---\n")
    s.append('<div align="center">\n')
    s.append("[![Email](https://img.shields.io/badge/mohamedjanane147@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mohamedjanane147@gmail.com)")
    s.append("[![Site](https://img.shields.io/badge/janane--allah.github.io-0A66C2?style=flat-square&logo=github-pages&logoColor=white)](https://janane-allah.github.io)")
    s.append("[![Retour au profil](https://img.shields.io/badge/⬅_Retour_au_profil-555555?style=flat-square)](../README.md)\n")
    s.append("<sub>Page générée par <code>tools/build_tp_electricite.py</code> · Université Hassan II de Casablanca — FSTM</sub>\n")
    s.append("</div>\n")
    page = "\n".join(s)
    io.open(os.path.join(ROOT, "tp-electricite.md"), "w", encoding="utf-8", newline="\n").write(page)
    print("OK - %d lignes" % page.count("\n"))


main()
