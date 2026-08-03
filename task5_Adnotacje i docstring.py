def kalkulator (a:float, b:float, operacja:str) -> float:
    """
    Wykonuje podstawowe działanie matematyczne na dwóch liczbach.
    Parametry:
       a (float): Pierwsza liczba.
       b (float): Druga liczba.
       operacja (str): Symbol działania:
          "+" - dodawanie,
          "-" - odejmowanie,
          "*" - mnożenie,
          "/" - dzielenie.
    Zwraca:
       float: Wynik wybranego działania matematycznego.
    """
    if operacja == "+":
        wynik = a + b
        print (f"Wynik działania: {wynik}")
    elif operacja == "-":
        wynik = a - b
        print (f"Wynik działania: {wynik}")
    elif operacja == "*":
        wynik = a * b
        print (f"Wynik działania: {wynik}")
    elif operacja == "/":
        wynik = a / b
        print (f"Wynik działania: {wynik}")
    else:
        raise ValueError ("Błędna operacja")
    return

kalkulator (6.0, 10.0, "-")