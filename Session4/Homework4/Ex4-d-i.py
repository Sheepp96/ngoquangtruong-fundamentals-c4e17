a = 1
b = 0

for i in range(10):
    for j in range(10):
        if (i+j) % 2 != 0:
            print(a, end = "\t")
        else:
            print(b, end = "\t")
    print()
