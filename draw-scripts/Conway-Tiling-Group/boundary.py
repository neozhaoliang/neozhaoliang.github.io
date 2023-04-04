from piscript.PiModule import *
from math import *


sqrt3 = 3**0.5
FC = 1.2
n = 7
va = Vector(cos(pi/12*5), sin(pi/12*5)) * 0.55
vb = Vector(1, 0) * 0.4
vc = Vector(cos(pi/12*8), sin(pi/12*8)) * 0.65
R = (1.0, 0.3, 0)
G = (0.4, 1.0, 0.1)
B = (0.0, 0.5, 1.0)
L = [0, 1, 2, 3, 4, 5]


def hexagon(color=None, indices=L):
    newpath()
    v = Vector(0, 1)
    moveto(v)
    for i in range(5):
        v.rotate(pi/3)
        lineto(v)
    closepath()
    if color:
        fill(*color)
    stroke()

    if 0 in indices:
        t = texinsert("$a$")
        t.scale(FC)
        t.translate(1.5*t.width, t.height*1.7)
        place(t, va)

    if 1 in indices:
        t = texinsert("$a$")
        t.scale(FC)
        t.translate(-2.5*t.width, -t.height*2)
        place(t, -va*1.3)

    if 2 in indices:
        t = texinsert("$b$")
        t.scale(FC)
        t.translate(3.5*t.width, -t.height/2)
        place(t, vb)

    if 3 in indices:
        t = texinsert("$b$")
        t.scale(FC)
        t.translate(-t.width*2.2, -t.height/2)
        place(t, -vb*2)

    if 4 in indices:
        t = texinsert("$c$")
        t.scale(FC)
        t.translate(-2*t.width, t.height*1.5)
        place(t, vc)

    if 5 in indices:
        t = texinsert("$c$")
        t.scale(FC)
        t.translate(t.width, -t.height*2.75)
        place(t, -vc)


size = 400
init("boundary.eps", size, size)
scale(size / (1.5 * (n - 1) + 4))
translate(n * sqrt3 / 4 - sqrt3, n * sqrt3 / 4 -1)

for i in range(0, n):
    for k in range(n-i):
        gsave()
        translate((k+0.5*i) * sqrt3, 1.5*i )
        if 1 <= i <= n-2:
            if k == 0:
                hexagon(indices=[3, 4])
            elif k == n-i-1:
                hexagon(indices=[0, 2])
            else:
                hexagon(indices=[])
        elif i == 0:
            if k == 0:
                hexagon(indices=[1, 3, 4, 5])
            elif k == n-1:
                hexagon(indices=[1, 0, 2, 5])
            else:
                hexagon(indices=[1, 5])
        elif i == n - 1:
            hexagon(indices=[0, 2, 3, 4])

        grestore()

newpath()
an = pi/6
circle(-cos(an), -sin(an), 0.1)
fill(1, 0, 1)
stroke()

finish()