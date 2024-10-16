from turtle import *

def tortoise(rules):
    for i in rules:
        left(i[0])
        forward(i[1])

tortoise([(0, 30), (60, 50), (-120, 50), (60, 30)])
done()