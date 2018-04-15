items = ['T-Shirt', 'Sweater']

while True:

    print("Welcome to our shop, what do u want?")
    print("Our items: ", end = "")
    print(*items, sep=", ")

    a = str(input("Enter new iteam: "))
    items.append(a)
    print("Our items: ", end = "")
    print(*items, sep=", ")

    b = int(input("Update position: "))
    c = str(input("Input new item: "))
    items[b] = c
    print("Our items: ", end = "")
    print(*items, sep=", ")

    d = int(input("Delete position: "))
    del items[d]
    print("Our items: ", end ="")
    print(*items, sep=", ")
