prawo_jazdy = input("Czy masz prawo jazdy? Wpisz tak lub nie: ")
wiek = int(input("Ile masz lat? "))

wynik = wiek >= 18 and prawo_jazdy.lower() == "tak"

print(wynik)