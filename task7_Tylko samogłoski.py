zdanie = input("Podaj zdanie: ")

for litera in zdanie:
    if litera.lower() not in "aeiouyąęó":
        continue

    print(litera)