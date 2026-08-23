import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS studenci(
id_studenta INTEGER PRIMARY KEY,
imie TEXT NOT NULL,
nazwisko TEXT NOT NULL
)
''')

conn.commit()

print("Tabela 'studenci' została utworzona")

c.execute('''
CREATE TABLE IF NOT EXISTS audytoria(
id_audytorium INTEGER PRIMARY KEY,
nazwa_budynku TEXT NOT NULL,
numer_sali INTEGER
)
''')

conn.commit()

print("Tabela 'audytoria' została utworzona")

conn.close()