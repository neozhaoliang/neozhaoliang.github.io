from piscript.PiModule import *
from math import *

n = 3
r = 0.08
init(300, 100)
center()
scale(50)


def text(string, pos, sc):
    t = texinsert(string)
    t.scale(sc)
    t.translate(-t.width / 2, -t.height / 2)
    place(t, pos)


def dot(p, color=(1, 1, 1)):
    newpath()
    circle(p, r)
    fill(*color)
    stroke()


def line(p, q, color=None):
    newpath()
    moveto(p)
    lineto(q)
    if color:
        stroke(*color)
    else:
        stroke()


def fork(p, n, ll, color=(1, 0, 0)):
    gsave()
    setdash([4, 4])
    scalelinewidth(0.5)
    p = Vector(p)
    n = Vector(n)
    q1 = p + n * ll
    q2 = p + n.rotated(pi / 4) * ll
    q3 = p + n.rotated(-pi / 4) * ll
    for q in [q1, q2, q3]:
        newpath()
        moveto(p)
        lineto(q)
        stroke(*color)
    grestore()


A = Vector(-1, 0)
B = Vector(0, 0)
C = Vector(1, 0)
gsave()
translate(-1.2, 0)
line(A, C)
fork(A, A, 0.5)
fork(C, C, 0.5, color=(0, 0, 1))
for p in [A, C]:
    dot(p)
dot(B, color=(0, 0, 0))

text("$1$", A * 0.5, 1.25)
text("$1$", C * 0.5, 1.25)
grestore()


gsave()
translate(1, 0)
fork(C, A, 0.5)
fork(C, C, 0.5, color=(0, 0, 1))
dot(C, color=(1, 1, 1))
grestore()

setarrowdims(0.06, 0.15)
arrow((0.5, 0), (1.2, 0))
stroke()
finish()
