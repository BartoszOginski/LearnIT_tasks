import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

def znajdz_produkty_w_kategorii(nazwa_kategorii):
    query = '''
    SELECT p.nazwa_produktu, p.cena
    FROM Produkty p
    JOIN Kategorie k ON p.id_kategorii = k.id_kategorii
    WHERE k.nazwa_kategorii = ?
    '''

    c.execute(query, (nazwa_kategorii,))
    return c.fetchall()


produkty = znajdz_produkty_w_kategorii("Elektronika")

print(produkty)

conn.close()