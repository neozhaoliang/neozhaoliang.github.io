from piscript.PiModule import *
import numpy as np


init("lws.eps", 400, 400, "noclip")
center()
scale(80)
translate(0, -0.4)

def draw_triangle(a, b, c, fc=None):
    newpath()
    moveto(a[0], a[1])
    lineto(b[0], b[1])
    lineto(c[0], c[1])
    lineto(a[0], a[1])
    if fc:
        fill(*fc)
    stroke()


def draw_line():
    newpath()
    moveto(0, 2.5)
    lineto(0, 0.8)
    stroke()

    newpath()
    moveto(0, 0.2)
    lineto(0, -1.5)
    stroke()


    gsave()
    setdash([4, 4])
    newpath()
    moveto(0, 0.8)
    lineto(0, 0.2)
    stroke()
    grestore()

draw_line()

A = np.array([0, 1])
B = np.array([0, 2])
C = np.array([-np.sqrt(3)/2, 1.5])
D = np.array([np.sqrt(3)/2, 1.5])

draw_triangle(A, B, C, fc=(0.8, 0.8, 0.8))
draw_triangle(A, B, D, fc=None)

newpath()
moveto(*A)
lineto(*B)
stroke(0, 0, 1)

P = np.array([0, 0])
Q = np.array([0, -1])
R = np.array([np.sqrt(3) / 2, -0.5])

draw_triangle(P, Q, R, fc=None)

sc = 1.5
t = texinsert(r"$\mathcal{D}$")
t.translate(-t.width * 1.5, -t.height/2)
t.scale(sc)
place(t, 0.5, -0.5)

t = texinsert(r"$w\mathcal{D}$")
t.translate(-t.width, -t.height/2)
t.scale(sc)
place(t, np.sqrt(3)/4, 1.5)

t = texinsert(r"$w\color{0 0 1}s\uncolor\mathcal{D}$")
t.translate(-t.width/3, -t.height/2)
t.scale(sc)
place(t, -np.sqrt(3)/4, 1.5)


t = texinsert(r"$w\alpha_s=0$")
t.translate(-t.width/2, t.height/2)
t.scale(sc)
place(t, 0, 2.5)


t = texinsert(r"$w\alpha_s>0$")
t.translate(-t.width/2, t.height/2)
t.scale(sc)
place(t, 1, 0.5)


t = texinsert(r"$w\alpha_s<0$")
t.translate(-t.width/2, t.height/2)
t.scale(sc)
place(t, -1, 0.5)

t = texinsert(r"$l(ws) > l(w)$")
t.translate(-t.width/2, t.height/2)
t.scale(sc)
place(t, -1.2, 2)

setarrowdims(0.03, 0.1)
arrow([0.15, 1.75], [-0.15, 1.75])
stroke()

flush()


