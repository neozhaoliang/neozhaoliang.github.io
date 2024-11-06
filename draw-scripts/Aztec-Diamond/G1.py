from piscript.PiModule import *
from math import *

n = 4
r = 0.08
init(400, 400)
center()
scale(55)

def square(pts):
    newpath()
    moveto(pts[0])
    for p in pts[1:]:
        lineto(p)
    lineto(pts[0])
    closepath()
    fill(1, 0.75, 0.75)
    stroke()

cells = []
for j in range(-n, n):
    k = min(n+1+j, n-j)
    for i in range(-k, k):
        cells.append((i, j))

rotate(pi/4)
a = 0.25
for i, j in cells:
    if (i + j + n) % 2 == 1:
        v = Vector(i+0.5, j+0.5)
        v1 = v + (a, a)
        v2 = v - (a, a)
        
    else:
        v = Vector(i+0.5, j+0.5)
        v1 = v + (a, -a)
        v2 = v - (a, -a)

    newpath()
    moveto(v1)
    lineto(v2)
    stroke()
    if (i + j + n) % 2 == 1 and (i+1, j+1) in cells:
        c = Vector(i+1, j+1)
        pts = [c + (-a, a), c + (a, a), c + (a, -a),  c+(-a, -a)]
        square(pts)

    for p in [v, v1, v2]:
        newpath()
        circle(p, r)
        fill(1, 0, 0)
        stroke()

finish()
