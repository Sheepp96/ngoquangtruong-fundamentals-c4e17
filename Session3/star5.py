a = int(input("Input a: "))

for i in range(a):
    for j in range(a):
        if j <= i:
            print("* ", end = " ")
        else:
            print(" ", end = " ")
    print()
