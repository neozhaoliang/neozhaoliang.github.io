# -*- coding: utf-8 -*-
from piscript.PiModule import *


N = Vector(0, 1)
S = Vector(0, -1)
W = Vector(-1, 0)
E = Vector(1, 0)
Dirs = [E, N, W, S]
blue = (0, 0, 1)


def line(p, q, color=None):
    newpath()
    moveto(p)
    lineto(q)
    if color:
        stroke(*color)
    else:
        stroke()

def dashline(p, q, color=None):
    gsave()
    setdash([3, 3], 0)
    newpath()
    moveto(p)
    lineto(q)
    if color:
        stroke(*color)
    else:
        stroke()
    grestore()


def dashsquare(pts, color=None):
    gsave()
    setdash([4, 4], 0)
    setlinewidth(0.5)
    newpath()
    p1, p2, p3, p4 = pts
    moveto(p1)
    lineto(p2)
    lineto(p3)
    lineto(p4)
    closepath()
    if color:
        stroke(*color)
    else:
        stroke()
    grestore()


def getsquare(x, y):
    x1 = x + 0.25
    x2 = x + 0.75
    y1 = y + 0.25
    y2 = y + 0.75
    return [(x1, y1), (x2, y1), (x2, y2), (x1, y2)]


def dots(pts, rad, color=(0, 0, 0)):
    for p in pts:
        newpath()
        circle(p, rad)
        fill(*color)
        stroke(*color)


def grid(xlist, ylist):
    for x in xlist[1:-1]:
        line((x, ylist[0]), (x, ylist[-1]))
    for y in ylist[1:-1]:
        line((xlist[0], y), (xlist[-1], y))

    for x in xlist[1:-1]:
        for y in ylist[1:-1]:
            dots([Vector(x,y)], 0.07)


init("grid.eps", 450, 200)
center()
scale(50)

xs = (0, 1, 2, 3, 4, 5)
ys = xs

gsave()
translate(-5, -2.5)

newpath()
moveto(0.5, 0.5)
lineto(0.5, 4.5)
lineto(4.5, 4.5)
lineto(4.5, 0.5)
closepath()
clip()

grid(xs, ys)

setlinewidth(0.5)
for x in xs[:-1]:
    for y in ys[:-1]:
        if (x + y) % 2 == 0:
            square = getsquare(x, y)
            dashsquare(square, color=(1, 0, 0))
            dots(square, 0.04, color=(1, 0, 0))
            a, b = square[2]
            c, d = a+0.5, b+0.5
            dashline((a, b), (c, d), (1, 0, 0))
            a, b = square[1]
            c, d = a+0.5, b-0.5
            dashline((a, b), (c, d), (1, 0, 0))
grestore()

gsave()
translate(0, -2.5)
setlinewidth(0.5)

newpath()
moveto(0.5, 0.5)
lineto(4.5, 0.5)
lineto(4.5, 4.5)
lineto(0.5, 4.5)
closepath()
clip()

for x in xs[:-1]:
    for y in ys[:-1]:
        dots([(x, y)], 0.04, color=(0,0,0))
        if (x + y) % 2 == 0:
            square = getsquare(x, y)
            dashsquare(square, color=(0, 0, 0))
            dots(square, 0.04, color=(0, 0, 0))
            a, b = square[2]
            c, d = a+0.5, b+0.5
            dashline((a, b), (c, d), (0, 0, 0))
            a, b = square[1]
            c, d = a+0.5, b-0.5
            dashline((a, b), (c, d), (0, 0, 0))

grestore()
finish()
