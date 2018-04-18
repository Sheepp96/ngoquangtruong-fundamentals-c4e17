loop = True
while loop:

    a = str(input("Input username: "))
    b = str(input("Input password: "))

    if a == "c4e":
        if b == "codethechange":
            print("Welcome - you're login")
            loop = False # ngắt vòng lặp. không dùng break vì break chỉ dùng được với vòng lặp gần nhất
        else:
            print("Wrong password - you can't login")
    else:
        print("Wrong username - you can't login")
