# Wersja 1 – z użyciem metody get()

def pobierz_wartosc(slownik, klucz):
    return slownik.get(klucz)

slownik = {
    "imie": "Jan",
    "wiek": 25
}

print(pobierz_wartosc(slownik, "imie"))
print(pobierz_wartosc(slownik, "miasto"))