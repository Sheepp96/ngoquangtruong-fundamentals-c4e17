from turtle import *

speed()

colors = ['red', 'blue', 'brown', 'yellow', 'gray']

# color(colors[0])
# forward(120)
# lt(120)
# forward(120)
# lt(120)
# forward(120)
#
# color(colors[1])
# lt(120)
# forward(120)
# for a in range(4):
#     lt(90)
#     forward(120)
#
# color(colors[2])
# for b in range(5):
#     lt(72)
#     forward(120)
#
# color(colors[3])
# for c in range(6):
#     lt(60)
#     forward(120)
#
# color(colors[4])
# for d in range(7):
#     lt(float(360/7))
#     forward(120)

for i in range(5):
    color(colors[i])
    for j in range(i + 3):
        forward(120)
        lt(360/(i+3))

mainloop()
