def analiza_listy(lista):
    return min(lista), max(lista), sum(lista)

wynik = analiza_listy([1,2,3,4,5,20])

print(wynik)