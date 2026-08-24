import sqlite3

conn = sqlite3.connect('sklep.db')
c = conn.cursor()

c.execute("SELECT * FROM Klienci")

wszyscy_klienci = c.fetchall()

for klient in wszyscy_klienci:
    print(f"Imię: {klient[1]}, email: {klient[2]}")