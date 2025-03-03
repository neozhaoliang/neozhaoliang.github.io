from piscript.PiModule import *
from math import *
import numpy as np


def e2h(r):
    return 2 * np.arctanh(r)


def h2e(r):
    return np.tanh(r / 2)


def get_hyperbolic_circle_center_rad(cen, rad):
    n = Vector(cen).normalize()
    p1 = cen - rad * n
    p2 = cen + rad * n
    r1 = p1.length()
    r2 = p2.length()
    d1 = e2h(r1)
    d2 = e2h(r2)
    rad = (r2 - r1) / 2
    pos = (r2 + r1) / 2
    pos = h2e(pos)
    return pos * n, rad


fc = (1, 1, 0.3)


def circ(x, y, rad, fc=None, ec=None):
    newpath()
    circle(x, y, rad)
    if fc is not None:
        fill(fc)
    if ec is None:
        ec = (0, 0, 0)
    stroke(*ec)


def dir(a):
    a = a * pi / 180.0
    ca = cos(a)
    sa = sin(a)
    return Vector(ca, sa)

def inversion(p, cen, rad):
    p = p - cen
    r2 = p * p
    p *= rad * rad / r2
    return p + cen


def make_tangent(p):
    gsave()
    scalelinewidth(0.5)
    v1 = Vector(-p[1], p[0])
    v2 = p
    l = 0.4
    setdash([4, 2])
    for v in [v1, v2]:
        newpath()
        start = p + v * l
        end = p - v * l
        moveto(start)
        lineto(end)
        stroke()

    grestore()
    l = 0.075
    w1 = p - v1 * l
    w2 = w1 - v2 * l
    w3 = w2 + v1 * l
    newpath()
    moveto(w1)
    lineto(w2)
    lineto(w3)
    stroke()


def get_center_rad(z1, z2):
    z0 = (z1 + z2) / 2
    w = z0 - z1
    iw = Vector(-w[1], w[0])
    t = (w*w + 1 - z0*z0) / (2 * z0 * iw)
    cen = z0 + iw * t
    rad = (cen - z1).length()
    return cen, rad


def main():
    init("poincare_disk.eps", 200, 200)
    center()
    scale(90)

    circ(0, 0, 1, fc=(0.8, 0.8, 0.8))

    P = Vector(0.4, 0.5)
    Q = Vector(0.2, -0.2)

    cen, rad = get_center_rad(P, Q)

    cc = cen / (cen * cen)
    ic = Vector(-cc[1], cc[0])
    A = cc + rad * ic
    B = cc - rad * ic
    angA = (A - cen).arg()
    angB = (B - cen).arg()
    newpath()
    if angA < angB:
        arc(cen, rad, angA, angB)
    else:
        arcn(cen, rad, angB, angA)
    stroke()

    angP = (P - cen).arg()
    angQ = (Q - cen).arg()
    newpath()
    if angP < angQ:
        arc(cen, rad, angP, angQ)
    else:
        arcn(cen, rad, angQ, angP)
    scalelinewidth(2)
    stroke()
    scalelinewidth(0.5)

    make_tangent(A)
    make_tangent(B)

    rad = 0.03
    circ(A[0], A[1], rad, fc=(1, .5, 0))
    circ(B[0], B[1], rad, fc=(1, .5, 0))
    circ(P[0], P[1], rad, fc=(0, 1, 0.5))
    circ(Q[0], Q[1], rad, fc=(0, 1, 0.5))
    circ(0, 0, 0.01, fc=(0, 0, 0))


    sc = 1
    t = texinsert(r"$P$")
    t.scale(sc)
    t.translate(-t.width/2, t.height/2)
    place(t, P[0] + 0.1, P[1] - 0.15)


    t = texinsert(r"$Q$")
    t.scale(sc)
    t.translate(-t.width/2, t.height/2)
    place(t, Q[0] + 0.1, Q[1] - 0.15)

    t = texinsert(r"$A$")
    t.scale(sc)
    t.translate(-t.width/2, t.height/2)
    place(t, A[0] + 0.1, A[1])

    t = texinsert(r"$B$")
    t.scale(sc)
    t.translate(-t.width/2, t.height/2)
    place(t, B[0] + 0.1, B[1] - 0.15)

    t = texinsert(r"$O$")
    t.scale(sc)
    t.translate(-t.width/2, t.height/2)
    place(t, -0.1, - 0.15)

    R = Vector(-0.2, 0.6)

    gsave()
    scalelinewidth(0.5)
    setdash([2, 1])
    newpath()
    moveto(0, 0)
    lineto(R)
    stroke()
    grestore()

    newpath()
    setarrowdims(0.015, 0.04)
    arrow(R*0.25, R*0.75)
    fill(0)
    stroke()

    circ(R[0], R[1], rad, fc=(0, 1, 0.5))
    t = texinsert(r"$R$")
    t.scale(sc)
    t.translate(-t.width/2, t.height/2)
    place(t, R[0]-0.1,  R[1])

    finish()

#main()

