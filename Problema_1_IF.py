n1 = int(input("nr crt "))
p1 = int(input("punctaj"))
n2 = int(input("nr crt"))
p2 = int(input("punctaj"))
n3 = int(input("nr crt"))
p3 = int(input("punctaj"))
if (p1 > 0) and (p2 > 0) and (p3 > 0):
    if (p1 > p2) and (p1 > p3):
        print("Punctaj maxim are elevul cu nr crt", n1)
    elif (p2 > p1) and (p2 > p3):
        print("Punctaj maxim are elevul cu nr crt", n2)
    elif (p3 > p1) and (p3 > p2):
        print("Punctaj maxim are elevul cu nr crt", n3)
    elif (p1 == p2) and (p1 > p3):
        print("Punctaj maxim are elevul cu nr crt", n1, n2)
    elif (p1 == p3) and (p1 > p2):
        print("Punctaj maxim are elevul cu nr crt",n1, n3)
    elif (p3 == p2) and (p3 > p1):
        print("Punctaj maxim are elevul cu nr crt",n2, n3)
else: 
    print("Punctajul trebuie sa fie pozitiv.")