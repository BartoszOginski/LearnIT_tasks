class InvalidPasswordError(Exception):
    pass


def ustaw_haslo(haslo):
    if len(haslo) < 8:
        raise InvalidPasswordError("Hasło musi mieć co najmniej 8 znaków.")
    
    print("Hasło zostało ustawione.")


try:
    ustaw_haslo("abc")
except InvalidPasswordError as blad:
    print("Błąd:", blad)