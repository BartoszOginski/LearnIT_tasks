sekret = 42

while True:
    liczba = int(input("Zgadnij sekretną liczbę: "))

    if liczba == sekret:
        print("Gratulacje! To poprawna liczba.")
        break
    else:
        print("To zła liczba. Spróbuj ponownie.")