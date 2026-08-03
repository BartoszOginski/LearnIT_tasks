def powtorz(n):
    def powtorzenie(funkcja):
        def wrapper():
            for i in range(n):
                funkcja()
        return wrapper
    return powtorzenie

@powtorz(3)
def przywitanie():
    print("Witaj")

przywitanie()