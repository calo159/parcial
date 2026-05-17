# Parcial — Clase 08: APIs REST con Python

**Integrantes:** Carlos / Yerfreth

---

## Descripción

Programa en Python que consume la API pública [REST Countries](https://restcountries.com/) para obtener información de 14 países elegidos a partir de las iniciales de los nombres de los integrantes. Muestra fichas individuales de cada país, una comparación general y rankings por población, densidad y área.

---

## Países elegidos

Los países se eligieron tomando una letra por inicial de cada nombre:

### Carlos — C · A · R · L · O · S

| Letra | País |
|-------|------|
| C | Colombia |
| A | Austria |
| R | Romania |
| L | Latvia |
| O | Oman |
| S | Sweden |

### Yerfreth — Y · E · R · F · R · E · T · H

| Letra | País |
|-------|------|
| Y | Yemen |
| E | Ecuador |
| R | Rwanda |
| F | Finland |
| R | Russia |
| E | Ethiopia |
| T | Turkey |
| H | Hungary |

---

## Estructura del proyecto

```
├── country.py   # Clases Country y CountryAPI
└── main.py      # Punto de entrada del programa
```

### `country.py`
- **`Country`** — modela un país como objeto con atributos (`nombre`, `capital`, `region`, `poblacion`, `area`, `idiomas`), método `density()` para calcular habitantes por km², y `comparar(otros)` para imprimir una tabla comparativa.
- **`CountryAPI`** — encapsula todas las peticiones HTTP a la API. Incluye `by_name()`, `by_region()` y `by_names()` (carga múltiple en paralelo con `ThreadPoolExecutor`).

### `main.py`
- Carga los 14 países de forma concurrente
- Imprime la ficha de cada país
- Muestra la comparación general
- Muestra los rankings por población, densidad y área

---

## Cómo ejecutarlo

Requiere Python 3.11+ y la librería `requests`:

```bash
pip install requests
python main.py
```

---

## Ejemplo de salida

```
============================================================
  Cargando paises de Carlos y Yerfreth
============================================================
  [OK] Colombia
  [OK] Austria
  ...
  Total cargados: 14 paises
  Tiempo de carga: 0.39s

🇨🇴 Colombia (Republic of Colombia)
  Capital    : Bogotá
  Region     : Americas / South America
  Poblacion  : 53,057,212
  Area       : 1,141,748.00 km2
  Densidad   : 46.47 hab/km2
  Idiomas    : Spanish
...

  RANKING POR POBLACION
   1. Russia               146,028,325
   2. Ethiopia             111,652,998
   3. Turkey                85,664,944
  ...
```
