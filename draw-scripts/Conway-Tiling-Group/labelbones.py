from piscript.PiModule import *
from math import *


SQRT3 = 3**0.5
FC = 1.5
va = Vector(cos(pi/12*5), sin(pi/12*5)) * 0.55
vb = Vector(1, 0) * 0.4
vc = Vector(cos(pi/12*8), sin(pi/12*8)) * 0.65

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

    t = texinsert("$a$")
    t.scale(FC)
    t.translate(t.width/2, 0)
    place(t, va)

    t = texinsert("$a$")
    t.scale(FC)
    t.translate(-t.width*2, 0)
    place(t, -va*1.3)

    t = texinsert("$b$")
    t.scale(FC)
    t.translate(t.width*2, -t.height/2)
    place(t, vb)

    t = texinsert("$b$")
    t.scale(FC)
    t.translate(t.width/2, -t.height/2)
    place(t, -vb*2)

    t = texinsert("$c$")
    t.scale(FC)
    t.translate(-t.width, -t.height/2)
    place(t, vc)

    t = texinsert("$c$")
    t.scale(FC)
    t.translate(-t.width*1.3, -t.height/2)
    place(t, -vc*1.1)



def bone1():
    init("bone1.eps", 300, 200)
    center()
    scale(50)
    for v in [(0, 0), (-SQRT3, 0), (SQRT3, 0)]:
        gsave()
        translate(v)
        hexagon(0, 1, 0)
        grestore()

    finish()

def bone2():
    init("bone2.eps", 300, 300)
    center()
    scale(50)
    for v in [(0, 0), (SQRT3/2, 1.5), (-SQRT3/2, -1.5)]:
        gsave()
        translate(v)
        hexagon(1, 0, 0)
        grestore()

    finish()

def bone3():
    init("bone3.eps", 300, 300)
    center()
    scale(50)
    for v in [(0, 0), (SQRT3/2, -1.5), (-SQRT3/2, 1.5)]:
        gsave()
        translate(v)
        hexagon(0, 0, 1)
        grestore()

    finish()
    
bone1()
bone2()
bone3()
