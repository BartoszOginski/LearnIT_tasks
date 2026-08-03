imiona = ["Anna", "Jan", "Piotr", "Kasia"]

szukane_imie = input("Podaj imię do wyszukania: ")

for imie in imiona:
    if imie.lower() == szukane_imie.strip().lower():
        print("Znaleziono!")
        break
else:
    print("Nie znaleziono imienia na liście.")