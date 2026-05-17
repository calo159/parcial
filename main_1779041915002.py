from country import Country, CountryAPI

# =============================================================
# Parcial — Clase 08: APIs REST con Python
# Integrantes: Carlos / Yerfreth
#
# Iniciales y paises elegidos (en orden):
#
#   C A R      L      O    S
#   C -> Colombia
#   A -> Austria
#   R -> Romania       (R de Carlos)
#   L -> Latvia
#   O -> Oman
#   S -> Sweden
#
#   Y       E        R                  F         R        E           T        H
#   Y -> Yemen
#   E -> Ecuador       (primera E de Yerfreth)
#   R -> Rwanda        (primera R de Yerfreth)
#   F -> Finland
#   R -> Russia        (segunda R de Yerfreth)
#   E -> Ethiopia      (segunda E de Yerfreth)
#   T -> Turkey
#   H -> Hungary
# =============================================================

PAISES_NOMBRES = [
    "colombia",   # C
    "austria",    # A
    "romania",    # R - Carlos
    "latvia",     # L
    "oman",       # O
    "sweden",     # S
    "yemen",      # Y
    "ecuador",    # E - primera E
    "rwanda",     # R - primera R Yerfreth
    "finland",    # F
    "russia",     # R - segunda R Yerfreth
    "ethiopia",   # E - segunda E
    "turkey",     # T
    "hungary",    # H
]


def main():
    api = CountryAPI()

    print("=" * 60)
    print("  Cargando paises de Carlos y Yerfreth...")
    print("=" * 60)

    paises = []
    for nombre in PAISES_NOMBRES:
        p = api.by_name(nombre)
        if p:
            paises.append(p)
            print(f"  [OK] {p.nombre}")

    print(f"\n  Total cargados: {len(paises)} paises\n")

    # ----------------------------------------------------------
    # Ficha de cada pais
    # ----------------------------------------------------------
    print("=" * 60)
    print("  FICHAS DE CADA PAIS")
    print("=" * 60)

    for p in paises:
        print()
        print(p)

    # ----------------------------------------------------------
    # Comparacion general — todos entre si
    # ----------------------------------------------------------
    print("\n" + "=" * 60)
    print("  COMPARACION GENERAL")
    print("=" * 60)

    if paises:
        paises[0].comparar(paises[1:])

    # ----------------------------------------------------------
    # Ranking por poblacion
    # ----------------------------------------------------------
    print("\n" + "=" * 60)
    print("  RANKING POR POBLACION")
    print("=" * 60)

    ranking_pob = sorted(paises, key=lambda p: p.poblacion, reverse=True)
    for i, p in enumerate(ranking_pob, 1):
        print(f"  {i:2}. {p.nombre:<20} {p.poblacion:>15,}")

    # ----------------------------------------------------------
    # Ranking por densidad
    # ----------------------------------------------------------
    print("\n" + "=" * 60)
    print("  RANKING POR DENSIDAD")
    print("=" * 60)

    ranking_den = sorted(paises, key=lambda p: p.density(), reverse=True)
    for i, p in enumerate(ranking_den, 1):
        print(f"  {i:2}. {p.nombre:<20} {p.density():>12.2f} hab/km2")

    # ----------------------------------------------------------
    # Ranking por area
    # ----------------------------------------------------------
    print("\n" + "=" * 60)
    print("  RANKING POR AREA")
    print("=" * 60)

    ranking_area = sorted(paises, key=lambda p: p.area, reverse=True)
    for i, p in enumerate(ranking_area, 1):
        print(f"  {i:2}. {p.nombre:<20} {p.area:>15,.2f} km2")


if __name__ == "__main__":
    main()
