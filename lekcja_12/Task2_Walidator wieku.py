class Uzytkownik:
    def __init__(self, wiek):
        self.__wiek = wiek

    @property
    def wiek(self):
        print("Odczytano wiek...")
        return self.__wiek

    @wiek.setter
    def wiek(self, nowy_wiek):
        if 0 <= nowy_wiek <= 120:
            self.__wiek = nowy_wiek
        else:
            print("Błąd: wiek musi być w zakresie od 0 do 120.")


uzytkownik = Uzytkownik(20)

print(uzytkownik.wiek)

uzytkownik.wiek = 30
print(uzytkownik.wiek)

uzytkownik.wiek = 150
print(uzytkownik.wiek) 