import sqlite3

conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()

print("\n Książki autorstwa Trudi Canavan")
c.execute("SELECT tytul, autor, rok_wydania FROM ksiazki WHERE autor = ?", ("Trudi Canavan",))

ksiazki_canavan = c.fetchall()
for ksiazka in ksiazki_canavan:
    print(f"autor: {ksiazka[1]}, tytul: {ksiazka[0]}")

conn.close()