while True:
    tekst = str(input("Co chciałbyś dodać: "))
    with open("dziennik.txt", "a", encoding="utf-8") as f:
        f.write(tekst + "\n")

    dalej = str(input("Czy chciałbyś coś jeszcze dodać (tak/nie)?"))

    if dalej.lower() == "nie":
        break