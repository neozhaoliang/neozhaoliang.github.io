from piscript.PiModule import *
from math import *


SQRT3 = 3**0.5

def hexagon(r,g,b):
    newpath()
    v = Vector(0, 1)
    moveto(v)
    for i in range(5):
        v.rotate(pi/3)
        lineto(v)
    closepath()
    fill(r, g, b)
    stroke()

def bone1():
    init("bone1.eps", 150, 100)
    center()
    scale(25)
    for v in [(0, 0), (-SQRT3, 0), (SQRT3, 0)]:
        gsave()
        translate(v)
        hexagon(0, 1, 0)
        grestore()

    finish()

def bone2():
    init("bone2.eps", 150, 150)
    center()
    scale(25)
    for v in [(0, 0), (SQRT3/2, 1.5), (-SQRT3/2, -1.5)]:
        gsave()
        translate(v)
        hexagon(1, 0, 0)
        grestore()

    finish()

def bone3():
    init("bone3.eps", 150, 150)
    center()
    scale(25)
    for v in [(0, 0), (SQRT3/2, -1.5), (-SQRT3/2, 1.5)]:
        gsave()
        translate(v)
        hexagon(0, 0, 1)
        grestore()

    finish()
    
bone1()
bone2()
bone3()
