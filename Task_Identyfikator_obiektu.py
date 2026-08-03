a = 256
b = 256
c = 256

print(id(a))
print(id(b))
print(id(c))

a = 257
b = 257
c = 257

print(id(a))
print(id(b))
print(id(c))

# Python często przechowuje małe liczby całkowite jako wspólne obiekty.
# Dlatego liczba 256 może mieć taki sam identyfikator dla kilku zmiennych.
# Przy liczbie 257 zachowanie może być inne, zależnie od wersji Pythona
# i sposobu uruchomienia programu.