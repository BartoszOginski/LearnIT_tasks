import sqlite3

conn = sqlite3.connect('biblioteka.db')
c = conn.cursor()

ksiazki_do_dodania = [

    ("Pieśń lodu i Ognia", "George R.R Martin", 1996),
    ("Trylogia Czarnego Maga", "Trudi Canavan", 2001),
    ("Trylogia Łotra", "Trudi Canavan", 2010)
]

c.executemany("INSERT INTO ksiazki (tytul, autor, rok_wydania) VALUES (?, ?, ?)", ksiazki_do_dodania)

conn.commit()
print(f"Dodano {c.rowcount * len(ksiazki_do_dodania)} rekordy do tabeli ksiazki")

conn.close()