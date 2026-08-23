import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()

przypisania = [
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 1)
]

c.executemany(
    "INSERT INTO przypisania (id_studenta, id_audytorium) VALUES (?, ?)",
    przypisania
)

conn.commit()

print("Studenci zostali przypisani do audytoriów.")

conn.close()