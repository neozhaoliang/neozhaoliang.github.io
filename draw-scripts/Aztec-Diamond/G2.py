from piscript.PiModule import *
from math import *

n = 3
r = 0.05
init(400, 400)
center()
scale(60)
# translate(0, 0.4)
fs = 1.5
lc = (0, 0, 1)


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

    if (i + j + n) % 2 == 1:
        if (i, j + 1) not in cells:
            newpath()
            moveto(i + 0.5, j + 0.5)
            lineto(i + 1, j + 1)
            stroke(*lc)
            newpath()
            circle(i + 1, j + 1, r)
            fill(0)
            stroke()
            t = texinsert("$1$")
            t.scale(fs)
            t.translate(-t.width / 2, -t.height / 2)
            place(t, i + 0.75, j + 0.75)

        if (i, j - 1) not in cells:
            newpath()
            moveto(i + 0.5, j + 0.5)
            lineto(i, j)
            stroke(*lc)
            newpath()
            circle(i, j, r)
            fill(0)
            stroke()
            t = texinsert("$1$")
            t.scale(fs)
            t.translate(-t.width / 2, -t.height / 2)
            place(t, i + 0.25, j + 0.25)
    else:
        if (i - 1, j) not in cells:
            newpath()
            moveto(i + 0.5, j + 0.5)
            lineto(i, j + 1)
            stroke(*lc)
            newpath()
            circle(i, j + 1, r)
            fill(1)
            stroke()
            t = texinsert("$1$")
            t.scale(fs)
            t.translate(-t.width / 2, -t.height / 2)
            place(t, i + 0.25, j + 0.75)

        if (i, j - 1) not in cells:
            newpath()
            moveto(i + 0.5, j + 0.5)
            lineto(i + 1, j)
            stroke(*lc)
            newpath()
            circle(i + 1, j, r)
            fill(1)
            stroke()
            t = texinsert("$1$")
            t.scale(fs)
            t.translate(-t.width / 2, -t.height / 2)
            place(t, i + 0.75, j + 0.25)

    newpath()
    circle(i + 0.5, j + 0.5, r)
    if (i + j + n) % 2 == 1:
        fill(1)
    else:
        fill(0)
    stroke()


for i, j in cells:
    if (i + j + n) % 2 == 1 and (i + 1, j + 1) in cells:
        newpath()
        t = texinsert("$w$")
        t.scale(fs)
        place(t, i + 0.9, j + 1.3)

        newpath()
        t = texinsert("$z$")
        t.scale(fs)
        place(t, i + 0.6, j + 0.95)

        newpath()
        t = texinsert("$x$")
        t.scale(fs)
        place(t, i + 1.25, j + 0.95)

        newpath()
        t = texinsert("$y$")
        t.scale(fs)
        place(t, i + 0.95, j + 0.6)


finish()
