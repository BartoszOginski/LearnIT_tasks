class Data:
    def __init__(self, dzien, miesiac, rok):
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok

    @classmethod
    def ze_stringa (cls, text):
        dzien, miesiac, rok = text.split("-")
        return cls(int(dzien), int(miesiac), int(rok))

data = Data.ze_stringa("16-08-2026")

print(data.dzien)
print(data.miesiac)
print(data.rok)