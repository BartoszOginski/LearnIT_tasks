from dataclasses import dataclass

class BrakSrodkowError (Exception):
    pass

@dataclass
class KontoBankowe:
    _saldo: int

    @property
    def saldo(self):
        return self._saldo

    def wplac(self, kwota):
        if kwota > 0:
            self._saldo += kwota
        else:
            raise ValueError ("Kwota nie może być ujemna!")
        
    def wyplac(self, kwota):
        if kwota > 0 and self._saldo > 0:
            self._saldo -= kwota
        elif kwota < 0:
            raise ValueError ("Kwota nie może być ujemna!")
        elif self._saldo <= 0:
            raise BrakSrodkowError ("Brak środków na koncie")

    def sprawdz(self):
        print (self._saldo)

Konto = KontoBankowe(1000)

Konto.wplac(200)
Konto.sprawdz()
Konto.wyplac(1200)
Konto.sprawdz()
Konto.wyplac(5)
        