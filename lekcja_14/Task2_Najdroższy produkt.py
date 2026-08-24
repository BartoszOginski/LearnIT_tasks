import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT
   MAX(cena) as max_cena
FROM Produkty
'''

c.execute(query)

wynik = c.fetchone()

print(f"Liczba wszystkich produktów {wynik[0]}")