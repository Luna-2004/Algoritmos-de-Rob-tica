#Dibuje el nombre de cada uno de los integrantes del grupo en un plot en 2D, teniendo en cuenta 
#líneas rectas y/o curvas.

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties

# Lista de integrantes del grupo: (nombre, posición vertical)
NOMBRES = [
    ("LUNA STEPHANIE MAHECHA ALARCON", 0),
    ("JULIETH MARLEN DIAZ VELOZA", 1.5),
    ("SANTIAGO FONSECA HURTADO", 2.5),
    ("FELIPE FONSECA HURTADO", 3.5),
    ("ANDRES SANTIAGO CARRILLO CABALLERO", 4.5),
    ("MADELEYNY ALAYON", 5.5)
]

def dibujar_nombre(ax, texto, y_offset, color):
    fp = FontProperties(family="DejaVu Sans", style="italic", weight="bold")
    path = TextPath((0, y_offset), texto, size=1, prop=fp)

    vertices = path.vertices
    codes = path.codes

    # Separar el path en subtrayectorias (cada letra puede tener varias)
    x_actual, y_actual = [], []
    for v, c in zip(vertices, codes):
        if c == path.MOVETO and x_actual:
            ax.plot(x_actual, y_actual, color=color, linewidth=2)
            x_actual, y_actual = [], []
        x_actual.append(v[0])
        y_actual.append(v[1])
    if x_actual:
        ax.plot(x_actual, y_actual, color=color, linewidth=2)

def main():
    fig, ax = plt.subplots(figsize=(10, 6))

    colores = ["steelblue", "firebrick", "seagreen", "darkorange", "purple"]
    for i, (nombre, y_off) in enumerate(NOMBRES):
        dibujar_nombre(ax, nombre, y_off, colores[i % len(colores)])

    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Nombres del grupo dibujados con líneas y curvas", fontsize=13)

    plt.tight_layout()
    plt.savefig("nombres_2D.png", dpi=150)
    plt.show()

if __name__ == "__main__":
    main()
