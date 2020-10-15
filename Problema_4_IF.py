a, b, c = input("Dati 3 varste. \t").split()
a = int(a)
b = int(b)
c = int(c)
if (a >= 18) and (a <= 60):
    print(a)
elif (b >= 18) and (b <= 60):
    print(b)
elif (c >= 18) and (c <= 60):
    print(c)
else:
    print("Gandeste-te la ce-ai facut...")