menu = ['pho', 'com rang', 'my xao', 'bun rieu']

print(*menu, sep=", ")

#creat

menu.append('hu tieu')
print("After append: ", end ="")
print(*menu, sep=", ")

#fori

for i in range(len(menu)):  #range này chỉ sinh ra số - int
    print(menu[i])
print()

#foreach

for item in menu:   # item lấy trực tiếp các giá trị trong mảng
                    # for i thì i chắc chắn là int
                    # item thì sẽ phụ thuộc vào list. giá trị của từng phần tử trong list
                    # là gì thì item sẽ có giá trị đấy
    print(item)
print()

#for enum - đặc trưng riêng của python

name = "truong"
age = 22
status = "not single"
address = "dinh cong str"

# print(name + str(age) + status + address)

message = '''name: {0}
tuoi: {1}
tinh trang quan he: {2}
dia chi: {3}'''.format(name, age, status, address)
print(message)
# for i, item in enumerate(menu):
#     message = "{0}. {1}".format((i + 1), item)
#     print(message)
#     i += 1
