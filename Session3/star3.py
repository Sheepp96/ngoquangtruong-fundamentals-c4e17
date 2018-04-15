a = int(input("Input a: "))
b = int(input("Input b: "))
c = "*"
d = "o"

for i in range(a): #i đại diện cho số hàng
    for j in range(b): #j đại diện cho số cột
        if (i+j) % 2 != 0:
            print(d, end =" ")
        else:
            print(c, end =" ")

    print(end='\n')
