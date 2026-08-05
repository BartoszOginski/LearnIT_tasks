import csv

produkty = [
{"nazwa": "Mleko", "cena": 3.50}, 
{"nazwa": "Chleb", "cena": 4.20}]

with open("produkty.csv", "w", newline="", encoding="utf-8") as f:
    plik = csv.DictWriter(f, fieldnames=["nazwa", "cena"])

    plik.writeheader()
    plik.writerows(produkty)