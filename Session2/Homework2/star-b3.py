n = int(input("Input n: "))
a = "*"
b = "x"
c = int(n/2)
if n % 2 == 0:
    for i in range(n):
        print(a, b, end =" "),
    print("Total x and * is: ", 2 * n)
else:
    for i in range(c):
        print(a, b, end =" "),
    print("Toltal x and * is: ", (n * 2) - 1)
