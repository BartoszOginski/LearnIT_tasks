class Film:

    def __init__(self, tytul, rezyser, rok):
        self.tytul = tytul
        self.rezyser = rezyser
        self.rok= rok

    def informacje(self):
        return(f"Tytuł: {self.tytul}, Reżyseria: {self.rezyser}, rok produkcji: {self.rok} ")


Batman = Film("Mroczny Rycerz", "Christopher Nolan", 2008)
Odyseja = Film("Odyseja", "Christopher Nolan", 2026)

print(Batman.informacje())
print(Odyseja.informacje())