def parallel_lines():
    init("parallel_lines.eps", 200, 200)
    center()
    scale(90)

    #circ(0, 0, 1, fc=(0.8, 0.8, 0.8))

    newpath()
    circle(0, 0, 1)
    fill(0.8)


    P = Vector(0.4, 0.5)
    Q = Vector(0.2, -0.2)

    cen, rad = get_center_rad(P, Q)

    cc = cen / (cen * cen)
    ic = Vector(-cc[1], cc[0])
    A = cc + rad * ic
    B = cc - rad * ic
    angA = (A - cen).arg()
    angB = (B - cen).arg()
    newpath()
    if angA < angB:
        arc(cen, rad, angA, angB)
    else:
        arcn(cen, rad, angB, angA)
    stroke(0, 0.5, 1)

    rad = 0.03
    P = Vector(-0.3, 0.4)
    l = 0.1
    N = 30
    for k in range(10, N-10):
        Q = P + l * Vector(cos(k*pi/N), sin(k*pi/N))
        cen, rad = get_center_rad(P, Q)
        cc = cen / (cen * cen)
        ic = Vector(-cc[1], cc[0])
        A = cc + rad * ic
        B = cc - rad * ic
        angA = (A - cen).arg()
        angB = (B - cen).arg()
        newpath()
        if angA < angB:
            arc(cen, rad, angA, angB)
        else:
            arcn(cen, rad, angB, angA)
        a = float(k) / float(N)
        stroke(1, 1-a, a)

    rad = 0.03
    circ(P[0], P[1], rad, fc=(0, 1, 0.5))


    newpath()
    circle(0, 0, 1)
    stroke()

    finish()


#parallel_lines()


def geodesic_triangle():
    init("geodesic_triangle.eps", 200, 200)
    center()
    scale(90)

    newpath()
    circle(0, 0, 1)
    fill(0.8)

    for k in [1, 0.6, 0.4, 0.2, 0.1]:
        A, B, C = dir(90)*k, dir(210)*k, dir(-30)*k
        c1, r1 = get_center_rad(A, B)
        c2, r2 = get_center_rad(B, C)
        c3, r3 = get_center_rad(C, A)
        a1, b1 = (A - c1).arg(), (B - c1).arg()
        a2, b2 = (B - c2).arg(), (C - c2).arg()
        a3, b3 = (C - c3).arg(), (A - c3).arg()
        newpath()
        arcn(c1, r1, a1, b1)
        arcn(c2, r2, a2, b2)
        arcn(c3, r3, a3, b3)
        fill(1, k, 0)
        stroke()

    """
    A, B, C = Vector(0.45, 0.7), Vector(0.4, 0.2), Vector(0.8, 0.45)
    c1, r1 = get_center_rad(A, B)
    c2, r2 = get_center_rad(B, C)
    c3, r3 = get_center_rad(C, A)
    a1, b1 = (A - c1).arg(), (B - c1).arg()
    a2, b2 = (B - c2).arg(), (C - c2).arg()
    a3, b3 = (C - c3).arg(), (A - c3).arg()
    newpath()
    arc(c1, r1, a1, b1)
    arcn(c2, r2, a2, b2)
    arcn(c3, r3, a3, b3)
    fill(0, 1, 1)
    stroke()
    """

    newpath()
    circle(0, 0, 1)
    stroke()
    finish()


#geodesic_triangle()




def hyperbolic_reflection():
    init("hyperbolic-reflection.eps", 200, 200)
    center()
    scale(90)
    fc = (1, 1, 0.2)

    P = Vector(0.4, 0.5)
    Q = Vector(0.1, -0.2)

    cen, rad = get_center_rad(P, Q)

    cc = cen / (cen * cen)
    ic = Vector(-cc[1], cc[0])
    A = cc + rad * ic
    B = cc - rad * ic
    angA = (A - cen).arg()
    angB = (B - cen).arg()
    newpath()
    if angA < angB:
        arc(cen, rad, angA, angB)
    else:
        arcn(cen, rad, angB, angA)
    stroke()

    newpath()
    arc(cen, rad, angA, angB)
    arcn(0, 0, 1, B.arg(), A.arg())
    closepath()
    fill(1, 0.2, 0.2)
    stroke()

    newpath()
    arc(cen, rad, angA, angB)
    arc(0, 0, 1, B.arg(), A.arg())
    closepath()
    fill(0.2, 0.4, 1)
    stroke()

    scalelinewidth(0.5)
    A = Vector(0.1, 0.5)
    B = Vector(-0.7, 0.)
    C = Vector(-0.1, -0.3)
    c1, r1 = get_center_rad(A, B)
    c2, r2 = get_center_rad(B, C)
    c3, r3 = get_center_rad(C, A)
    a1, b1 = (A - c1).arg(), (B - c1).arg()
    a2, b2 = (B - c2).arg(), (C - c2).arg()
    a3, b3 = (C - c3).arg(), (A - c3).arg()
    newpath()
    arcn(c1, r1, a1, b1)
    arcn(c2, r2, a2, b2)
    arc(c3, r3, a3, b3)
    #fill(*fc)
    stroke()

    A = inversion(A, cen, rad)
    B = inversion(B, cen, rad)
    C = inversion(C, cen, rad)
    c1, r1 = get_center_rad(A, B)
    c2, r2 = get_center_rad(B, C)
    c3, r3 = get_center_rad(C, A)
    a1, b1 = (A - c1).arg(), (B - c1).arg()
    a2, b2 = (B - c2).arg(), (C - c2).arg()
    a3, b3 = (C - c3).arg(), (A - c3).arg()
    newpath()
    arc(c1, r1, a1, b1)
    arc(c2, r2, a2, b2)
    arcn(c3, r3, a3, b3)
    #fill(*fc)
    setdash([4, 2])
    stroke()

    finish()

hyperbolic_reflection()
