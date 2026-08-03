kursy = { "USD": 4.0, "EUR": 4.3}

while True:
    kwota_pln = float(input("Podaj kwotę w PLN: "))

    while True:
        waluta = input("Podaj walutę (USD/EUR): ").strip().upper()

        if waluta in kursy:
            break

        print("Nieobsługiwana waluta. Spróbuj ponownie.")

    wynik = kwota_pln / kursy[waluta]
    print(f"{kwota_pln:.2f} PLN = {wynik:.2f} {waluta}")

    odpowiedz = input("Czy chcesz kontynuować? (tak/nie): ").strip().lower()

    if odpowiedz == "nie":
        break