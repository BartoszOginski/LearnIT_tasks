import json

class BrakTakiejOpcji(Exception):
    pass

try:
    with open("zadania.json", "r", encoding="utf-8") as f:
        zadania = json.load(f)

except FileNotFoundError:
    zadania = []

while True:
    print("LISTA ZADAŃ")
    print("1. Dodaj zadanie")
    print("2. Wyświetl zadania")
    print("3. Zapisz i zakończ")

    wybor = input("Co chcesz wykonać?: ")

    if wybor == "1":
        nowe_zadanie = str(input("Podaj treść zadania: "))
        zadania.append(nowe_zadanie)
        print("Dodano zadanie")

    elif wybor == "2":
        if len(zadania) == 0:
            print("Lista zadań jest pusta")
        else:
            for numer, zadanie in enumerate(zadania, start=1):
                print(f"{numer}. {zadanie}")

    elif wybor == "3":
        with open("zadania.json", "w", encoding="utf-8") as f:
            json.dump(zadania, f, ensure_ascii=False, indent=4)

        print ("Zapisano i zakończono program")   
        break

    else:
        raise BrakTakiejOpcji ("Nie ma takiej opcji")       
