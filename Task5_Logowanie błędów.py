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
            raise ValueError ("Nie ma takiej operacji")
        wynik = operacje[operacja]

    
    except Exception as e:
        sciezka = r"D:\python_lessons\log.txt"
        with open(sciezka,"a", encoding="utf-8") as plik:
            plik.write(f"{type(e).__name__}: {e} \n")
        print (f"Wystąpił błąd: {e}")

    else:
        print(f"Wynik: {wynik}")

    finally:
        print("Rozpoczynanie kolejnej operacji...")

    dalej = str(input("Czy chcesz kontynuować (tak/nie): ")).lower()

    if dalej == "nie":
        print("Koniec operacji")
        break