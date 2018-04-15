
names = ["Book", "Games", "Football"]
print("Here your favorite thing: ", end=" ")
print(*names, sep=", ") #thêm dấu * để python biết là nó phải in ra từng phần tử 1
                        #sep là seperate, ngăn cách các phần tử
a = str(input("Hi there, add your favorite thing: "))

names.append(a)
print(*names, sep=", ")
