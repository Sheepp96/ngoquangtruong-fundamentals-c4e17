numbers = [1, 6, 8, 1, 2, 1, 5, 6, 2, 10, 3, 2, 4, 5, 6]

a = 0
b = int(input("Input a number: "))
for i in range(len(numbers)):

    if numbers[i] == b:
        a += 1

message=''' {0} appears {1} in my list'''.format(b, a)
print(message)
