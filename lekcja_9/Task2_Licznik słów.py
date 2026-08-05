while True:
   nazwa_pliku = str(input("Podaj plik do otwarcia: "))

   try:
      with open(nazwa_pliku, "r",encoding="utf-8") as f:
          tresc = f.read()
          liczba_slow = len(tresc.split())
          print(liczba_slow)
          break

   except FileNotFoundError:
      print("Plik nie istnieje")
      continue
