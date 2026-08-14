class InvalidPasswordError (Exception):
    pass

def ustaw_haslo(haslo):
    if len(haslo) < 8:
        raise InvalidPasswordError ("Hasło powinno mieć co najmniej 8 znaków")
    print("Hasło zostało pomyślnie ustawione")

try:
    ustaw_haslo("abcd")
except InvalidPasswordError as blad:
    print(f"Błąd: {blad}")