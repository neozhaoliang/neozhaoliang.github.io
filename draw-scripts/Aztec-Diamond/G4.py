from piscript.PiModule import *
from math import *

n = 3
r = 0.05
init(300, 300)
center()
scale(50)
fs = 0.8


def rectangle(x1, y1, x2, y2, gray):
    newpath()
    moveto(x1, y2)
    lineto(x1, y1)
    lineto(x2, y1)
    stroke()


cells = []
for j in range(-n, n):
    k = min(n + 1 + j, n - j)
    for i in range(-k, k):
        cells.append((i, j))

for i, j in cells:
    if (
        (i + j + n) % 2 == 0
        and (i + 1, j + 1) in cells
        and (i - 1, j) in cells
        and (i, j - 1) in cells
    ):
        newpath()
        moveto(i + 0.5, j + 0.5)
        lineto(i + 0.5, j + 1.5)
        lineto(i + 1.5, j + 1.5)
        lineto(i + 1.5, j + 0.5)
        lineto(i + 0.5, j + 0.5)
        closepath()
        stroke()

    if (i, j + 1) in cells:
        newpath()
        moveto(i + 0.5, j + 0.5)
        lineto(i + 0.5, j + 1.5)
        stroke()

    if (i + 1, j) in cells:
        newpath()
        moveto(i + 0.5, j + 0.5)
        lineto(i + 1.5, j + 0.5)
        stroke()

    newpath()
    circle(i + 0.5, j + 0.5, r)
    if (i + j + n) % 2 == 0:
        fill(1)
    else:
        fill(0)
    stroke()

for i, j in cells:
    if (i + j + n) % 2 == 1 and (i + 1, j + 1) in cells:
        newpath()
        t = texinsert(r"$y/\Delta$")
        t.scale(fs)
        place(t, i + 0.8, j + 1.6)

        newpath()
        t = texinsert(r"$x/\Delta$")
        t.scale(fs)
        place(t, i + 0.1, j + 0.95)

        newpath()
        t = texinsert(r"$z/\Delta$")
        t.scale(fs)
        place(t, i + 1.55, j + 0.95)

        newpath()
        t = texinsert(r"$w/\Delta$")
        t.scale(fs)
        place(t, i + 0.8, j + 0.3)


finish()
