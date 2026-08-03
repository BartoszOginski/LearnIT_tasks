liczba_pierwsza = float(input("Podaj pierwszą liczbę: "))
znak = str(input("Jaką czynność chcesz wykonać: (+, -, *, /): "))
liczba_druga = float(input("Podaj drugą liczbę: "))
if znak == "+":
 print("Wynik: ",liczba_pierwsza + liczba_druga)
elif znak == "-":
 print("Wynik: ",liczba_pierwsza - liczba_druga)
elif znak == "*":
 print("Wynik: ",liczba_pierwsza * liczba_druga)
elif znak == "/":
 print("Wynik: ",liczba_pierwsza / liczba_druga)