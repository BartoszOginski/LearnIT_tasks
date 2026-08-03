class WiekNiepoprawnyError(Exception):
    pass

def rejestruj_uzytkownika(wiek):
    if not isinstance(wiek, int):
        raise ValueError("Wiek nie jest liczbą")
    if wiek < 18:
        raise WiekNiepoprawnyError("Użytkownik musi mieć powyżej 18 lat")
    if wiek < 0:
        raise ValueError("Użytkownik nie może mieć ujemnego wieku")
    if wiek > 150:
        raise ValueError("Wiek jest przesadzony")
    print (f"Zarejestrowano uzytkownika o wieku {wiek} lat")


rejestruj_uzytkownika(160)