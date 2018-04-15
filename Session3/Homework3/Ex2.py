sizes = [5, 7, 300, 90, 24, 50, 75]

n = int(input("Input number of month: "))
for i in range(n):
    print("Hello, i'm Truong and these are my sheep sizes: ", end="")
    print(*sizes, sep=", ")


    print("Now my biggest sheep has size ", max(sizes), end =". ")
    print("Let's shear it")


    print("After shearing, here is my flock: ", end ="")
    a = sizes.index(max(sizes))
    sizes[a] = 8
    print(*sizes, sep=", ")


    print("One month has passed, now here is my flock: ", end ="")
    for j in range(len(sizes)):
        sizes[j] = sizes[j] + 50
    print(*sizes, sep=", ")

    print("My flock has size in total: ", end="")
    total = sum(sizes)
    print(total)

    print("I would get: ", end="")
    price = total * 2
    print(price)
    print()
