from piscript.PiModule import *
import numpy as np


init("wd.eps", 400, 200, "noclip")
center()
scale(150)


def draw_triangle(a, b, c, fc=None):
    newpath()
    moveto(a[0], a[1])
    lineto(b[0], b[1])
    lineto(c[0], c[1])
    lineto(a[0], a[1])
    if fc:
        fill(*fc)
    stroke()


A = np.array([0, 0])
B = np.array([1, 0])
C = np.array([0.75, np.sqrt(3)/4])
D = np.array([0.75, -np.sqrt(3)/4])

gsave()
translate(-1.2, 0)
draw_triangle(A, B, C, fc=(0.8, 0.8, 0.8))
draw_triangle(A, B, D, fc=(1, 1, 1))

sc = 1.5
t = texinsert(r"$\mathcal{D}$")
t.translate(-t.width * 2, -t.height/2)
t.scale(sc)
place(t, 0.8, 0.2)

sc = 1.5
t = texinsert(r"$s\mathcal{D}$")
t.translate(-t.width * 1.5, 0)
t.scale(sc)
place(t, 0.8, -0.2)
grestore()


gsave()
translate(0.2, 0)
draw_triangle(A, B, C, fc=(0.8, 0.8, 0.8))
draw_triangle(A, B, D, fc=(1, 1, 1))

sc = 1.5
t = texinsert(r"$w\mathcal{D}$")
t.translate(-t.width * 1.2, -t.height/2)
t.scale(sc)
place(t, 0.8, 0.2)

sc = 1.5
t = texinsert(r"$ws\mathcal{D}$")
t.translate(-t.width * 1, 0)
t.scale(sc)
place(t, 0.8, -0.2)
grestore()

flush()


