from piscript.PiModule import *
from math import *


fc = (1, 1, 0)


def circ(x, y, rad, fc=None, ec=None):
    newpath()
    circle(x, y, rad)
    if fc is not None:
        fill(fc)
    if ec is None:
        ec = (0, 0, 0)
    stroke(*ec)


def inversion():
    init("circle_inversion.eps", 250, 150)
    center()
    scale(20)
    translate(-2.5, 0)

    rad = 3
    mark = 0.14
    sc = 1
    circ(0, 0, rad)

    P = Vector(8, 0)
    Q = Vector(rad * rad / P[0], 0)

    newpath()
    moveto(*P)
    lineto(0, 0)
    stroke()

    a = Q[0]
    b = sqrt(rad * rad - a * a)
    A = Vector(a, b)

    newpath()
    moveto(*P)
    lineto(*A)
    lineto(0, 0)
    stroke()

    v = Vector(-A[1], A[0]).normalize()
    P = Vector(P)
    n = Vector(A)
    n = n.normalize()
    l = 0.3
    p1 = A - l * n
    p2 = p1 + l * (P - A).normalize()
    p3 = p2 + l * n
    newpath()
    moveto(p1)
    lineto(p2)
    lineto(p3)
    stroke()

    newpath()
    moveto(A)
    lineto(Q)
    stroke()

    p1 = Q + l * (A - Q).normalize()
    p2 = p1 + l * Vector(1, 0)
    p3 = p2 - l * (A - Q).normalize()
    newpath()
    moveto(p1)
    lineto(p2)
    lineto(p3)
    stroke()

    t = texinsert(r"$O$")
    t.scale(sc)
    t.translate(-t.width/2, -t.height/2)
    place(t, -0.4, -0.4)

    t = texinsert(r"$P$")
    t.scale(sc)
    t.translate(-t.width/2, -t.height/2)
    place(t, P[0], P[1]-0.5)


    t = texinsert(r"$P'$")
    t.scale(sc)
    t.translate(-t.width/2, -t.height/2)
    place(t, Q[0] + 0.2, Q[1]-0.4)

    t = texinsert(r"$Q$")
    t.scale(sc)
    t.translate(0, t.height/2)
    place(t, A[0], A[1])

    circ(0, 0, mark, fc=(0, 1, .5))
    circ(P[0], P[1], mark, fc=(1, 0, .5))
    circ(A[0], A[1], mark, fc=(1, 0.5, 0))
    circ(Q[0], Q[1], mark, fc=(0, 0.5, 1))
    finish()


inversion()
