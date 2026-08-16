class MetaWalidujMetody(type):
    def __new__(mcls, name, bases, namespace):
        for nazwa, obiekt in namespace.items():
            # sprawdza metody magiczne
            if nazwa.startswith("__"):
                continue

            # sprawdza czy metoda ma docstring'a
            if callable(obiekt):
                if obiekt.__doc__ is None:
                    raise TypeError (f"Metoda '{nazwa}' wymaga dokumentacji")
        return super().__new__(mcls, name, bases, namespace)

#Test poprawności dwóch klas

class Poprawna(metaclass=MetaWalidujMetody):
    def przywitaj(self):
        """Wyświetla powitanie."""
        print("Cześć!")

    def dodaj(self, a, b):
        """Zwraca sumę dwóch liczb."""
        return a + b


print("Klasa Poprawna została utworzona.")

obiekt = Poprawna()
obiekt.przywitaj()
print(obiekt.dodaj(2, 3))


class Niepoprawna(metaclass=MetaWalidujMetody):
    def test(self):
        print("Ta metoda nie ma docstringa.")