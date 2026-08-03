def wielokrotne_powitanie(imie: str, ilosc: int) -> None:
    for i in range(ilosc):
        print(f"Cześć, {imie}!")
    return

wielokrotne_powitanie ("Bartek", 6)