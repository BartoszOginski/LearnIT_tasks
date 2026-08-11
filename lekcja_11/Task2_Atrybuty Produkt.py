class Produkt:
    def __init__(self, nazwa, cena, kategoria):
        self.nazwa = nazwa
        self.cena = cena
        self.kategoria = kategoria

Chleb = Produkt("Chleb", 2, "Pieczywo")

print(f"{Chleb.nazwa}")
print(f"{Chleb.cena}zł")
print(f"{Chleb.kategoria}")

