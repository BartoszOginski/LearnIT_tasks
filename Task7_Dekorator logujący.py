def loguj(funkcja):
    def wrapper():
        print(f"Uruchamian funkcję {funkcja.__name__}...")
        funkcja()
        print(f"Zakończono funkjcę {funkcja.__name__}")
    return wrapper

@loguj
def powitanie():
    print("Witaj")

powitanie()