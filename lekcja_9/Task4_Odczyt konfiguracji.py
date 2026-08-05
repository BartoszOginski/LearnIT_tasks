import json

with open("config.json", "r", encoding="utf-8") as f:
    tresc = json.load(f)

print(f"Witaj, {tresc["uzytkownik"]} ! Twój motyw to {tresc["motyw"]}")