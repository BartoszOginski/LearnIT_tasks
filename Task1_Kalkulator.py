def kalkulator (a, b, operacja):
    if operacja == "+":
        wynik = a + b
        print (f"Wynik działania: {wynik:.0f}")
    elif operacja == "-":
        wynik = a - b
        print (f"Wynik działania: {wynik:.0f}")
    elif operacja == "*":
        wynik = a * b
        print (f"Wynik działania: {wynik:.0f}")
    else:
        wynik = a / b
        print (f"Wynik działania: {wynik:.0f}")
    return

a = float(input("Podaj pierwszą liczbę: "))   
b = float(input("Podaj drugą liczbę: "))
operacja = str(input("Jakie działanie chcesz wykonać (+;-;*;/): "))

kalkulator(a, b, operacja)