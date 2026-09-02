# AstroCO - Comunidad Colombiana de Astronomía

Registro público de la membresía de **AstroCO**, la Comunidad Colombiana de
Astronomía, año por año y separada en las clases de membresía vigentes.

El registro cubre dos periodos:

- **2018-2023**, cuando la comunidad funcionaba como **UAI-Col**.
- **2024**: sin membresía activa (cero miembros).
- **2025-2026**, la membresía actual de AstroCO como nodo de ACCEFYN.

## Membresía año por año

Las clases son las que se usan en 2025-2026: **Titular**, **Honorario**,
**Socio Estudiante** y **Socio No-Estudiante**.

| Año | Titular | Honorario | Socio Estudiante | Socio No-Estudiante | Total |
|---|---|---|---|---|---|
| 2018 | 22 | 4 | 6 | 0 | 32 |
| 2019 | 22 | 5 | 3 | 0 | 30 |
| 2020 | 21 | 6 | 0 | 0 | 27 |
| 2021 | 23 | 7 | 2 | 0 | 32 |
| 2022 | 13 | 7 | 1 | 0 | 21 |
| 2023 | 5 | 4 | 0 | 0 | 9 |
| 2024 | 0 | 0 | 0 | 0 | 0 |
| 2025 | 18 | 5 | 4 | 2 | 29 |
| 2026 | 15 | 2 | 4 | 2 | 23 |

Tabla generada automáticamente; ver [RESUMEN.md](RESUMEN.md).

## Estructura del repositorio

```
data/fuente-2018-2023.csv     Registro UAI-Col, tal como aparece en la lista original
data/fuente-2025-2026.csv     Registro AstroCO/ACCEFYN actual
data/membresia-por-anio.csv   Derivado: una fila por (persona, año)
data/resumen-por-anio.csv     Derivado: conteos por año y clase
RESUMEN.md                    Derivado: la tabla de arriba
scripts/construir.py          Genera los tres archivos derivados
```

Los archivos `fuente-*.csv` son los únicos que se editan a mano. Después de
cualquier cambio:

```bash
python3 scripts/construir.py
```

### Columnas de `data/fuente-2018-2023.csv`

| Campo | Descripción |
|---|---|
| `nombre` | Nombre como aparece en la fuente |
| `clase` | Clase equivalente en la nomenclatura 2025-2026 |
| `anios` | Años de membresía, separados por `;` |
| `clase_fuente` | Categoría original en la lista de UAI-Col |
| `anios_fuente` | Años tal como los escribe la fuente, sin normalizar |
| `interpretacion` | Cómo se leyó `anios_fuente` para producir `anios` |
| `notas` | Observaciones |

### Columnas de `data/fuente-2025-2026.csv`

| Campo | Descripción |
|---|---|
| `nombre` | Nombre completo |
| `clase` | Titular, Honorario, Socio Estudiante o Socio No-Estudiante |
| `anios` | `2025;2026` o `2025` según renovación |
| `institucion` | Afiliación publicada |
| `actualizada_2026` | `sí` para quienes la fuente marca con `*` |

## Decisiones de interpretación

Estas son lecturas de la fuente, no datos originales. Corregirlas es bienvenido.

1. **Mapeo de clases.** La lista de UAI-Col usaba categorías distintas. Se
   tradujeron así: `PhD` → **Titular**; `Profesionales - Diáspora` (MSc, PhD,
   candidatos, otros perfiles) → **Honorario**, porque es la clase que en
   2025-2026 ocupan los miembros radicados fuera del país; `Miembro Honorario`
   → **Honorario**; `Estudiante` → **Socio Estudiante**. La clase
   **Socio No-Estudiante** no existía antes de 2025, por eso aparece en cero.
2. **Rangos de años.** La fuente escribe `2018-->2023` para periodos continuos
   y `2018-2019-2021` para listas de años sueltos. Los pares con hueco
   (`2020-2022`, `2019-2023`, `2021-2023`, `2021-2024`) se leyeron como
   periodos continuos; la columna `interpretacion` los marca como
   `rango supuesto`.
3. **2024.** La fuente registra a Mauricio Chacón Pachón como `2021-2024`, pero
   en 2024 no hubo membresía activa, así que su registro se recorta a 2023
   (`rango supuesto recortado`).
4. **2025 vs 2026.** El sitio actual lista los miembros vigentes y marca con
   `*` la membresía actualizada en 2026. Se asume que quienes no llevan `*`
   renovaron por última vez en 2025.
5. **Sin años.** Lauren Flor y Jorge Arias de Greiff aparecen en la lista de
   UAI-Col sin años; no cuentan en ningún año hasta que se registren.
6. Los nombres se transcriben como en la fuente, incluidos posibles errores de
   digitación (por ejemplo `Carlos Eduerdo Cedeño Montaña`).

## Fuentes

- Miembros actuales de AstroCO (ACCEFYN):
  <https://accefyn.com/microsites/nodos/astroco/miembros-actuales/>
- Microsite del nodo AstroCO, captura del 2025-03-28 en Internet Archive:
  <https://web.archive.org/web/20250328021313/https://accefyn.com/microsites/nodos/astroco/>
- Listado histórico de membresía de UAI-Col 2018-2023, aportado por la
  coordinación de la comunidad.

## Cómo corregir o completar

Ver [CONTRIBUTING.md](CONTRIBUTING.md).

## Licencia

Los datos se publican bajo [CC0 1.0](LICENSE) (dominio público).
