wiek = int(input("Podaj swój wiek: "))

if wiek >= 0 and wiek <= 1:
    print("Niemowlę")
elif wiek >= 2 and wiek <= 12:
    print("Dziecko")
elif wiek >= 13 and wiek <= 17:
    print("Nastolatek")
elif wiek >= 18 and wiek <= 64:
    print("Dorosły")
elif wiek >= 65:
    print("Senior")
else:
    print("Podano nieprawidłowy wiek")