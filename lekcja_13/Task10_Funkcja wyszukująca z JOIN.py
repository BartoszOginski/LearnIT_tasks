import sqlite3

class BrakStudenta(Exception):
    pass

def znajdz_sale_studenta(nazwisko):
    conn = sqlite3.connect("uczelnia.db")
    c = conn.cursor()

    c.execute('''
        SELECT a.nazwa_budynku, a.numer_sali
        FROM studenci AS s
        JOIN przypisania AS p
        ON s.id_studenta = p.id_studenta
        JOIN audytoria AS a
        ON a.id_audytorium = p.id_audytorium
        WHERE s.nazwisko = ?
    ''', (nazwisko,))

    wynik = c.fetchone()

    if wynik:
        print(f"Budynek: {wynik[0]}, sala: {wynik[1]}")
    else:
        raise BrakStudenta("Nie znaleziono studenta.")

    conn.close()


znajdz_sale_studenta("Kowalski")