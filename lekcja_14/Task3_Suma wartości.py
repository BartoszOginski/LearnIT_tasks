import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT
   SUM(cena) as sum_cena
FROM Produkty p
JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
WHERE k.nazwa_kategorii = "Elektronika"
'''

c.execute(query)

wynik = c.fetchone()

print(f"Suma wszystkich produktów z kategorii 'Elektronika': {wynik[0]}")