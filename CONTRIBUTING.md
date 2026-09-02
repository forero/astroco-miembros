# Cómo corregir o completar el registro

Este repositorio es un registro de membresía, no un directorio de contacto. Solo
contiene nombre, clase de membresía, años y afiliación institucional: datos que
ya son públicos en las fuentes citadas en el README.

## Editar los datos

1. Edita **solo** `data/fuente-2018-2023.csv` o `data/fuente-2025-2026.csv`.
   Los demás archivos de `data/` y `RESUMEN.md` se generan solos.
2. Vuelve a generar los archivos derivados:
   ```bash
   python3 scripts/construir.py
   ```
3. Abre un Pull Request incluyendo los archivos derivados actualizados.

### Convenciones

- `anios` es una lista de años separados por `;`, sin espacios: `2021;2022;2023`.
- Las clases válidas son exactamente `Titular`, `Honorario`, `Socio Estudiante`
  y `Socio No-Estudiante`.
- Si corriges una interpretación de años, actualiza también la columna
  `interpretacion` y deja `anios_fuente` intacto: es el registro literal de la
  fuente.

## Si no quieres editar archivos

Abre un Issue describiendo la corrección (nombre, clase, años correctos y de
dónde sale el dato). Alguien hará el cambio.

## Correcciones y bajas

Cualquier persona listada puede pedir que se corrija su entrada o que se
eliminen sus datos, por Issue o por Pull Request, y se hará sin preguntas.
