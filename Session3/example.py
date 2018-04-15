# name1 = "Canh"
# name2 = "Hieu"
# name3 = "Duc Anh"
# name4 = "Nguyen"
# name5 = "Don"

# names = [] # để rỗng vì mình vẫn chưa biết nó chứa cái gì và sẽ thêm cái gì

# print(names)
# print(type(names))

names = ["Canh", "Hieu", "Duc Anh", "Don"]
# print(names)


#Creat
# names.append("Nguyen") #thêm vào list names
# print(names)
#
# new_name = "Don"
# names.append(new_name)
# print(names)


#Read
# x = 4
# x = 5
# y = x
# print(x)
# print(y)
#
# names[1] = "Hieu dep trai"
# n = names[1]
# print(n)
#
# print(names) #nghĩa là chỉ in ra phần tử đầu tiên của cái list đấy
# print(names[-1]) #in ra Duc Anh - nghĩa là nó sẽ đảo chiều - từ phải sang trái

# print(len(names)) #len = length - lấy số phần tử của list
# for i in range(len(names)):
#     print(names[i])


#vòng lặp foreach:


    # for name in names: #name là biến - đặt là gì cũng được
    #     print(name)

# for i in range(len(names)): #dùng for i
#     print(i,".", names[i])

no = 1
for n in names:
    #print(no,". ", n, sep="")
    #thay vì dùng sep như trên, dài dòng - ta dùng string format
    message = "{0}. {1}".format(no, n)
    print(message)
    no += 1 # no = no + 1
