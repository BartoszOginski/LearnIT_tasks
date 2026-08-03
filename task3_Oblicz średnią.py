def oblicz_średnią(*args):
    if len(args) == 0:
        return 0
    return sum(args)/len(args)

print(oblicz_średnią(5, 4, 3))
print(oblicz_średnią(1, 2, 3, 4, 5, 6))
print(oblicz_średnią())