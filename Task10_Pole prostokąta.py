def oblicz_pole_prostokata(a, b):
    """Oblicza pole prostokąta na podstawie długości boków."""

    # Obliczenie pola prostokąta
    pole = a * b

    # Zwrócenie wyniku
    return pole


# Długość pierwszego boku
bok_a = 10

# Długość drugiego boku
bok_b = 20

# Wywołanie funkcji i zapisanie wyniku
wynik = oblicz_pole_prostokata(bok_a, bok_b)

# Wyświetlenie wyniku
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")