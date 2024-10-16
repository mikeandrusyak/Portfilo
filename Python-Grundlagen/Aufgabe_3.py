from turtle import *

def Spirale(width):
    for i in range(width,0,-1):
        forward(i)
        left(45)

Spirale(100)
done()