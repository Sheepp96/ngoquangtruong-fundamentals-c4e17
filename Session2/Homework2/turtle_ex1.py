from turtle import *

color("red")

speed()

for i in range(4):
    lt(30)
    forward(90)
    rt(60)
    forward(90)
    rt(120)
    forward(90)
    rt(60)
    forward(90)

    if i in range(3):
        lt(120)

mainloop()
