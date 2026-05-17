import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout
from concurrent.futures import ThreadPoolExecutor, as_completed


BASE = "https://restcountries.com/v3.1"


class Country:
    def __init__(self, data: dict):
        self.nombre    = data["name"]["common"]
        self.oficial   = data["name"]["official"]
        self.capital   = data.get("capital", ["—"])[0]
        self.region    = data.get("region", "—")
        self.subregion = data.get("subregion", "—")
        self.poblacion = data.get("population", 0)
        self.area      = data.get("area", 0.0)
        self.idiomas   = list(data.get("languages", {}).values())
        self.bandera   = data.get("flag", "")

    def density(self) -> float:
        if self.area == 0:
            return 0.0
        return self.poblacion / self.area

    def __str__(self) -> str:
        idiomas_str = ", ".join(self.idiomas) if self.idiomas else "—"
        return (
            f"{self.bandera} {self.nombre} ({self.oficial})\n"
            f"  Capital    : {self.capital}\n"
            f"  Region     : {self.region} / {self.subregion}\n"
            f"  Poblacion  : {self.poblacion:,}\n"
            f"  Area       : {self.area:,.2f} km2\n"
            f"  Densidad   : {self.density():.2f} hab/km2\n"
            f"  Idiomas    : {idiomas_str}"
        )

    def comparar(self, otros: list):
        todos = [self] + otros

        col = 20
        print(f"\n{'Pais':<{col}} {'Poblacion':>15} {'Area (km2)':>15} {'Densidad':>15}")
        print("-" * (col + 48))

        for p in todos:
            print(
                f"{p.nombre:<{col}} "
                f"{p.poblacion:>15,} "
                f"{p.area:>15,.2f} "
                f"{p.density():>14.2f}"
            )

        print("-" * (col + 48))

        mayor_pob  = max(todos, key=lambda p: p.poblacion)
        mayor_area = max(todos, key=lambda p: p.area)
        mayor_den  = max(todos, key=lambda p: p.density())

        print(f"Mayor poblacion : {mayor_pob.nombre}")
        print(f"Mayor area      : {mayor_area.nombre}")
        print(f"Mayor densidad  : {mayor_den.nombre}")


class CountryAPI:
    def by_name(self, name: str) -> "Country | None":
        url = f"{BASE}/name/{name}"
        try:
            r = requests.get(url, timeout=5, params={"fullText": "true"})
            r.raise_for_status()
            return Country(r.json()[0])
        except Timeout:
            print(f"[!] Timeout buscando '{name}'")
        except ConnectionError:
            print("[!] Sin conexion a internet")
        except HTTPError as e:
            print(f"[!] Error {e.response.status_code}: '{name}' no encontrado")
        return None

    def by_names(self, names: list[str], max_workers: int = 10) -> list["Country"]:
        """Obtiene varios paises en paralelo usando un pool de hilos."""
        resultados: dict[str, Country | None] = {}

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futuros = {executor.submit(self.by_name, name): name for name in names}

            for futuro in as_completed(futuros):
                name = futuros[futuro]
                pais = futuro.result()
                resultados[name] = pais
                if pais:
                    print(f"  [OK] {pais.nombre}")

        return [resultados[name] for name in names if resultados.get(name)]

    def by_region(self, region: str) -> list:
        url = f"{BASE}/region/{region}"
        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            return [Country(d) for d in r.json()]
        except Timeout:
            print(f"[!] Timeout buscando region '{region}'")
        except ConnectionError:
            print("[!] Sin conexion a internet")
        except HTTPError as e:
            print(f"[!] Error {e.response.status_code}: region '{region}' no encontrada")
        return []
