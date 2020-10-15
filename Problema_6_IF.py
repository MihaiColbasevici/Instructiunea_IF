a, b, c = input("Ce note a primit Gigel? \t").split()
a = int(a)
b = int(b)
c = int(c)
if (c >= 8):
    print("Gigel le-a spus parintilor ca a primit un", a, ", un", b, "si un", c)
elif (c < 8):
    if (a > b):
        print("Gigel le-a spus parintilor ca a primit un", a)
    elif (a < b):
        print("Gigel le-a spus parintilor ca a primit un", b)
    elif (a == b):
        print("Gigel le-a spus parintilor ca a primit un", a)
elif (a < 0) or (a > 10) or (b < 0) or (b > 10) or (c < 0) or (c > 10):
    print("In Moldova, notele sunt doar de la 1 la 10!")