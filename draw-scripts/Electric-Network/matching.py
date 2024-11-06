from piscript.PiModule import *
import numpy as np


def dot(x, y):
    newpath()
    circle(x, y, 0.04)
    fill(0, 0, 0)


init("matching.eps", 500, 200)
center()
scale(80)
translate(-1.8, 0)
scalelinewidth(0.5)
setarrowdims(0.02, 0.08)

pts = [np.exp(1j * 2 * i * np.pi / 6) for i in range(6)]
pts = [(z.real, z.imag) for z in pts]
pts = [Vector(p) * 0.9 for p in pts]

c1 = [1, 3, 4, 5, 7, 10]
for i in range(6):
    label = str(c1[i])
    p = pts[i]
    t = texinsert(r"${}$".format(label))
    # t.scale(1.5)
    t.translate(-t.width / 2, -t.height / 2)
    t.scale(1.5)
    place(t, p)
    # dot(x, y)

for i in range(6):
    j = (i + 1) % 6
    A = pts[i]
    B = pts[j]
    start = A + 0.15 * (B - A)
    end = A + 0.85 * (B - A)
    newpath()
    arrow(start, end)
    if i % 2 == 0:
        fill(1, 0, 0)
        setcolor(1, 0, 0)
        t = texinsert(r"$\pi$")
        t.scale(1.5)
        t.translate(-t.width / 2, -t.height / 2)
        place(t, (A + B) / 2 * 1.2)
        setcolor(0, 0, 0)

    else:
        fill(0, 0, 1)
        setcolor(0, 0, 1)
        t = texinsert(r"$\pi'$")
        t.scale(1.5)
        t.translate(-t.width / 2, -t.height / 2)
        place(t, (A + B) / 2 * 1.2)
        setcolor(0, 0, 0)
    stroke()

s = Vector((2.4, 0))
k = 0.6
a = Vector(1, -1) * k + s
b = Vector(1, 1) * k + s
c = Vector(-1, 1) * k + s
d = Vector(-1, -1) * k + s
pts = [a, b, c, d]

c2 = [2, 6, 9, 8]


for i in range(4):
    label = str(c2[i])
    p = pts[i]
    t = texinsert(r"${}$".format(label))
    t.translate(-t.width / 2, -t.height / 2)
    t.scale(1.5)
    place(t, p)

for i in range(4):
    j = (i + 1) % 4
    A = pts[i]
    B = pts[j]
    start = A + 0.15 * (B - A)
    end = A + 0.85 * (B - A)
    newpath()
    arrow(start, end)
    if i % 2 == 0:
        fill(1, 0, 0)
        setcolor(1, 0, 0)
        t = texinsert(r"$\pi$")
        t.scale(1.5)
        t.translate(-t.width / 2, -t.height / 2)
        place(t, (A - s + B - s) / 2 * 1.3 + s)
        setcolor(0, 0, 0)

    else:
        fill(0, 0, 1)
        setcolor(0, 0, 1)
        t = texinsert(r"$\pi'$")
        t.scale(1.5)
        t.translate(-t.width / 2, -t.height / 2)
        place(t, (A - s + B - s) / 2 * 1.3 + s)
        setcolor(0, 0, 0)
    stroke()


pts = [Vector((4.2, 0.6)), Vector((4.2, -0.6))]
c3 = [11, 12]

for i in range(2):
    label = str(c3[i])
    p = pts[i]
    t = texinsert(r"${}$".format(label))
    t.translate(-t.width / 2, -t.height / 2)
    t.scale(1.5)
    place(t, p)


def putarc(P, Q, theta=30, delta=0.15):
    theta = np.deg2rad(theta)
    P1 = P - Vector(1, 1) * delta
    Q1 = Q - Vector(1, -1) * delta
    mid = (P1 + Q1) / 2
    r = (P1 - Q1).length() / 2 / np.sin(theta)
    cen = mid + Vector((r * np.cos(theta), 0))
    newpath()
    arcarrow(cen, r, np.pi - theta, np.pi + theta)
    fill(1, 0, 0)
    stroke()


def putarc2(P, Q, theta=30, delta=0.15):
    theta = np.deg2rad(theta)
    P1 = P + Vector(1, -1) * delta
    Q1 = Q + Vector(1, 1) * delta
    mid = (P1 + Q1) / 2
    r = (P1 - Q1).length() / 2 / np.sin(theta)
    cen = mid - Vector((r * np.cos(theta), 0))
    newpath()
    arcarrow(cen, r, -theta, theta)
    fill(0, 0, 1)
    stroke()


P, Q = pts
putarc(P, Q)
putarc2(P, Q)


setcolor(1, 0, 0)
t = texinsert(r"$\pi$".format(label))
t.translate(-t.width / 2, -t.height / 2)
t.scale(1.5)
place(t, 3.75, 0)

setcolor(0, 0, 1)
t = texinsert(r"$\pi'$".format(label))
t.translate(-t.width / 2, -t.height / 2)
t.scale(1.5)
place(t, 4.65, 0)
finish()
