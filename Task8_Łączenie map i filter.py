lista = [-5, 2, 8, -1, 0, 10]

druga_lista = list(map(lambda x: x*x, filter(lambda i: i > 0, lista)))

print(druga_lista)