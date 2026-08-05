plik = str(input("Jaki plik chcesz zbadać: "))
slowo = str(input("Jakie jest szukane słowo: "))

with open(plik, "r", encoding="utf-8") as duzy_plik, \
     open("wyniki_wyszukiwania.txt", "w", encoding="utf-8") as plik_koncowy:

    for linia in duzy_plik:
        if slowo.lower() in linia.lower():
            plik_koncowy.write(linia)
    