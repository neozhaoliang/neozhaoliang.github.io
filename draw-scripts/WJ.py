from piscript.PiModule import *
from math import *


def circ(x, y, rad, fc=(0, 0, 0), ec=None):
    newpath()
    circle(x, y, rad)
    if fc is not None:
        fill(fc)
    if ec is None:
        ec = (0, 0, 0)
    stroke(*ec)


def WJ2():
    init("WJ2.eps", 200, 200)
    center()
    scale(120)
    translate(0, -0.6)

    a = 0.5
    b = a * 3**0.5
    c = b + 0.15
    A = Vector(-a, 0)
    C = Vector(0, b)
    B = Vector(a, 0)

    newpath()
    moveto(A)
    lineto(B)
    lineto(C)
    lineto(A)
    fill(0.9)

    newpath()
    moveto(-2 * a, 0)
    lineto(2 * a, 0)
    stroke()

    l = 0.8
    dir = Vector(cos(pi / 3), sin(pi / 3)) * l

    newpath()
    moveto(A - dir)
    lineto(C + dir)
    stroke()

    newpath()
    dir = Vector(cos(-pi / 3), sin(-pi / 3)) * l
    moveto(B + dir)
    lineto(C - dir)
    stroke()

    rad = 0.02
    k = 0.4
    circ(0, k, rad, fc=(0.5, 0.75, 0))
    circ(0, b, rad, fc=(1, 0, 0))

    dir = Vector(0, k) - Vector(0, b)
    for i in range(6):
        dir.rotate(pi / 3)
        x, y = C + dir
        circ(x, y, rad, fc=(0.5, 0.75, 0))

    fc = 1.0
    t = texinsert(r"""$\alpha_s=0$""")
    t.scale(fc)
    t.translate(-t.width / 2, t.height / 2)
    place(t, 0.0, -0.15)

    t = texinsert(r"""$\mathcal{D}$""")
    t.scale(fc * 1.25)
    t.translate(-t.width / 2, t.height)
    place(t, -0.2, 0.2)

    setcolor(1, 0, 0)
    t = texinsert(r"$x$")
    t.scale(fc)
    t.translate(-t.width / 2, -t.height / 2)
    place(t, 0.1, b)

    setcolor(0.5, 0.75, 0)
    t = texinsert(r"$y$")
    t.scale(fc)
    t.translate(-t.width / 2, -t.height / 2)
    place(t, 0.0, k - 0.1)

    finish()


WJ2()


def WJ1():
    init("WJ.eps", 200, 200)
    center()
    scale(120)
    translate(0, -0.7)

    a = 0.5
    b = a * 3**0.5
    c = b + 0.15
    A = Vector(-a, 0)
    C = Vector(0, b)
    B = Vector(a, 0)

    newpath()
    moveto(A)
    lineto(B)
    lineto(C)
    lineto(A)
    fill(0.9)

    newpath()
    moveto(-2 * a, 0)
    lineto(2 * a, 0)
    stroke()

    l = 0.8
    dir = Vector(cos(pi / 3), sin(pi / 3)) * l

    newpath()
    moveto(A - dir)
    lineto(C + dir)
    stroke()

    newpath()
    dir = Vector(cos(-pi / 3), sin(-pi / 3)) * l
    moveto(B + dir)
    lineto(C - dir)
    stroke()

    rad = 0.02
    setdash([4, 4])
    newpath()
    moveto(0, 0.2)
    lineto(0, c)
    stroke()

    circ(0, b, 0.2, fc=None, ec=(0, 0, 0))
    setdash([])

    circ(0, 0.2, rad, fc=(0.5, 0.75, 0))
    circ(0, b, rad, fc=(1, 0, 0))
    circ(0, c, rad, fc=(0, 0, 1))

    fc = 1.0
    t = texinsert("""$J=\{s,t\}$""")
    t.scale(fc)
    t.translate(-t.width / 2, t.height)
    place(t, 0.0, 1.3)

    t = texinsert(r"""$\alpha_s=0$""")
    t.scale(fc)
    t.translate(-t.width / 2, t.height / 2)
    place(t, 0.4, 0.4)

    t = texinsert(r"""$\alpha_t=0$""")
    t.scale(fc)
    t.translate(-t.width / 2, t.height / 2)
    place(t, -0.4, 0.4)

    t = texinsert(r"""$\mathcal{D}$""")
    t.scale(fc * 1.25)
    t.translate(-t.width / 2, t.height)
    place(t, -0.2, 0.2)

    setcolor(1, 0, 0)
    t = texinsert(r"$x$")
    t.scale(fc)
    t.translate(-t.width / 2, -t.height / 2)
    place(t, 0.1, b)

    setcolor(0.5, 0.75, 0)
    t = texinsert(r"$y$")
    t.scale(fc)
    t.translate(-t.width / 2, -t.height / 2)
    place(t, 0.0, 0.1)

    setcolor(0, 0, 1)
    t = texinsert(r"$z$")
    t.scale(fc)
    t.translate(-t.width / 2, -t.height / 2)
    place(t, 0.0, c + 0.1)
    finish()


def WJ3():
    init("WJ3.eps", 200, 200)
    center()
    scale(120)
    translate(0, -0.6)

    a = 0.5
    b = a * 3**0.5
    c = b + 0.15
    A = Vector(-a, 0)
    C = Vector(0, b)
    B = Vector(a, 0)

    newpath()
    moveto(A)
    lineto(B)
    lineto(C)
    lineto(A)
    fill(0.9)

    newpath()
    moveto(-2 * a, 0)
    lineto(2 * a, 0)
    stroke()

    l = 0.8
    dir = Vector(cos(pi / 3), sin(pi / 3)) * l

    newpath()
    moveto(A - dir)
    lineto(C + dir)
    stroke()

    newpath()
    dir = Vector(cos(-pi / 3), sin(-pi / 3)) * l
    moveto(B + dir)
    lineto(C - dir)
    stroke()

    rad = 0.02
    k = 0.4

    setdash([4, 4])
    moveto(0, k)
    lineto(0, c)
    stroke()
    setdash([])

    circ(0, k, rad, fc=(0.5, 0.75, 0))
    circ(0, b, rad, fc=(1, 0, 0))
    circ(0, c, rad, fc=(0, 0, 1))

    fc = 1.0
    t = texinsert(r"""$\alpha_s=0$""")
    t.scale(fc)
    t.translate(-t.width / 2, t.height / 2)
    place(t, 0.0, -0.15)

    t = texinsert(r"""$\mathcal{D}$""")
    t.scale(fc * 1.25)
    t.translate(-t.width / 2, t.height)
    place(t, -0.2, 0.2)

    setcolor(1, 0, 0)
    t = texinsert(r"$x$")
    t.scale(fc)
    t.translate(-t.width / 2, -t.height / 2)
    place(t, 0.1, b)

    setcolor(0.5, 0.75, 0)
    t = texinsert(r"$y$")
    t.scale(fc)
    t.translate(-t.width / 2, -t.height / 2)
    place(t, 0.0, k - 0.1)

    setcolor(0, 0, 1)
    t = texinsert(r"$z$")
    t.scale(fc)
    t.translate(-t.width / 2, -t.height / 2)
    place(t, 0.0, c + 0.1)

    finish()


WJ3()
