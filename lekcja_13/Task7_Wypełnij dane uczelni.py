import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()

studenci = [
    ("Jan", "Kowalski"),
    ("Anna", "Nowak"),
    ("Piotr", "Wiśniewski"),
    ("Maria", "Wójcik")
]

audytoria = [
    ("Budynek A", 101),
    ("Budynek B", 205),
    ("Budynek C", 310)
]

c.executemany(
    "INSERT INTO studenci (imie, nazwisko) VALUES (?, ?)", studenci)

conn.commit()

c.executemany(
    "INSERT INTO audytoria (nazwa_budynku, numer_sali) VALUES (?, ?)", audytoria)

conn.commit()

print("Dodano studentów oraz audytoria do bazy")

conn.close()

