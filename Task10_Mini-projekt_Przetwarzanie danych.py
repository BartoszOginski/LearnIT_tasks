uzytkownicy = [
{"imie": "Jan", "wiek": 30, "aktywny": True},
{"imie": "Anna", "wiek": 17, "aktywny": False},
{"imie": "Piotr", "wiek": 25, "aktywny": True}
]

lista = list(map(lambda i: i["imie"].upper(), filter(lambda x: x["aktywny"] == True and x["wiek"] > 18, uzytkownicy)))

print(lista)