def stworz_licznik():
    x = 0

    def zwieksz_licznik():
        nonlocal x
        x += 1
        return x
    return zwieksz_licznik

licznik = stworz_licznik()

print(licznik())
print(licznik())
print(licznik())
print(licznik())
