#!/usr/bin/env python3
"""Construye la membresía año por año a partir de los archivos de data/fuente-*.csv.

Genera:
  data/membresia-por-anio.csv  formato largo: una fila por (persona, año)
  data/resumen-por-anio.csv    conteos por año y clase
  RESUMEN.md                   la misma tabla en Markdown
"""
import csv
from collections import defaultdict
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CLASES = ["Titular", "Honorario", "Socio Estudiante", "Socio No-Estudiante"]
FUENTES = {
    "data/fuente-2018-2023.csv": "UAI-Col 2018-2023",
    "data/fuente-2025-2026.csv": "AstroCO/ACCEFYN 2025-2026",
}


def leer():
    filas = []
    for ruta, etiqueta in FUENTES.items():
        for r in csv.DictReader(open(RAIZ / ruta, encoding="utf-8")):
            anios = [a for a in r["anios"].split(";") if a]
            for anio in anios:
                filas.append({
                    "anio": int(anio),
                    "clase": r["clase"],
                    "nombre": r["nombre"],
                    "institucion": r.get("institucion", "") or "",
                    "fuente": etiqueta,
                })
            if not anios:
                print(f"  aviso: sin años -> {r['nombre']} ({etiqueta})")
    return sorted(filas, key=lambda f: (f["anio"], CLASES.index(f["clase"]), f["nombre"]))


def main():
    filas = leer()
    with open(RAIZ / "data/membresia-por-anio.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["anio", "clase", "nombre", "institucion", "fuente"])
        w.writeheader()
        w.writerows(filas)

    conteo = defaultdict(int)
    for f in filas:
        conteo[(f["anio"], f["clase"])] += 1
    anios = sorted({f["anio"] for f in filas})
    anios = list(range(min(anios), max(anios) + 1))  # incluye los años sin miembros

    with open(RAIZ / "data/resumen-por-anio.csv", "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["anio"] + CLASES + ["total"])
        for a in anios:
            fila = [conteo[(a, c)] for c in CLASES]
            w.writerow([a] + fila + [sum(fila)])

    md = ["# Membresía año por año", "",
          "Generado por `scripts/construir.py`. No editar a mano.", "",
          "| Año | " + " | ".join(CLASES) + " | Total |",
          "|---|" + "---|" * (len(CLASES) + 1)]
    for a in anios:
        fila = [conteo[(a, c)] for c in CLASES]
        md.append(f"| {a} | " + " | ".join(str(v) for v in fila) + f" | {sum(fila)} |")
    md.append("")
    (RAIZ / "RESUMEN.md").write_text("\n".join(md), encoding="utf-8")
    print(f"{len(filas)} pares (persona, año) en {len(anios)} años")


if __name__ == "__main__":
    main()
