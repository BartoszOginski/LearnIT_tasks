class BladPrzetwarzaniaDanychError(Exception):
    pass

def przetworz_dane(dane):
    try:
        wartosc = dane["klucz"]
        return wartosc

    except KeyError as e:
        brakujacy_klucz = e.args[0]
        raise BladPrzetwarzaniaDanychError(f"Brakuje klucza: {brakujacy_klucz}") from e

slownik = {"imie": "Jan"}

przetworz_dane(slownik)