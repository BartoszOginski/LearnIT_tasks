def stworz_profil(imie, **dane_dodatkowe):
    profil = {"imie":imie}

    profil.update(dane_dodatkowe)

    print(profil)

    return

stworz_profil("Bartek", wiek = 25, miasto = "Łódź", zawód = "Analityk finansowy")