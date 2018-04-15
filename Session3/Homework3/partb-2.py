from turtle import *

speed()

colors = ['red', 'blue', 'brown', 'yellow', 'gray']


# for a in range(2):
#     color(colors[0])
#     begin_fill()
#     forward(50)
#     lt(90)
#     forward(100)
#     lt(90)
#     forward(50)
#     end_fill()
#
# for b in range(2):
#     color(colors[1])
#     begin_fill()
#     forward(50)
#     lt(90)
#     forward(100)
#     lt(90)
#     forward(50)
#     end_fill()
#
# for c in range(2):
#     color(colors[2])
#     begin_fill()
#     forward(50)
#     lt(90)
#     forward(100)
#     lt(90)
#     forward(50)
#     end_fill()
#
# for d in range(2):
#     begin_fill()
#     color(colors[3])
#     forward(50)
#     lt(90)
#     forward(100)
#     lt(90)
#     forward(50)
#     end_fill()
#
# for e in range(2):
#     color(colors[4])
#     begin_fill()
#     forward(50)
#     lt(90)
#     forward(100)
#     lt(90)
#     forward(50)
#     end_fill()

for i in range(5):
    color(colors[i])
    begin_fill()
    for j in range(2):
        forward(60)
        lt(90)
        forward(120)
        lt(90)
    forward(60)
    end_fill()

mainloop()
