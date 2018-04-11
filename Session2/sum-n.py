#cách 2
n = int(input("Input n: "))
m = 0
for i in range(n):
    m = (i+1) + m
print("Tong la: ", m)

#cách 1

n = int(input("Enter a number: "))
n_range= range(n+1) #khoảng, dãy số từ 0 đến n
total = sum(n_range) #sum(0,n): không chạy
print(total)
