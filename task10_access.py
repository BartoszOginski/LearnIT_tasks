wzrost = float(input("Jaki jest wzrost dziecka (w cm): "))
opiekun = str(input("Czy z dzieckiem jest opiekun (tak/nie)?: "))
if (wzrost >= 120 and opiekun == "tak" or wzrost >= 160):
    print("True")
else:
    print ("False")