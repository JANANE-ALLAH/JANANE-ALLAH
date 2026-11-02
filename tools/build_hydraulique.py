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
 "03": ("Chapitre_03_Technologie_systemes_hydrauliques", "Technologie des systèmes hydrauliques", ""),
 "04": ("Chapitre_04_Circuits_hydrauliques", "Circuits hydrauliques", ""),
 "05": ("Chapitre_05_Maintenance_installations", "Maintenance des installations", ""),
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
GALERIE = [  # (titre, colonnes, [(fichier, legende)])
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
 ("👷 Sur le terrain", 2, [
   ("terrain-groupe-sany.jpg", "Une partie du groupe devant la pelle SANY."),
   ("terrain-demontage-moteur.jpg", "Autour d'un moteur démonté, en blouse de TP."),
   ("terrain-inspection-sany.jpg", "Au pied de la flèche d'une pelle SANY : observation et discussion en petit groupe."),
   ("terrain-sur-la-machine.jpg", "Sur la machine : on pointe, on identifie, on vérifie."),
 ]),
]


def fichiers(num):
    d = os.path.join(ROOT, B, CH[num][0])
    return sorted(os.listdir(d)) if os.path.isdir(d) else []


def lien(num, f, label):
    return "[%s](%s/%s/%s)" % (label, B, CH[num][0], f)


def cellule(num, test, label):
    hits = [f for f in fichiers(num) if test(f)]
    return "<br>".join(lien(num, f, label(f)) for f in hits)


def pages(num):
    f = [x for x in fichiers(num) if x.startswith("1_")]
    if not f:
        return None
    try:
        import pypdf
        return len(pypdf.PdfReader(os.path.join(ROOT, B, CH[num][0], f[0])).pages)
    except Exception:
        return None


COLONNES = [  # (titre, fonction cellule)
    ("📄 Cours", lambda n: cellule(n, lambda f: f.startswith("1_"), lambda f: "PDF")),
    ("📝 TD", lambda n: cellule(n, lambda f: f.startswith("3_") and "corrige" not in f.lower(), lambda f: "TD")),
    ("🔬 TP", lambda n: cellule(n, lambda f: f.startswith("4_") and "corrige" not in f.lower(),
                               lambda f: f.split("_")[1])),
    ("✅ Corrigé", lambda n: cellule(n, lambda f: "corrige" in f.lower(), lambda f: "Corrigé")),
    ("🎥 Vidéo", lambda n: "[▶ Voir](%s)" % VIDEOS[n] if n in VIDEOS else ""),
]

# Le cours est toujours affiche ; les autres colonnes seulement si elles ont du contenu.
actives = [c for i, c in enumerate(COLONNES) if i == 0 or any(c[1](n) for n in CH)]
publies = [n for n in CH if COLONNES[0][1](n)]

rows = ["| # | Chapitre | %s |" % " | ".join(c[0] for c in actives),
        "|:-:|----------|%s|" % "|".join(":--------:" for _ in actives)]
for n in sorted(CH):
    cells = [c[1](n) or ("🚧 À venir" if c is actives[0] else "—") for c in actives]
    titre = CH[n][1] if n in publies else "*%s*" % CH[n][1]
    rows.append("| **%s** | %s | %s |" % (n, titre, " | ".join(cells)))
plan = "\n".join(rows)

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
    desc.append("")
descriptif = "\n".join(desc)


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
        texte += u"""**Dans l'exemple de présentation** : 18 diapositives minutées (plus une annexe et les crédits hors minutage), sur le plan Introduction · Réservoir · Filtration · Pompes · Autres composants · Circuit · Maintenance · Conclusion. Il montre comment rattacher chaque partie à un chapitre du cours et à une section du manuel de service, recouper des fiches techniques et refaire sur une machine réelle les calculs du cours (volume du réservoir, régulation de puissance, effort d'un vérin, bilan de puissance). C'est un exemple pédagogique : ses valeurs viennent de fiches publiques et sont à remplacer par les relevés de la machine étudiée ; il renvoie aux chapitres 1 à 5 du cours, dont les chapitres 3 à 5 ne sont pas encore en ligne.

"""
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
    return "\n".join(out) + "\n"


def galerie():
    """Section 'Le module en images' : grilles de photos avec legendes."""
    import html
    blocs = []
    for titre, cols, items in GALERIE:
        items = [i for i in items if fichier_image(i[0])]
        if not items:
            continue
        t = ["### %s\n" % titre, "<table>"]
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
[**Plan du module**](#-plan-du-module) · %(nav_mini)s%(nav_images)s[**Prérequis et évaluation**](#-prérequis-et-évaluation) · [**Contact**](#-contact)

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

## 📚 Plan du module

%(parcours)s%(plan)s

> 📘 Les chapitres sont publiés au fur et à mesure ; 🚧 signale un chapitre pas encore en ligne.

<details>
<summary><i>Descriptif des chapitres publiés</i></summary>
<br/>

%(descriptif)s
</details>

---

%(mini)s%(galerie)s## 🧭 Prérequis et évaluation

| | |
|---|---|
| **Prérequis** | Mécanique générale (forces, travail, puissance) et mathématiques de base — aucun acquis en hydraulique n'est supposé. |
| **Niveau** | Débutant → intermédiaire. |
| **Évaluation** | QCM d'auto-évaluation en fin de chapitre, TD corrigés, manipulations en TP. |
| **TP** | Sur banc d'essai : le repère **TP** en haut à droite des diapos signale la notion que vous manipulerez sur machine. |

---

## 📫 Contact

<div align="center">

[![Email](https://img.shields.io/badge/mohamedjanane147@gmail.com-EA4335?style=flat-square&logo=gmail&logoColor=white)](mailto:mohamedjanane147@gmail.com)
[![Site](https://img.shields.io/badge/janane--allah.github.io-0A66C2?style=flat-square&logo=github-pages&logoColor=white)](https://janane-allah.github.io)

</div>
"""

page = TPL.replace("%%", "%").replace("%(plan)s", plan).replace("%(descriptif)s", descriptif) \
          .replace("%(publies)s", str(len(publies))).replace("%(mini)s", mini) \
          .replace("%(nav_mini)s", "[**Mini-projets**](#-mini-projets) · " if mini else "") \
          .replace("%(parcours)s", parcours()).replace("%(stats)s", badges_stats()) \
          .replace("%(bandeau)s", bandeau()) \
          .replace("%(nav_images)s", "[**En images**](#-le-module-en-images) · " if galerie() else "") \
          .replace("%(galerie)s", galerie())
io.open(os.path.join(ROOT, PAGE), "w", encoding="utf-8", newline="\n").write(page)
print("OK - %s : %d lignes, %d/%d chapitre(s) publie(s)" % (PAGE, page.count("\n"), len(publies), len(CH)))
