while True:
    m = int(input("Input m: "))
    n = int(input("Input n: "))
    o = "*"
    for i in range(m):
        for j in range(n):
            print(o, end=" ")
        print(end='\n')
