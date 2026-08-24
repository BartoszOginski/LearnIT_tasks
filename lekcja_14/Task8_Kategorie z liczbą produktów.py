import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

query = '''
SELECT k.nazwa_kategorii, COUNT(p.id_produktu)
FROM Kategorie k
JOIN Produkty p ON k.id_kategorii = p.id_kategorii
GROUP BY k.nazwa_kategorii;
'''

c.execute(query)

wyniki = c.fetchall()

for wynik in wyniki:
    print(f"Kategoria: {wynik[0]}, liczba produktów: {wynik[1]}")