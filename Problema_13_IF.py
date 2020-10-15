x = int(input("Ce loc a luat Ionel? \t"))
if (x - (x // 4) * 4 == 1):
    print("Ionel a primit un tricou alb.")
if (x - (x // 4) * 4 == 2):
    print("Ionel a primit un tricou rosu.")
if (x - (x // 4) * 4 == 3):
    print("Ionel a primit un tricou albastru.")
if (x - (x // 4) * 4 == 0):
    print("Ionel a primit un tricou negru.")