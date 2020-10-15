a = int(input("Pe ce loc se afla Radu? \t"))
if (a <= 25):
    print("Radu este in clasa A.")
elif (a > 25) and (a <= 50):
    print("Radu este in clasa B.")
elif (a > 50) and (a <= 75):
    print("Radu este in clasa C.")
elif (a > 75) and (a <= 100):
    print("Radu este in clasa D.")
elif (a > 100) and (a <= 125):
    print("Radu este in clasa E.")
elif (a < 0) or (a > 100):
    print("Alegeti alt numar.")