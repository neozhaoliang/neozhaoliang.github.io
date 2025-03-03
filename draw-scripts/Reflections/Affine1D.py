from piscript.PiModule import *
import numpy as np


def main():
    def ref(v):
        return -v

    def ref2(v):
        return np.array([2 - v[0], v[1]])

    init("affine1d.eps", 500, 150)
    center()
    scale(70)
    translate(-0.5, 0)

    newpath()
    moveto(-6, 0)
    lineto(6, 0)
    stroke()

    sc = 1.6
    TEX = r"\mathcal{{D}}"
    t = texinsert(r"${}$".format(TEX))
    t.scale(sc)
    t.translate(-t.width/2, t.height)
    setcolor(1, 0, 0)
    place(t, .5, 0)

    setcolor(0)
    t = texinsert(r"$t{}$".format(TEX))
    t.scale(sc)
    t.translate(-t.width/2, t.height)
    place(t, 1.5, 0)

    t = texinsert(r"$ts{}$".format(TEX))
    t.scale(sc)
    t.translate(-t.width/2, t.height)
    place(t, 2.5, 0)

    t = texinsert(r"$tst{}$".format(TEX))
    t.scale(sc)
    t.translate(-t.width/2, t.height)
    place(t, 3.5, 0)

    t = texinsert(r"$s{}$".format(TEX))
    t.scale(sc)
    t.translate(-t.width/2, t.height)
    place(t, -0.5, 0)

    t = texinsert(r"$st{}$".format(TEX))
    t.scale(sc)
    t.translate(-t.width/2, t.height)
    place(t, -1.5, 0)

    t = texinsert(r"$sts{}$".format(TEX))
    t.scale(sc)
    t.translate(-t.width/2, t.height)
    place(t, -2.6, 0)

    col = (0, 0, 0)

    dx = 2
    for k in [0, 1]:
        newpath()
        moveto(k, -dx)
        lineto(k, dx)
        stroke(*col)

    dx = 0.1
    scalelinewidth(2)
    for k in range(-8, 8):
        newpath()
        moveto(k, -dx)
        lineto(k, dx)
        stroke(*col)

    flush()

main()
