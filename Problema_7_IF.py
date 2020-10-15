a, b, c = input("Dati 3 numere intregi: \t").split()
a = int(a)
b = int(b)
c = int(c)
if (a > 0) and (b > 0) and (c > 0):
    if (b > c):
        print(b)
    elif (c > b):
        print(c)
else:
    print(a + b)