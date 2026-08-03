cena = 100

student = input("Czy jesteś studentem? (tak/nie): ").lower()
wiek = int(input("Podaj swój wiek: "))

if student == "tak" or wiek < 18:
    cena = cena * 0.5
    print("Przysługuje Ci 50% zniżki.")
else:
    print("Nie przysługuje Ci zniżka.")

print("Cena biletu:", cena, "PLN")