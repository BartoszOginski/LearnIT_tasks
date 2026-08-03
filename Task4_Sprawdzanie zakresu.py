POZIOM_DOSTEPU = "user"

def zmiana_dostępu():
    POZIOM_DOSTEPU = "admin"
    print(f"Wewnątrz funkcji: {POZIOM_DOSTEPU}")

zmiana_dostępu()

print(f"Na zewnątrz funkcji: {POZIOM_DOSTEPU}")