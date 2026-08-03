def sprawdz_haslo(haslo: str) -> bool:
    if len(haslo) < 8:
        return False
    duza_litera = False
    cyfra = False

    for znak in haslo:
        if znak.isupper():
            duza_litera = True

        if znak.isdigit():
            cyfra = True
    return duza_litera and cyfra

print(sprawdz_haslo("LearnIT8"))

