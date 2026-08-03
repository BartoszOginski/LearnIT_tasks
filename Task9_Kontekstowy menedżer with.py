def czytaj_plik(nazwa_pliku):
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        return plik.read()


tresc = czytaj_plik("dane.txt")
print(tresc)