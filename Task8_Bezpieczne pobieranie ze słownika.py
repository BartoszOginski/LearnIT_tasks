class BladWalidacjiError(Exception):
    pass


def waliduj_haslo(haslo):
    bledy = []

    if len(haslo) < 8:
        bledy.append("Hasło musi mieć co najmniej 8 znaków.")

    if not any(znak.isupper() for znak in haslo):
        bledy.append("Hasło musi zawierać co najmniej jedną wielką literę.")

    if not any(znak.islower() for znak in haslo):
        bledy.append("Hasło musi zawierać co najmniej jedną małą literę.")

    if not any(znak.isdigit() for znak in haslo):
        bledy.append("Hasło musi zawierać co najmniej jedną cyfrę.")

    if bledy:
        raise BladWalidacjiError(bledy)

    return bledy

walidacja = str(input("Podaj hasło: "))

waliduj_haslo(walidacja)