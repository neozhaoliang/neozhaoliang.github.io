import numpy as np
from numpy import sin, cos, pi, sqrt
from piscript.PiModule import *


def draw_circle(cen, rad, col, type):
    newpath()
    if type == "C":
        circle(cen[0], cen[1], rad)
    else:
        n = complex(*cen)
        x = rad * n
        v = n * 1j
        start = x - 10 * v
        end = x + 10 * v
        moveto(start.real, start.imag)
        lineto(end.real, end.imag)
    stroke(*col)


blue = (0, 0, 1)
green = (0, 0.6, 0.2)
red = (1, 0, 0)
yellow = (0.7, 0.7, 0)


def get_circle(A, B, C):
    """Return the squared circumradius of a triangle."""
    dx, dy = B - A
    ex, ey = C - A
    bl = dx * dx + dy * dy
    cl = ex * ex + ey * ey
    d = 0.5 / (dx * ey - ex * dy)
    x = (ey * bl - dy * cl) * d
    y = (dx * cl - ex * bl) * d
    return np.array([x + A[0], y + A[1], np.sqrt(x * x + y * y)])


def stretch(circle):
    cen, r = circle[:2], circle[2]
    d = cen / np.linalg.norm(cen)
    return cen + r * d


init("compute_apollonian.eps", 400, 400)
center()
scale(50, 50)
translate(0, 0.2)

r = 3**0.5 / 2
C2 = np.array([0, 1, r])
C3 = np.array([np.cos(np.deg2rad(210)), np.sin(np.deg2rad(210)), r])
C4 = np.array([np.cos(np.deg2rad(330)), np.sin(np.deg2rad(330)), r])
C1 = np.array([0, 0, 1 + r])

r1 = (1 - r * r) ** 0.5
B1 = np.array([0, 0, r1])
B2 = get_circle([0, -r1], stretch(C3), stretch(C4))
B3 = get_circle(
    stretch(C2),
    r1 * np.array([np.cos(np.deg2rad(30)), np.sin(np.deg2rad(30))]),
    stretch(C4),
)
B4 = get_circle(
    stretch(C2),
    stretch(C3),
    r1 * np.array([np.cos(np.deg2rad(150)), np.sin(np.deg2rad(150))]),
)
draw_circle(C1[:2], C1[2], blue, "C")
draw_circle(C2[:2], C2[2], green, "C")
draw_circle(C3[:2], C3[2], red, "C")
draw_circle(C4[:2], C4[2], yellow, "C")


# draw_circle(B0[:2], B0[2], blue, "C")
# draw_circle(B1[:2], B1[2], green, "C")
# draw_circle(B2, 0, red, "L")
# draw_circle(B3, 0, yellow, "L")

fc = 1.5
setcolor(blue)
t = texinsert(r"$\hat{\omega}_1^\ast$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, -1.35 - r, 0)


setcolor(green)
t = texinsert(r"$\hat{\omega}_2$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, C2[0], C2[1])

setcolor(red)
t = texinsert(r"$\hat{\omega}_3$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, C3[0], C3[1])

setcolor(yellow)
t = texinsert(r"$\hat{\omega}_4$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, C4[0], C4[1])

setdash([4, 4])
scalelinewidth(0.5)

setcolor(blue)
draw_circle(B1[:2], B1[2], blue, "C")
t = texinsert(r"$\alpha_1^\ast$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, B1[0], B1[1])

setdash([4, 4])
scalelinewidth(0.5)
setcolor(green)
draw_circle(B2[:2], B2[2], green, "C")
t = texinsert(r"$\alpha_2^\ast$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, B2[0], B2[1])

setdash([4, 4])
scalelinewidth(0.5)
setcolor(red)
draw_circle(B3[:2], B3[2], red, "C")
t = texinsert(r"$\alpha_3^\ast$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, B3[0], B3[1])

setdash([4, 4])
scalelinewidth(0.5)
setcolor(yellow)
draw_circle(B4[:2], B4[2], yellow, "C")
t = texinsert(r"$\alpha_4^\ast$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, B4[0], B4[1])
"""


setcolor(yellow)
t = texinsert(r"$\alpha_4$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, 0.52, 1.15)

setcolor(green)
t = texinsert(r"$\alpha_2^{\ast}$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, -0.85, 1.1)

setcolor(blue)
t = texinsert(r"$\alpha_1^{\ast}$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, B0[0] - 0.025, B0[1])

t = texinsert(r"$\hat{\omega}_1^{\ast}$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, -1.1, 0)
"""
finish()
