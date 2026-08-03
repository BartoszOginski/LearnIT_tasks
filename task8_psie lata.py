wiek_psa = int(input("Podaj wiek psa: "))

if wiek_psa == 1:
    wiek_czlowieka = 15
elif wiek_psa == 2:
    wiek_czlowieka = 24
else:
    wiek_czlowieka = 24 + (wiek_psa - 2) * 5

print(f"Wiek psa w ludzkich latach wynosi {wiek_czlowieka}.")