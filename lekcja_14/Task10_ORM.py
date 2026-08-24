import sqlite3

class Produkt:
    def __init__(self, id_produktu, nazwa_produktu, cena):
        self.id_produktu = id_produktu
        self.nazwa_produktu = nazwa_produktu
        self.cena = cena


def pobierz_wszystkie_produkty():
    conn = sqlite3.connect("sklep.db")
    c = conn.cursor()

    query = '''
    SELECT id_produktu, nazwa_produktu, cena
    FROM Produkty
    '''

    c.execute(query)
    wyniki = c.fetchall()

    produkty = []

    for wynik in wyniki:
        produkt = Produkt(wynik[0], wynik[1], wynik[2])
        produkty.append(produkt)

    conn.close()

    return produkty


przedmioty = pobierz_wszystkie_produkty()

for przedmiot in przedmioty:
    print(przedmiot.nazwa_produktu, przedmiot.cena)