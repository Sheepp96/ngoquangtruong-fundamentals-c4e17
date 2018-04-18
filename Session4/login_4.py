n = 0
while n < 4:
    a = str(input("Input username: "))
    b = str(input("Input password: "))

    if a == "c4e":
        if b == "codethechange":
            print("Welcome - you're login")
            break
        else:
            print("Wrong password - you can't login")
    else:
        print("Wrong username - you can't login")

    n += 1
    if n == 4:
        print("Error so many times, out of system")
        break #chỉ tác động với vòng lặp gần nhất
