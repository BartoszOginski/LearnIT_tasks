class KalkulatorWalut:
    @staticmethod
    def usd_na_pln (usd):
        kurs = 4.0
        return usd * kurs

print (KalkulatorWalut.usd_na_pln(4))