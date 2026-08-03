imie = str(input("Podaj swoje imię: "))
wiek = int(input("Podaj swój wiek: "))
miasto = str(input("Podaj miasto zamieszkania: "))

print("A więc, masz na imię", imie, ", masz", wiek,
      "lat i mieszkasz w mieście", miasto + ".")

#Drugi sposób

imie = str(input("Podaj swoje imię: "))
wiek = int(input("Podaj swój wiek: "))
miasto = str(input("Podaj miasto zamieszkania: "))

print(f"A więc, masz na imię {imie}, masz {wiek} lat i mieszkasz w mieście {miasto}.")