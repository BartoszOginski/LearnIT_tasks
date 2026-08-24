import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT * FROM Produkty
WHERE cena > (SELECT AVG(cena) FROM Produkty)
'''

c.execute(query)

produkty = c.fetchall()

for produkt in produkty:
    print(f"Produkt: {produkt[1]}, Cena: {produkt[2]}")