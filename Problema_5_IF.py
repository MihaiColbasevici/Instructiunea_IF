zc, lc, ac = input("Dati data curenta (cifrele sa fie separate prin puncte) \t").split('.')
zn, ln, an = input("Dati data nasterii \t").split('.')
zc = int(zc)
lc = int(lc)
ac = int(ac)
zn = int(zn)
ln = int(ln)
an = int(an)
if (zc > 31) or (zn > 31) or (ln > 12) or (lc > 12) or (ac < an):
    print("Gandeste-te la ce-ai facut...")
elif (lc > ln):
    if (zc < zn):
        print((ac - an) - 1, "ani.")
    elif (zc > zn):
        print((ac - an), "ani.")
    elif (zc == zn):
        print(ac - an, "ani.")
elif (lc < ln):
    if (zc < zn):
        print((ac - an) - 1, "ani.")
    elif (zc > zn):
        print((ac - an) - 1, "ani.")
    elif (zc == zn):
        print((ac - an) - 1, "ani.")
elif (lc == ln):
    if (zc < zn):
        print((ac - an) - 1, "ani.")
    elif (zc > zn):
        print((ac - an), "ani.")
    elif (zc == zn):
        print((ac - an), "ani.")
