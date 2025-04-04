from piscript.PiModule import *
from math import *
import numpy as np


init("finite2d.eps", 400, 400)
center()
scale(180)
setfont("CMR10", 12)

N = 5
a = pi / N

nA = np.array((1, 0))
nB = np.array((-cos(a), sin(a)))

pA = (0, 1)
pB = (cos(pi/2 - a), sin(pi/2-a))


def ref(v, n):
    return v - 2 * np.dot(v, n) * n


G = []
for k in range(N // 2 + 1):
    G.append("st"*k)
    G.append("t" + "st"*k)

for k in range(1, N // 2 + 1):
    G.append("ts"*k)

for k in range(N // 2):
    G.append("s" + "ts"*k)

sc = 1.5
newpath()
moveto(0, 0)
lineto(*pA)
lineto(*pB)
closepath()
fill(1, 1, 0)

v0 = np.array((0.2, 0.6))
for g in G:
    v = v0
    if len(g) > 0:
        for s in g[::-1]:
            if s == "s":
                v = ref(v, nA)
            else:
                v = ref(v, nB)

        t = texinsert(r"${}K$".format(g))
        t.scale(sc)
        t.translate(-t.width/2, -t.height/2)
        if len(g) == 5:
            place(t, v[0] - 0.05, v[1])
        else:
            place(t, v[0], v[1])
    else:
        t = texinsert(r"$K$")
        t.scale(sc)
        t.translate(-t.width/2, -t.height/2)
        place(t, v0[0], v0[1])

scalelinewidth(2)
for k in range(0, 10, 2):
    newpath()
    moveto(0, 0)
    lineto(cos(a*k+pi/2-a), sin(a*k+pi/2-a))
    stroke(0)

for k in range(1, 11, 2):
    newpath()
    moveto(0, 0)
    lineto(cos(a*k+pi/2-a), sin(a*k+pi/2-a))
    stroke(1, 0.5, 0)

"""
pts = [[cos(k*pi/N), sin(k*pi/N)]for k in range(2*N)]
pts = np.array(pts) * 0.9
newpath()
moveto(*pts[0])
for k in range(1, 2*N):
    lineto(*pts[k])
closepath()
stroke()

rad = 0.03
for k in range(0, 2*N):
    newpath()
    circle(pts[k][0], pts[k][1], rad)
    fill(0, 1, 0.5)
    stroke()
"""

t = texinsert(r"$\alpha=0$")
t.scale(sc)
t.translate(-t.width/2, 0)
place(t, 0, 1)

t = texinsert(r"$\beta=0$")
t.scale(sc)
t.translate(-t.width/2, 0)
place(t, 0.55, .85)


setarrowdims(0.015, 0.04)
newpath()
arrow((0, 0), nA*0.4)
fill(1, 0.5, 0)
stroke()

newpath()
arrow((0, 0), nB*0.4)
fill(1, 0.5, 0)
stroke()

t = texinsert(r"$\alpha^\vee$")
t.scale(sc)
t.translate(-t.width/2, -t.height/2)
place(t, 0.4, -0.05)

t = texinsert(r"$\beta^\vee$")
t.scale(sc)
t.translate(-t.width/2, -t.height/2)
pos = nB*0.4 + np.array([-0.1, 0])
place(t, *pos)


flush()
