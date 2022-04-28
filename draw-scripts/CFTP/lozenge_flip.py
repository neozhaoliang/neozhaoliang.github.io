from piscript.PiModule import *
from math import *


Tcolor = (0.678, 0.847, 1)
Lcolor = (0.314, 0.188, 0.475)
Rcolor = (1, 0.569, 0.459)


def dir(ang):
    a = ang * pi / 180
    return complex(cos(a), sin(a))


def lozenge(verts, col):
    newpath()
    v = verts[0]
    moveto(v.real, v.imag)
    for i in range(1, 4):
        lineto(verts[i].real, verts[i].imag)
    closepath()
    fill(*col)
    stroke()


def main():
    init(400, 150)
    center()
    scale(60)
    setlinejoin(2)
    setlinewidth(2)

    X = dir(30)
    Y = dir(150)
    Z = dir(-90)
    t = [0, X, X + Y, Y]
    l = [0, Y, Y + Z, Z]
    r = [0, X, X + Z, Z]

    gsave()
    translate(-2, 0)
    lozenge(t, Tcolor)
    lozenge(l, Lcolor)
    lozenge(r, Rcolor)
    grestore()

    X = dir(210)
    Y = dir(-30)
    Z = dir(90)
    t = [0, X, X + Y, Y]
    l = [0, Y, Y + Z, Z]
    r = [0, X, X + Z, Z]

    gsave()
    translate(2, 0)
    lozenge(t, Tcolor)
    lozenge(l, Lcolor)
    lozenge(r, Rcolor)
    grestore()

    setlinewidth(1)
    sw = 0.04
    hw = 4 * sw
    s = 0.6
    setarrowdims(sw, hw)
    newpath()
    openarrow(s, 0)
    openarrow(-s, 0)
    fill(0, 1, 0.5)
    stroke()
    finish()


main()
