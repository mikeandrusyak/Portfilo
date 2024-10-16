from math import pi
from turtle import *

def turn(step):
    for i in range(18):
        forward(step * pi / 36)
        right(10)

left(90)
forward(250)
right(90)
turn(100)
forward(100 * pi / 36)
left(180)
turn(150)
forward(150 * pi / 36)
left(180)
done()
