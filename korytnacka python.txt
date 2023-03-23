from turtle import *

delay(0)

def kresli(n, d):
    if n <= 0:
        return
    for i in range(0, 4):
        kresli(n - 1, d / 3)
        forward(d)
        left(90)

kresli(6, 200)
