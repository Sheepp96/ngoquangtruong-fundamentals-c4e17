from turtle import *

shape("turtle")
speed(0)

for i in range(0, 100 , 5): #thay i bằng _ : nghĩa là không quan tâm tới số lần lặp
    forward(5+i)
    lt(90)


mainloop()
