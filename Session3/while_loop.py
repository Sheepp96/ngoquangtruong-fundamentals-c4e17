from getpass import getpass

while True: #while true tức là lặp vô hạn - không bao giờ có điểm dừng
    a = str(input("Input username: "))
    b = getpass("Input password: ")

    if a == "c4e":
        if b == "codethechange":
            print("---Welcome---")
            break #muốn thoát ở đâu thì dùng lệnh break
        else:
            print("Wrong password - you can't login")
    else:
        print("Wrong username - you can't login")
