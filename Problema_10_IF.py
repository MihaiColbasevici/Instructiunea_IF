gaini, boabe = input("Dati numarul de gaini si de boabe: \t").split()
gaini = int(gaini)
boabe = int(boabe)
curcan = boabe % gaini
if (curcan > (boabe // gaini)):
    print("Curcanul a primit", curcan, "boabe. Mai mult cu", curcan - (boabe // gaini), "boabe decat gainile.")
elif (curcan == (boabe // gaini)):
    print("Fiecare gaina a primit cate", boabe // gaini, "boabe. EGALITATE!")
