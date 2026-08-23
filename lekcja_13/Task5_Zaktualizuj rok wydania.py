import sqlite3

conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()

nowy_rok = 2026
ksiazka_do_aktualizacji = "Pieśń lodu i Ognia"

c.execute("UPDATE ksiazki SET rok_wydania = ? WHERE tytul = ?", (nowy_rok, ksiazka_do_aktualizacji))

conn.commit()

print("Książka zaktualizowna")

c.execute("SELECT * FROM ksiazki WHERE tytul = ?", (ksiazka_do_aktualizacji,))

zaktualizowana_ksiazka = c.fetchone()
print(f"Nowe dane: {zaktualizowana_ksiazka}")

conn.close()