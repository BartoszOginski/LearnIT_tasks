class Wektor2D:
    def __init__(self, x, y):
        self.x = x
        self.y= y

    def __str__(self):
        return f"współrzędne ({self.x},{self.y})"

    def __add__(self, other):
        if isinstance (other, Wektor2D):
            return self.x + other.x, self.y + other.y
        return NotImplemented

    def __sub__(self, other):
        if isinstance (other, Wektor2D):
            return self.x - other.y,  self.y - other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        

wektor1 = Wektor2D(5,12)
wektor2 = Wektor2D (3,3)

suma_wektorow = wektor1 + wektor2
roznica_wektorow = wektor1- wektor2

print(wektor1)
print(wektor2)
print(suma_wektorow)
print(roznica_wektorow)
print(wektor1 == wektor2)