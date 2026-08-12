plik = None

try:
    plik = open("nieistniejacy.txt", "r", encoding="utf-8")
    zawartosc = plik.read()
except FileNotFoundError:
    print("Plik nie istnieje")
else:
    print("Plik odczytany pomyślnie.")
    print("Zawartość:", zawartosc)
finally:
    if plik:
        plik.close()
        print("Plik został pomyślnie zamknięty")
    else:
        print("Wystąpił błąd")