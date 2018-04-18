a = 1
b = 0

n = int(input("Input the total number of 1's and 0's : "))

for i in range(n):
    if i % 2 != 0:
        print(a, end = " ")
    else:
        print(b, end = " ")
