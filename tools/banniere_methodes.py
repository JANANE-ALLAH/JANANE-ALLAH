# -*- coding: utf-8 -*-
# Genere les visuels de la page Methodes numeriques (a lancer une fois, ou apres un changement de texte) :
#   cours/methodes-numeriques/images/banniere.jpg  : bandeau d'en-tete, titre a gauche et, a droite, un vrai
#       calcul du cours (equation de Laplace sur une plaque, differences finies a 5 points, chapitre 9) ;
#   cours/methodes-numeriques/images/enseignant.png : monogramme de l'enseignant.
# Usage :  python tools/banniere_methodes.py      (necessite numpy, matplotlib et Pillow)
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from PIL import Image, ImageDraw, ImageFont

SORTIE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "cours", "methodes-numeriques", "images")
os.makedirs(SORTIE, exist_ok=True)

MARINE, MARINE2 = "#0B1F3A", "#14365F"
BLEU, AMBRE, GRIS = "#2E86AB", "#F2A900", "#C9D6E8"
plt.rcParams["font.family"] = ["Segoe UI", "DejaVu Sans"]


def laplace(nx=81, ny=41, tol=1e-6):
    """Plaque [0, 2] x [0, 1] : T = 100 sin(pi x / 2) sur le bord haut, 0 ailleurs ; Gauss-Seidel rouge-noir."""
    x, y = np.linspace(0, 2, nx), np.linspace(0, 1, ny)
    T = np.zeros((ny, nx))
    T[-1, :] = 100 * np.sin(np.pi * x / 2)
    rouge = (np.add.outer(np.arange(ny), np.arange(nx)) % 2 == 0)[1:-1, 1:-1]
    for it in range(20000):
        ancien = T.copy()
        for masque in (rouge, ~rouge):
            moy = 0.25 * (T[1:-1, :-2] + T[1:-1, 2:] + T[:-2, 1:-1] + T[2:, 1:-1])
            interieur = T[1:-1, 1:-1]
            interieur[masque] = moy[masque]
        if np.abs(T - ancien).max() < tol:
            break
    exact = 100 * np.outer(np.sinh(np.pi * y / 2) / np.sinh(np.pi / 2), np.sin(np.pi * x / 2))
    print("Laplace : %d iterations, ecart max a la solution exacte %.3f" % (it + 1, np.abs(T - exact).max()))
    return x, y, T


def banniere():
    x, y, T = laplace()
    fig = plt.figure(figsize=(16, 5), dpi=100)
    fond = fig.add_axes([0, 0, 1, 1])
    fond.imshow(np.linspace(0, 1, 256)[None, :], aspect="auto", extent=[0, 1, 0, 1],
                cmap=LinearSegmentedColormap.from_list("fond", [MARINE, MARINE2]))
    fond.axis("off")

    fig.text(0.045, 0.80, "FSTM  ·  UNIVERSITÉ HASSAN II DE CASABLANCA", color=AMBRE, fontsize=14, fontweight="bold")
    fig.text(0.045, 0.56, "Méthodes numériques", color="white", fontsize=44, fontweight="bold")
    fig.text(0.045, 0.39, "pour la mécanique", color="white", fontsize=44, fontweight="bold")
    fig.text(0.045, 0.24, "LST Génie Mécanique  ·  1re année Cycle Ingénieur Génie Énergétique",
             color=GRIS, fontsize=15)
    fig.text(0.045, 0.11, "Pr. Mohamed JANANE ALLAH   |   12 chapitres  ·  TD  ·  TP MATLAB",
             color="white", fontsize=15)

    ax = fig.add_axes([0.575, 0.13, 0.385, 0.77])
    ax.imshow(T, origin="lower", extent=[0, 2, 0, 1], cmap="inferno", vmin=0, vmax=100, aspect="auto")
    ax.contour(x, y, T, levels=np.arange(10, 100, 10), colors="white", linewidths=0.8, alpha=0.55)
    for xv in np.arange(0, 2.0001, 0.1):
        ax.axvline(xv, color="white", lw=0.4, alpha=0.13)
    for yv in np.arange(0, 1.0001, 0.1):
        ax.axhline(yv, color="white", lw=0.4, alpha=0.13)
    cx, cy, h = 1.5, 0.5, 0.1  # stencil a 5 points
    ax.plot([cx - h, cx + h], [cy, cy], color=AMBRE, lw=2)
    ax.plot([cx, cx], [cy - h, cy + h], color=AMBRE, lw=2)
    ax.plot([cx, cx - h, cx + h, cx, cx], [cy, cy, cy, cy - h, cy + h], "o", color=AMBRE, ms=7,
            markeredgecolor="white", markeredgewidth=0.8)
    ax.set_xticks([])
    ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color(BLEU)
        s.set_linewidth(1.2)
    fig.text(0.575, 0.055, "Équation de Laplace sur une plaque — différences finies, schéma à 5 points (chapitre 9)",
             color="#9FB3CC", fontsize=10)

    chemin = os.path.join(SORTIE, "banniere.png")
    fig.savefig(chemin, dpi=100)
    plt.close(fig)
    Image.open(chemin).convert("RGB").save(os.path.join(SORTIE, "banniere.jpg"), "JPEG", quality=90,
                                           optimize=True, progressive=True)
    os.remove(chemin)


def monogramme():
    n = 240
    im = Image.new("RGBA", (n * 4, n * 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.ellipse([8, 8, n * 4 - 8, n * 4 - 8], fill=MARINE2, outline=BLEU, width=28)
    try:
        f = ImageFont.truetype("segoeuib.ttf", 300)
    except Exception:
        f = ImageFont.load_default()
    d.text((n * 2, n * 2), "MJA", anchor="mm", fill="white", font=f)
    im.resize((n, n), Image.LANCZOS).save(os.path.join(SORTIE, "enseignant.png"), optimize=True)


banniere()
monogramme()
print("OK -", ", ".join(sorted(os.listdir(SORTIE))))
