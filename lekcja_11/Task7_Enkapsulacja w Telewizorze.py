class Telewizor:
    def __init__(self, kanal=1, glosnosc=10, wlaczony="Wyłączony"):
        self.__kanal = kanal
        self.__glosnosc = glosnosc
        self.__wlaczony = wlaczony

    def wlacz(self):
        self.__wlaczony = "Włączony"

    def wylacz(self):
            self.__wlaczony = "Wyłączony"

    def glosniej(self):
            if self.__wlaczony == "Włączony" and self.__glosnosc < 100:
               self.__glosnosc += 1

    def ciszej(self):
                if self.__wlaczony == "Włączony" and self.__glosnosc > 0:
                   self.__glosnosc -=1

    def zmien_kanal(self, numer):
           if self.__wlaczony == "Włączony":
                 self.__kanal = numer

    def info(self):
          print(f"Stan: {self.__wlaczony}, kanał: {self.__kanal}, głośność: {self.__glosnosc}")

tv = Telewizor()

tv.info()

tv.wlacz()
tv.zmien_kanal(5)
tv.glosniej()
tv.glosniej()

tv.info()
          


