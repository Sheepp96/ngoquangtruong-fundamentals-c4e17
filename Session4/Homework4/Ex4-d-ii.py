n = int(input("Input a number: "))
a = 1
b = 0

for i in range(n):
    for j in range(n):
        if (i+j) % 2 != 0:
            print(a, end = "\t")
        else:
            print(b, end = "\t")

    print()
