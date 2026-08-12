from dataclasses import dataclass

@dataclass
class Film:
    tytul: str
    rezyser: str
    rok: int

Batman = Film("Mroczny Rycerz", "Christopher Nolan", 2008)
Odyseja = Film("Odyseja", "Christopher Nolan", 2026)

print(Batman)
print(Odyseja)