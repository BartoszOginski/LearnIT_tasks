import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT
   AVG(cena) as avg_cena
FROM Produkty p
JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
WHERE k.nazwa_kategorii = "Książki"
'''

c.execute(query)

wynik = c.fetchone()

print(f"Suma wszystkich produktów z kategorii 'Książki': {wynik[0]}")