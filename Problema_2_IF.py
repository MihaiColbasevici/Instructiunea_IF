a, b, c = input("Dati 3 numere \t").split()
a = int(a)
b = int(b)
c = int(c)
if (a < 32000) and (b < 32000) and (c < 32000) and (a > 0) and (b > 0) and (c > 0):
    if ((a + b) >= c) and ((a + c) >= b) and ((b + c) >= a):
        print("Da")
    elif (a + b < c) or (a + c < b) or (b + c < a):
        print("Nu")
else:
    print("Dati alte numere.")