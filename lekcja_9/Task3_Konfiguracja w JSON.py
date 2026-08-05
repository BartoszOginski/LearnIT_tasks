import json

konfiguracja = {
"uzytkownik": "admin", 
"motyw": "ciemny", 
"rozdzielczosc":[1920, 1080]}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(konfiguracja, f, indent=4, ensure_ascii="False")
