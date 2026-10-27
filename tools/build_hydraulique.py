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

TPL = u"""<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=3500&pause=1000&color=2E86AB&center=true&vCenter=true&width=780&lines=Syst%C3%A8mes+Hydrauliques;Licence+Professionnelle+IMPI+%E2%80%94+ENSAM+Casablanca;Module+6+%3A+Hydraulique+%C2%B7+5+chapitres" alt="Systemes Hydrauliques" />

**Pr. Mohamed JANANE ALLAH**, PhD<br/>
École Nationale Supérieure d'Arts et Métiers (ENSAM) — Casablanca

🎓 **Public :** Licence Professionnelle Universitaire *Ingénierie Mécanique et Productique Industrielle* (IMPI)

<br/>

![Formation](https://img.shields.io/badge/Licence_Pro-IMPI-2E86AB?style=for-the-badge)
![Module](https://img.shields.io/badge/Module_6-Hydraulique-4C9A2A?style=for-the-badge)
![Chapitres](https://img.shields.io/badge/Chapitres_en_ligne-%(publies)s_%%2F_5-E67E22?style=for-the-badge)

[**Plan du module**](#-plan-du-module) · [**Prérequis et évaluation**](#-prérequis-et-évaluation) · [**Contact**](#-contact)

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

%(plan)s

> 📘 Les chapitres sont publiés au fur et à mesure ; 🚧 signale un chapitre pas encore en ligne.

<details>
<summary><i>Descriptif des chapitres publiés</i></summary>
<br/>

%(descriptif)s
</details>

---

## 🧭 Prérequis et évaluation

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
          .replace("%(publies)s", str(len(publies)))
io.open(os.path.join(ROOT, PAGE), "w", encoding="utf-8", newline="\n").write(page)
print("OK - %s : %d lignes, %d/%d chapitre(s) publie(s)" % (PAGE, page.count("\n"), len(publies), len(CH)))
