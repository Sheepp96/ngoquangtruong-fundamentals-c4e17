from turtle import *

color("red")
shape("turtle")
speed()

for i in range(20):
    if i % 2 == 0:
        penup()
        forward(10)
    else:
        pendown()
        forward(10)

mainloop()
