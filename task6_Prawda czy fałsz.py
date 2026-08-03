tekst = input("Wpisz dowolny tekst: ")

wartosc = bool(tekst)

print(wartosc)

if wartosc:
    print("Wpisany tekst jest prawdziwy, ponieważ nie jest pusty.")
else:
    print("Wpisany tekst jest fałszywy, ponieważ jest pusty.")