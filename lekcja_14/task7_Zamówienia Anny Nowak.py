import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT * FROM Produkty p
JOIN Zamowienia_Produkty zp ON zp.id_produktu = p.id_produktu
JOIN Zamowienia z ON z.id_zamowienia = zp.id_zamowienia
JOIN Klienci k ON k.id_klienta  = z.id_klienta
WHERE k.imie= "Anna Nowak"
'''

c.execute(query)

wyniki = c.fetchall()

for wynik in wyniki:
    print(f"{wynik[1]}")