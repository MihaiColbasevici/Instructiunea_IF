bami = int(input("Numarul bilelor albe mici: "))
bama = int(input("Numarul bilelor albe mari: "))
brmi = int(input("Numarul bilelor rosii mici: "))
brma = int(input("Numarul bilelor rosii mari: "))
bvmi = int(input("Numarul bilelor verzi mici: "))
bvma = int(input("Numarul bilelor verzi mari: "))
print("Pe masa sunt", bami + bama + brmi + brma + bvmi + bvma)
ba = bami + bama
br = brmi + brma
bv = bvmi + bvma
bmi = bami + brmi + bvmi 
bma = bama + brma + bvma
if (bmi > bma):
    print("Bilele mici sunt mai numeroase.")
elif (bma > bmi):
    print("Bilele mari sunt mai numeroase.")

if (ba > br) and (ba > bv):
    print("Albe:", ba)
elif (br > ba) and (br > bv):
    print("Rosii:", br)
elif (bv > ba) and (bv > br):
    print("Verzi:", bv)
elif (ba == br) and (ba > bv):
    print("Albe si rosii:", ba)
elif (ba == bv) and (ba > br):
    print("Albe si verzi:", ba)
elif (br == bv) and (br > ba):
    print("Rosii si verzi:", br)
