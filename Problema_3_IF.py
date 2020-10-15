lit = input("Dati o litera. \t")
alfa_vocala = ['A', 'a',  'E', 'e', 'I', 'i', 'Î', 'î', 'O', 'o', 'U', 'u', 'Y', 'y', 'Ă', 'ă', 'î', 'î']
alfa_consoana = ['B', 'b', 'C', 'c', 'D', 'd','F', 'f', 'G', 'g', 'H', 'h', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'Ș', 'ș', 'T', 't', 'Ț', 'ț', 'V', 'v', 'W', 'w', 'X', 'x', 'Z', 'z', ]
if (lit in alfa_vocala):
    print("Vocala.")
elif (lit in alfa_consoana):
    print("Consoana.")
else:
    print(lit, "nu e o litera.")