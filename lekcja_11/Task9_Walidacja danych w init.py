class RejestracjaUzytkownika:
    def __init__(self, email, haslo):

        if "@" not in email:
            raise ValueError("Email musi zawierać znak @")

        if len(haslo) < 8:
            raise ValueError("Hasło musi mieć co najmniej 8 znaków")

        self.email = email
        self.haslo = haslo

try:
    uzytkownik1 = RejestracjaUzytkownika(
        "test@gmail.com",
        "haslo123"
    )
    print("Użytkownik został utworzony")

except ValueError as blad:
    print(blad)

try:
    uzytkownik2 = RejestracjaUzytkownika(
        "testgmail.com",
        "haslo123"
    )
    print("Użytkownik został utworzony")

except ValueError as blad:
    print(blad)

try:
    uzytkownik3 = RejestracjaUzytkownika(
        "test@gmail.com",
        "123"
    )
    print("Użytkownik został utworzony")

except ValueError as blad:
    print(blad)