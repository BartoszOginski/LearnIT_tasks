while True:
    try:
        liczba1 = float(input("Podaj pierwszą liczbę: "))
        liczba2 = float(input("Podaj drugą liczbę: "))
        operacja = str(input("Jaką operację chcesz wykonać (+,-,*,/): "))

        operacje = {
         "+": liczba1 + liczba2,
         "-": liczba1 - liczba2, 
         "*": liczba1 * liczba2, 
         "/": liczba1 / liczba2}

        if operacja not in operacje:
            print("Nie ma takiej operacji")
            continue
        wynik = operacje[operacja]

    except ValueError:
        print("Podano nieprawidłową wartość")

    except ZeroDivisionError:
        print("Nie można dzielić przez zero")

    else:
        print(f"Wynik: {wynik}")

    finally:
        print("Rozpoczynanie kolejnej operacji...")

    dalej = str(input("Czy chcesz kontynuować (tak/nie): ")).lower()

    if dalej == "nie":
        print("Koniec operacji")
        break
 