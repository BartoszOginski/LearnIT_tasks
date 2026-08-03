def pobierz_wartosc(slownik, klucz):
    try:
        return slownik[klucz]

    except KeyError:
        return None

slownik = {
    "imie": "Jan",
    "wiek": 25
}

print(pobierz_wartosc(slownik, "imie"))
print(pobierz_wartosc(slownik, "miasto"))