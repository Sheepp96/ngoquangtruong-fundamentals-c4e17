from getpass import getpass #getpass là 1 thư viện - mình phải import vào để sử dụng
a = str(input("Input username: "))
b = getpass("Input password: ") #lệnh ẩn password

if a == "c4e":
    if b == "codethechange":
        print("---Welcome---")
    else:
        print("Wrong password - you can't login")
else:
    print("Wrong username - you can't login")
