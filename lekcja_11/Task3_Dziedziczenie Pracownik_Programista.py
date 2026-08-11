class Pracownik:
    def __init__(self, imie, stawka_godzinowa):
        self.imie = imie
        self.stawka_godzinowa = stawka_godzinowa

    def oblicz_pensje(self, liczba_godzin):
        return(f"Wypracowana pensja: {liczba_godzin * self.stawka_godzinowa}")

class Programista (Pracownik):
    def  __init__(self, imie, stawka_godzinowa, jezyki_programowania):
        super().__init__(imie, stawka_godzinowa)
        self.jezyki_programowania = jezyki_programowania

Marek = Programista("Marek", 15, ["Python", "C++", "JavaScript"])

print(Marek.oblicz_pensje(3))