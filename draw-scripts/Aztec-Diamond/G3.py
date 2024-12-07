from piscript.PiModule import *
from math import *

n = 3
r = 0.05
fs = 0.8
init(400, 400)
center()
scale(65)


def dot(p, color=(1, 1, 1)):
    newpath()
    circle(p, r)
    fill(*color)
    stroke()


def square(pts):
    newpath()
    moveto(pts[0])
    for p in pts[1:]:
        lineto(p)
    lineto(pts[0])
    closepath()
    stroke()


cells = []
for j in range(-n, n):
    k = min(n + 1 + j, n - j)
    for i in range(-k, k):
        cells.append((i, j))


a = 0.25
for i, j in cells:
    if (i + j + n) % 2 == 1:
        v = Vector(i + 0.5, j + 0.5)
        v1 = v + (a, a)
        v2 = v - (a, a)

    else:
        v = Vector(i + 0.5, j + 0.5)
        v1 = v + (a, -a)
        v2 = v - (a, -a)

    newpath()
    moveto(v1)
    lineto(v2)
    stroke()
    if (i + j + n) % 2 == 1 and (i + 1, j + 1) in cells:
        c = Vector(i + 1, j + 1)
        pts = [c + (-a, a), c + (a, a), c + (a, -a), c + (-a, -a)]
        square(pts)

    if (i + j + n) % 2 == 0:
        dot(v, (0, 0, 0))
        dot(v2, (1, 1, 1))
        dot(v1, (1, 1, 1))
    else:
        dot(v, (1, 1, 1))
        dot(v2, (0, 0, 0))
        dot(v1, (0, 0, 0))


for i, j in cells:
    if (i + j + n) % 2 == 1 and (i + 1, j + 1) in cells:
        newpath()
        t = texinsert(r"$y/\Delta$")
        t.scale(fs)
        place(t, i + 0.85, j + 1.3)

        newpath()
        t = texinsert(r"$x/\Delta$")
        t.scale(fs)
        place(t, i + 0.45, j + 0.95)

        newpath()
        t = texinsert(r"$z/\Delta$")
        t.scale(fs)
        place(t, i + 1.3, j + 0.95)

        newpath()
        t = texinsert(r"$w/\Delta$")
        t.scale(fs)
        place(t, i + 0.85, j + 0.6)

finish()
