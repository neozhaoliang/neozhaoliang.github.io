from piscript.PiModule import *
from math import *

n = 4
r = 0.08
init(400, 400)
center()
scale(50)
fs = 1.5

def rectangle(x1, y1, x2, y2, gray):
    newpath()
    moveto(x1, y2)
    lineto(x1, y1)
    lineto(x2, y1)
    stroke()

cells = []
for j in range(-n, n):
    k = min(n+1+j, n-j)
    for i in range(-k, k):
        cells.append((i, j))

rotate(pi/4)
for i, j in cells:
    if (i + j + n) % 2 == 1 and (i+1, j+1) in cells:
        newpath()
        moveto(i+0.5, j+0.5)
        lineto(i+0.5, j+1.5)
        lineto(i+1.5, j+1.5)
        lineto(i+1.5, j+0.5)
        lineto(i+0.5, j+0.5)
        closepath()
        fill(1, 0.75, 0.75)

    if (i, j+1) in cells:
        newpath()
        moveto(i+0.5, j+0.5)
        lineto(i+0.5, j+1.5)
        stroke()

    if (i+1, j) in cells:
        newpath()
        moveto(i+0.5, j+0.5)
        lineto(i+1.5, j+0.5)
        stroke()

    if (i + j + n) % 2 == 1:
        if (i, j+1) not in cells:
            newpath()
            moveto(i+0.5, j+0.5)
            lineto(i+1, j+1)
            stroke()
            newpath()
            circle(i+1, j+1, r)
            fill(1,0, 0)
            stroke()
        if (i, j-1) not in cells:
            newpath()
            moveto(i+0.5, j+0.5)
            lineto(i, j)
            stroke()
            newpath()
            circle(i, j, r)
            fill(1, 0, 0)
            stroke()
    else:
        if (i-1, j) not in cells:
            newpath()
            moveto(i+0.5, j+0.5)
            lineto(i, j+1)
            stroke()
            newpath()
            circle(i, j+1, r)
            fill(1, 0, 0)
            stroke()

        if (i, j-1) not in cells:
            newpath()
            moveto(i+0.5, j+0.5)
            lineto(i+1, j)
            stroke()
            newpath()
            circle(i+1, j, r)
            fill(1, 0, 0)
            stroke()
    
    newpath()
    circle(i+0.5, j+0.5, r)
    fill(1, 0, 0)
    stroke()


finish()
