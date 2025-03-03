from piscript.PiModule import *
from math import *


SQRT3 = 3**0.5

R = (1.0, 0.3, 0)
G = (0.4, 1.0, 0.1)
B = (0.0, 0.5, 1.0)


def hexagon(color):
    newpath()
    v = Vector(0, 1)
    moveto(v)
    for i in range(5):
        v.rotate(pi/3)
        lineto(v)
    closepath()
    fill(*color)
    stroke()


init("bone.eps", 500, 200)
center()
scale(30)
for v in [(0, 0), (-SQRT3, 0), (SQRT3, 0)]:
    gsave()
    translate(v)
    hexagon(G)
    grestore()


a = 5.5
gsave()
translate(-a, 0)
for v in [(0, 0), (SQRT3/2, 1.5), (-SQRT3/2, -1.5)]:
    gsave()
    translate(v)
    hexagon(R)
    grestore()
grestore()

gsave()
translate(a, 0)
for v in [(0, 0), (SQRT3/2, -1.5), (-SQRT3/2, 1.5)]:
    gsave()
    translate(v)
    hexagon(B)
    grestore()
grestore()

finish()