#1
text = "overnight"
characters = list(text)
#characters = text.split("") #chia text ra thành từng kí tự

print(*characters, sep=" ")

#2
from random import choice #chọn ngẫu nhiên ra 1 từ bên trong list


print(choice(characters))
