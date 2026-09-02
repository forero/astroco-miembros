# AstroCO - Comunidad Colombiana de Astronomía

Registro abierto de las personas que forman parte de **AstroCO**, la Comunidad
Colombiana de Astronomía.

El objetivo es tener un directorio público, sencillo y fácil de mantener, que
permita saber quiénes somos, dónde estamos y en qué trabajamos.

## Estructura del repositorio

```
data/miembros.csv     Directorio de personas (una fila por persona)
data/instituciones.csv Instituciones y afiliaciones referenciadas
CONTRIBUTING.md       Cómo agregar o actualizar tu información
```

## Campos de `data/miembros.csv`

| Campo | Descripción |
|---|---|
| `id` | Identificador corto y único (ej. `jforero`) |
| `nombre` | Nombre completo |
| `pronombres` | Pronombres (opcional) |
| `institucion` | Código de institución en `instituciones.csv` |
| `posicion` | Estudiante pregrado, maestría, doctorado, posdoc, profesor, investigador, aficionado, docente, divulgador, etc. |
| `area` | Áreas de interés separadas por `;` (ej. `cosmología;estructura a gran escala`) |
| `ciudad` | Ciudad de residencia o trabajo |
| `pais` | País (muchos miembros están fuera de Colombia) |
| `orcid` | ORCID iD (opcional) |
| `sitio_web` | Página personal (opcional) |
| `github` | Usuario de GitHub (opcional) |
| `correo_publico` | Correo, solo si se desea hacerlo público (opcional) |

Los campos opcionales pueden quedar vacíos. No se incluye información
personal sensible: cada persona decide qué datos comparte.

## Cómo participar

Ver [CONTRIBUTING.md](CONTRIBUTING.md). En resumen: abre un Pull Request
agregando tu fila al CSV, o abre un Issue con tus datos si prefieres que
alguien más lo haga.

## Licencia

Los datos se publican bajo [CC0 1.0](LICENSE) (dominio público).
