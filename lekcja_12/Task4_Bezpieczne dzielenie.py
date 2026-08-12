def bezpieczne_dzielenie(a,b):
    try:
       print(a/b)
    except ZeroDivisionError:
        print("Błąd: Dzielenie przez zero!")

bezpieczne_dzielenie(5,5)
bezpieczne_dzielenie(5,0)