import sqlite3

conn = sqlite3.connect('uczelnia.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS przypisania(
    id_przypisania INTEGER PRIMARY KEY,
    id_studenta INTEGER,
    id_audytorium INTEGER,
    FOREIGN KEY (id_studenta) REFERENCES studenci(id_studenta),
    FOREIGN KEY (id_audytorium) REFERENCES audytoria(id_audytorium)
)
''')

conn.commit()

print("Tabela 'przypisania' została utworzona")

conn.close()