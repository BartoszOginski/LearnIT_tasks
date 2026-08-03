suma = 0

nazwa_pliku = input("Podaj nazwę pliku: ")

try:
    with open(nazwa_pliku, "r", encoding="utf-8") as plik:
        for linia in plik:
            try:
                liczba = float(linia.strip())
                suma += liczba

            except ValueError:
                print(f"Pominięto linię: {linia.strip()}")

except FileNotFoundError:
    print("Błąd: plik nie istnieje.")

finally:
    print("Suma wynosi:", suma)