def oblicz_srednia (lista_ocen):
    assert len(lista_ocen) > 0, "lista ocen jest pusta"
    return sum(lista_ocen)/len(lista_ocen)

lista = [1, 2, 3, 4, 5, 6, 7]

print(oblicz_srednia (lista))