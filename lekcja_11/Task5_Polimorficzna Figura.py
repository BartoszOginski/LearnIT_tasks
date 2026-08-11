import math

class Figura:
    def oblicz_pole(self):
        pass

class Kwadrat(Figura):
    def __init__(self, bok):
        self.bok = bok

    def oblicz_pole(self):
        return(self.bok ** 2)

class Kolo (Figura):
    def __init__(self, promien):
        self.promien = promien

    def oblicz_pole(self):
        return(math.pi * self.promien**2)


figury = [Kwadrat(3), Kolo(2)]

for figura in figury:
    print(figura.oblicz_pole())