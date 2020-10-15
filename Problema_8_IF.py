a, b = input("Dati 2 numere. \t").split()
a = int(a)
b = int(b)
if (a % 2 == 0) and (b % 2 == 0):
    if (a > b):
        print(a)
    elif (b > a):
        print(b)
    elif (a == b):
        print(a)
elif (a % 2 == 0) and (b % 2 != 0):
    print(a)
elif (a % 2 != 0) and (b % 2 == 0):
    print(b)
elif (a % 2 != 0) and (b % 2 != 0):
    print("Nu exista numere pare.")
