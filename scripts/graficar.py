#!/usr/bin/env python3
"""Gráfica de la membresía total por año, apilada por clase de membresía.

Lee data/resumen-por-anio.csv y escribe figuras/membresia-por-anio-{claro,oscuro}.png
"""
import csv
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

RAIZ = Path(__file__).resolve().parent.parent
CLASES = ["Titular", "Honorario", "Socio Estudiante", "Socio No-Estudiante"]

# Paleta categórica de referencia, slots 1-4 (azul, naranja, aqua, amarillo).
# El orden de los slots es el mecanismo de seguridad para daltonismo: no reordenar.
TEMAS = {
    "claro": {
        "series": ["#2a78d6", "#eb6834", "#1baf7a", "#eda100"],
        "surface": "#fcfcfb",
        "text": "#0b0b0b",
        "text2": "#52514e",
        "grid": "#e3e2de",
    },
    "oscuro": {
        "series": ["#3987e5", "#d95926", "#199e70", "#c98500"],
        "surface": "#1a1a19",
        "text": "#ffffff",
        "text2": "#c3c2b7",
        "grid": "#33332f",
    },
}


def leer():
    with open(RAIZ / "data/resumen-por-anio.csv", encoding="utf-8") as fh:
        filas = list(csv.DictReader(fh))
    anios = [int(f["anio"]) for f in filas]
    series = {c: [int(f[c]) for f in filas] for c in CLASES}
    totales = [int(f["total"]) for f in filas]
    return anios, series, totales


def graficar(modo, anios, series, totales):
    t = TEMAS[modo]
    fig, ax = plt.subplots(figsize=(9, 5), dpi=200)
    fig.patch.set_facecolor(t["surface"])
    ax.set_facecolor(t["surface"])

    x = range(len(anios))
    base = [0] * len(anios)
    for clase, color in zip(CLASES, t["series"]):
        v = series[clase]
        ax.bar(x, v, bottom=base, width=0.62, label=clase, color=color,
               edgecolor=t["surface"], linewidth=1.6, zorder=3)
        # Etiqueta directa dentro del segmento: la regla de relieve exige
        # etiquetas visibles porque aqua y amarillo no alcanzan 3:1 en claro.
        for xi, (vi, bi) in enumerate(zip(v, base)):
            if vi >= 3:
                ax.text(xi, bi + vi / 2, str(vi), ha="center", va="center",
                        fontsize=8.5, color="#ffffff" if clase != "Socio No-Estudiante" else "#0b0b0b",
                        zorder=4)
        base = [b + vi for b, vi in zip(base, v)]

    for xi, total in zip(x, totales):
        ax.text(xi, total + 0.9, str(total), ha="center", va="bottom",
                fontsize=10, fontweight="semibold", color=t["text"], zorder=4)

    ax.set_title("Membresía de AstroCO por año y clase", fontsize=13,
                 color=t["text"], pad=16, loc="left")
    ax.text(0, 1.015, "UAI-Col 2018-2023  ·  sin membresía activa en 2024  ·  AstroCO/ACCEFYN 2025-2026",
            transform=ax.transAxes, fontsize=9, color=t["text2"], va="bottom")

    ax.set_xticks(list(x))
    ax.set_xticklabels([str(a) for a in anios], color=t["text2"], fontsize=10)
    ax.set_ylabel("Miembros", color=t["text2"], fontsize=10)
    ax.tick_params(axis="y", colors=t["text2"], labelsize=9, length=0)
    ax.tick_params(axis="x", length=0)
    ax.set_ylim(0, max(totales) + 5)
    ax.yaxis.grid(True, color=t["grid"], linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    for lado in ("top", "right", "left"):
        ax.spines[lado].set_visible(False)
    ax.spines["bottom"].set_color(t["grid"])

    leg = ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.09), ncol=4,
                    frameon=False, fontsize=9.5, handlelength=0.9,
                    handleheight=0.9, borderpad=0, columnspacing=1.6)
    for texto in leg.get_texts():
        texto.set_color(t["text2"])

    salida = RAIZ / f"figuras/membresia-por-anio-{modo}.png"
    salida.parent.mkdir(exist_ok=True)
    fig.savefig(salida, bbox_inches="tight", facecolor=t["surface"])
    plt.close(fig)
    print(f"escrito {salida.relative_to(RAIZ)}")


def main():
    anios, series, totales = leer()
    for modo in TEMAS:
        graficar(modo, anios, series, totales)


if __name__ == "__main__":
    main()
