from piscript.PiModule import *
from math import *


fc = (1, 1, 0)


def circ(x, y, rad, fc=(1, 1, 0), ec=None):
    gsave()
    scalelinewidth(2)
    newpath()
    circle(x, y, rad)
    if fc is not None:
        fill(fc)
    if ec is None:
        ec = (0, 0, 0)
    stroke(*ec)
    grestore()


def rank2_inf():
    init("rank2_inf.eps", 160, 40)
    center()
    scale(70)

    a = 0.5
    newpath()
    moveto(-a, 0)
    lineto(a, 0)
    stroke()

    rad = 0.08

    circ(-a, 0, rad)
    circ(a, 0, rad)

    t = texinsert(r"${\bf \infty}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, -0.05, 0.05)

    finish()


def affine_A2():
    init("a2~.eps", 100, 100)
    center()
    scale(40)
    rad = 0.08
    a = 3**0.5 / 2
    A = Vector(0, 1)
    B = Vector(-a, -0.5)
    C = Vector(a, -0.5)

    newpath()
    moveto(A)
    lineto(B)
    lineto(C)
    closepath()
    stroke()

    circ(*A, rad=rad)
    circ(*B, rad=rad)
    circ(*C, rad=rad)

    finish()


def affine_B2():
    init("b2~.eps", 120, 60)
    center()
    scale(50)

    rad = 0.08
    a = 1

    newpath()
    moveto(-a, 0)
    lineto(a, 0)
    stroke()

    circ(-a, 0, rad)
    circ(0, 0, rad)
    circ(a, 0, rad)

    t = texinsert(r"${\bf 4}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, -0.5, 0)
    place(t, 0.5, 0)

    finish()


def affine_C2():
    init("c2~.eps", 120, 60)
    center()
    scale(50)

    rad = 0.08
    a = 1

    newpath()
    moveto(-a, 0)
    lineto(a, 0)
    stroke()

    circ(-a, 0, rad)
    circ(0, 0, rad)
    circ(a, 0, rad)

    t = texinsert(r"${\bf 6}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, -0.5, 0)

    finish()


def affine_A3():
    init("a3~.eps", 100, 100)
    center()
    scale(80)

    rad = 0.08
    a = 0.5

    newpath()
    moveto(a, a)
    lineto(a, -a)
    lineto(-a, -a)
    lineto(-a, a)
    closepath()
    stroke()

    circ(-a, a, rad)
    circ(a, a, rad)
    circ(a, -a, rad)
    circ(-a, -a, rad)
    finish()


def affine_B3():
    init("b3~.eps", 200, 100)
    center()
    scale(80)
    rad = 0.08
    a = 3**0.5 / 2

    newpath()
    moveto(-1, 0)
    lineto(0, 0)
    lineto(a, 0.5)
    stroke()

    newpath()
    moveto(0, 0)
    lineto(a, -0.5)
    stroke()

    circ(-1, 0, rad)
    circ(0, 0, rad)
    circ(a, 0.5, rad)
    circ(a, -0.5, rad)

    t = texinsert(r"${\bf 4}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, -0.5, 0)

    finish()


def affine_C3():
    init("c3~.eps", 180, 50)
    center()
    scale(50)
    rad = 0.08
    a = 1.0

    newpath()
    moveto(-1.5 * a, 0)
    lineto(1.5 * a, 0)
    stroke()

    circ(a / 2, 0, rad)
    circ(-a / 2, 0, rad)
    circ(a * 1.5, 0, rad)
    circ(-a * 1.5, 0, rad)

    t = texinsert(r"${\bf 4}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, -a, 0)
    place(t, a, 0)

    finish()


def rank2_finite():
    init("rank2_finite.eps", 100, 40)
    center()
    scale(70)

    a = 0.5
    newpath()
    moveto(-a, 0)
    lineto(a, 0)
    stroke()

    rad = 0.08

    circ(-a, 0, rad)
    circ(a, 0, rad)
    setfont("Helvetica-Bold", 8)
    t = texinsert(r"$m$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, -0.05, 0.05)

    finish()


def cube43():
    init("cube43.eps", 120, 60)
    center()
    scale(50)

    rad = 0.08
    a = 1

    newpath()
    moveto(-a, 0)
    lineto(a, 0)
    stroke()

    circ(-a, 0, rad)
    circ(0, 0, rad)
    circ(a, 0, rad)

    t = texinsert(r"${\bf 4}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, -0.5, 0)

    finish()


def tetra33():
    init("tetra33.eps", 120, 60)
    center()
    scale(50)

    rad = 0.08
    a = 1

    newpath()
    moveto(-a, 0)
    lineto(a, 0)
    stroke()

    circ(-a, 0, rad)
    circ(0, 0, rad)
    circ(a, 0, rad)
    finish()


def icosa53():
    init("icosa53.eps", 120, 60)
    center()
    scale(50)

    rad = 0.08
    a = 1

    newpath()
    moveto(-a, 0)
    lineto(a, 0)
    stroke()

    circ(-a, 0, rad)
    circ(0, 0, rad)
    circ(a, 0, rad)

    t = texinsert(r"${\bf 5}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, -0.5, 0)

    finish()


def prism():
    init("prism.eps", 120, 60)
    center()
    scale(50)

    rad = 0.08
    a = 1

    newpath()
    moveto(-a, 0)
    lineto(0, 0)
    stroke()

    circ(-a, 0, rad)
    circ(0, 0, rad)
    circ(a, 0, rad)

    t = texinsert(r"$ m$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, -0.5, 0)

    finish()


def paracompact():
    init("paracompact.eps", 120, 60)
    center()
    scale(50)

    rad = 0.08
    a = 1

    newpath()
    moveto(-a, 0)
    lineto(a, 0)
    stroke()

    circ(-a, 0, rad)
    circ(0, 0, rad)
    circ(a, 0, rad, fc=(1, 0.2, 0))

    t = texinsert(r"${\bf \infty}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, -0.55, 0.08)

    t = texinsert(r"${\bf 5}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, 0.5, 0)

    finish()


def noncompact():
    init("noncompact.eps", 120, 60)
    center()
    scale(50)

    rad = 0.08
    a = 1

    newpath()
    moveto(-a, 0)
    lineto(a, 0)
    stroke()

    circ(-a, 0, rad)
    circ(0, 0, rad)
    circ(a, 0, rad, fc=(1, 0.2, 0))

    t = texinsert(r"${\bf-1.1}$")
    t.scale(1.2)
    t.translate(-t.width / 2, t.height)
    place(t, -0.6, 0.08)

    finish()


def comb534():
    init("534.eps", 180, 50)
    center()
    scale(50)
    rad = 0.08
    a = 1.0

    newpath()
    moveto(-1.5 * a, 0)
    lineto(1.5 * a, 0)
    stroke()

    # circ(-a * 1.5, 0, rad * 2, fc=(1, 1, 1))

    circ(a / 2, 0, rad)
    circ(-a / 2, 0, rad)
    circ(a * 1.5, 0, rad)
    circ(-a * 1.5, 0, rad)

    t = texinsert(r"${\bf 5}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, -a, 0)

    t = texinsert(r"${\bf 4}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, a, 0)

    finish()


def comb363():
    init("363.eps", 180, 50)
    center()
    scale(50)
    rad = 0.08
    a = 1.0

    newpath()
    moveto(-1.5 * a, 0)
    lineto(1.5 * a, 0)
    stroke()

    circ(-a * 1.5, 0, rad * 2, fc=(1, 1, 1))

    circ(a / 2, 0, rad)
    circ(-a / 2, 0, rad)
    circ(a * 1.5, 0, rad)
    circ(-a * 1.5, 0, rad)

    t = texinsert(r"${\bf 6}$")
    t.scale(1.5)
    t.translate(-t.width / 2, t.height)
    place(t, 0, 0)

    finish()


def rank4_level3():
    init("rank4-level3.eps", 100, 100)
    center()
    scale(60)

    rad = 0.08
    a = 0.5

    newpath()
    moveto(a, a)
    lineto(a, -a)
    lineto(-a, -a)
    lineto(-a, a)
    closepath()
    stroke()

    circ(-a, a, rad)
    circ(a, a, rad)
    circ(a, -a, rad, fc=(1, 0, 0))
    circ(-a, -a, rad, fc=(1, 0, 0))

    t = texinsert(r"${\bf -1.1}$")
    t.scale(1.2)
    t.translate(-t.width / 2, t.height)
    place(t, -0.05, a)

    t = texinsert(r"${\bf 7}$")
    t.scale(1.2)
    t.translate(t.width / 2, -t.height / 2)
    place(t, a, 0)

    finish()


# rank2_inf()
# affine_A2()
# affine_B2()
# affine_C2()
# affine_A3()
# affine_B3()
# affine_C3()
# rank2_finite()
cube43()
# tetra33()
# icosa53()
# prism()
# paracompact()
# noncompact()
comb534()
# comb363()
rank4_level3()


def shadertoy():
    init("noncompact.eps", 100, 100)
    center()
    scale(40)
    rad = 0.08
    a = 3**0.5 / 2
    A = Vector(0, 1)
    B = Vector(-a, -0.5)
    C = Vector(a, -0.5)

    newpath()
    moveto(A)
    lineto(B)
    lineto(C)
    closepath()
    stroke()

    circ(*A, rad=rad, fc=(1, 0.2, 0))
    circ(*B, rad=rad)
    circ(*C, rad=rad)

    sc = 1
    t = texinsert(r"${\bf -1.1}$")
    t.scale(sc)
    t.translate(-t.width / 2, -t.height)
    place(t, -0.1, -0.6)

    t = texinsert(r"${\bf 4}$")
    t.scale(sc)
    t.translate(t.width / 2, -t.height)
    place(t, 0.4, 0.5)

    finish()


shadertoy()
