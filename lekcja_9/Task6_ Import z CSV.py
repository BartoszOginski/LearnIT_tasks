import csv

suma = 0

with open ("produkty.csv", "r", newline="", encoding="utf-8") as f:
    dane = csv.DictReader(f)

    for wiersz in dane:
        suma += float(wiersz["cena"])
print(f"Suma cen: {suma}")
