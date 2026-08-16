while True:
    try:
        liczba_pierwsza = float(input("Podaj pierwszą liczbę: "))
        liczba_druga = float(input("Podaj drugą liczbę: "))
        operacja = str(input("Jaką operację chcesz wykonać (+,-,*,/): "))

        if operacja == "+":
            print(liczba_pierwsza+liczba_druga)
        elif operacja == "-":
            print(liczba_pierwsza-liczba_druga)
        elif operacja == "*":
            print(liczba_pierwsza*liczba_druga)
        elif operacja == "/":
            print(liczba_pierwsza/liczba_druga)

    except ValueError:
        print("Podana wartość nie jest liczbą!")
    except ZeroDivisionError:
        print("Nie wolno dzielić przez zero!")

    kontynuuacja = str(input("Czy chcesz kontynuuować (y/n): "))
    if kontynuuacja == "n":
        print("Program został zamknięty")
        break


