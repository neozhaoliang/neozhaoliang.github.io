from piscript.PiModule import *
from math import *


SQRT3 = 3**0.5
FC = 1.2
va = Vector(cos(pi/12*5), sin(pi/12*5)) * 0.55
vb = Vector(1, 0) * 0.4
vc = Vector(cos(pi/12*8), sin(pi/12*8)) * 0.65
R = (1.0, 0.3, 0)
G = (0.4, 1.0, 0.1)
B = (0.0, 0.5, 1.0)


def circ(x, y, rad, col):
    newpath()
    circle(x, y, rad)
    fill(*col)
    stroke()


def hexagon(color, indices):
    newpath()
    v = Vector(0, 1)
    moveto(v)
    for i in range(5):
        v.rotate(pi/3)
        lineto(v)
    closepath()
    fill(*color)
    stroke()

    if 0 in indices:
        t = texinsert("$a$")
        t.scale(FC)
        t.translate(0, 0)
        place(t, va)

    if 1 in indices:
        t = texinsert("$a$")
        t.scale(FC)
        t.translate(-t.width, 0)
        place(t, -va*1.3)

    if 2 in indices:
        t = texinsert("$b$")
        t.scale(FC)
        t.translate(t.width, -t.height/2)
        place(t, vb)

    if 3 in indices:
        t = texinsert("$b$")
        t.scale(FC)
        t.translate(0, -t.height/2)
        place(t, -vb*2)

    if 4 in indices:
        t = texinsert("$c$")
        t.scale(FC)
        t.translate(-t.width, -t.height/2)
        place(t, vc)

    if 5 in indices:
        t = texinsert("$c$")
        t.scale(FC)
        t.translate(-t.width*1.3, -t.height/2)
        place(t, -vc*1.1)


init("bone.eps", 500, 200)
center()
scale(30)
for i, v in enumerate([(0, 0), (-SQRT3, 0), (SQRT3, 0)]):
    gsave()
    translate(v)
    hexagon(G, [0, 1, 2, 3, 4, 5])
    if i == 1:
        circ(-cos(pi/6), -sin(pi/6), 0.1, (1, 0, 1))
    grestore()

a = 5.5
gsave()
translate(-a, 0)
for i, v in enumerate([(0, 0), (SQRT3/2, 1.5), (-SQRT3/2, -1.5)]):
    gsave()
    translate(v)
    hexagon(R, [0, 1, 2, 3, 4, 5])
    if i == 2:
        circ(0, -1, 0.1, (1, 0, 1))
    grestore()
grestore()

gsave()
translate(a, 0)
for i, v in enumerate([(0, 0), (SQRT3/2, -1.5), (-SQRT3/2, 1.5)]):
    gsave()
    translate(v)
    hexagon(B, [0, 1, 2, 3, 4, 5])
    if i == 1:
        circ(cos(pi/6), -sin(pi/6), 0.1, (1, 0, 1))
    grestore()
grestore()

finish()