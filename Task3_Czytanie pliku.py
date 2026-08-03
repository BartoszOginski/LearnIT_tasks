def czytaj_plik(nazwa_pliku):
    try:
        with open(nazwa_pliku, "r", encoding="utf-8") as plik:
            return plik.read()

    except FileNotFoundError:
        print("Błąd: plik nie istnieje.")

    except PermissionError:
        print("Błąd: brak uprawnień do odczytu pliku.")


# Przykład użycia
tresc = czytaj_plik("dane.txt")

if tresc is not None:
    print(tresc)