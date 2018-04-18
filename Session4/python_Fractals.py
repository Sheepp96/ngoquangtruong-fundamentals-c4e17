from turtle import *

speed()
color('black')

begin_fill()

for a in range(3):
    forward(60)
    lt(120)
for b in range(3):
    rt(60)
    forward(60)

end_fill()

mainloop()
