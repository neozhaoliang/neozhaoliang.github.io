from piscript.PiModule import *
from math import *


SQRT3 = 3**0.5
FC = 1.5
va = Vector(cos(pi/12*5), sin(pi/12*5)) * 0.55
vb = Vector(1, 0) * 0.4
vc = Vector(cos(pi/12*8), sin(pi/12*8)) * 0.65

def hexagon(r,g,b, l1, l2):
    newpath()
    v = Vector(0, 1)
    moveto(v)
    for i in range(5):
        v.rotate(pi/3)
        lineto(v)
    closepath()
    #fill(r, g, b)
    stroke()

    t = texinsert(l1)
    t.scale(FC)
    t.translate(t.width/2, 0)
    place(t, va)

    t = texinsert(l2)
    t.scale(FC)
    t.translate(-t.width*2, 0)
    place(t, -va*1.3)

    t = texinsert(l2)
    t.scale(FC)
    t.translate(t.width*2, -t.height/2)
    place(t, vb)

    t = texinsert(l1)
    t.scale(FC)
    t.translate(t.width/2, -t.height/2)
    place(t, -vb*2)

    t = texinsert(l2)
    t.scale(FC)
    t.translate(-t.width, -t.height/2)
    place(t, vc)

    t = texinsert(l1)
    t.scale(FC)
    t.translate(-t.width*1.3, -t.height/2)
    place(t, -vc*1.1)



def main():
    init(300, 300)
    center()
    scale(50)
    gsave()
    hexagon(0, 1, 0, "$a$", "$c$")
    grestore()
    #for v in [(0, 0), (-SQRT3, 0), (SQRT3, 0), (SQRT3/2, 1.5), (SQRT3/2, -1.5), (-SQRT3/2, -1.5), (-SQRT3/2, 1.5)]:

    for v in [(-SQRT3, 0), (SQRT3/2, 1.5), (SQRT3/2, -1.5)]:
        gsave()
        translate(v)
        hexagon(0, 1, 0, "$b$", "$a$")
        grestore()

    for v in [(SQRT3, 0), (-SQRT3/2, -1.5), (-SQRT3/2, 1.5)]:
        gsave()
        translate(v)
        hexagon(0, 1, 0, "$c$", "$b$")
        grestore()
    finish()

main()
