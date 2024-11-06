from piscript.PiModule import *

n = 10
init(300, 300)
center()
scale(14)


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

for i, j in cells:
    rectangle(i, j, i+1, j+1, 0)
    if (i, j+1) not in cells:
        newpath()
        moveto(i, j+1)
        lineto(i+1, j+1)
        stroke()

    if (i+1, j) not in cells:
        newpath()
        moveto(i+1, j)
        lineto(i+1, j+1)
        stroke()

finish()
