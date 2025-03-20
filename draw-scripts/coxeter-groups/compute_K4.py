import numpy as np
from numpy import sin, cos, pi, sqrt
from piscript.PiModule import *

inf = 1.0


def dihedral(x):
    if x == inf:
        return inf
    return cos(pi / x)


def get_circles(
    dihedralAngle2_3,  # v2, v3 angle, for example 4
    # angles in order: (v0, v2), (v0, v3), (v1, v2), (v1, v3)
    # for example (4, 4, 4, 4)
    dihedralAngles01_23,
    # v0, v1 angle, for example 4
    dihedralAngle0_1,
):
    # B2, B3 are always two lines
    c23 = dihedral(dihedralAngle2_3)
    s23 = sqrt(1 - c23 * c23)
    B2 = np.array([1, 0])
    B3 = np.array([-c23, s23])

    # solve for virtual B1
    # get dihedral angles between (v1, v2) (v1, v3)
    # --------
    # x = c12 * r
    # x * -c23 + y * s23 = r c13
    # x^2 + y^2 = r^2 + 1
    c12 = dihedral(dihedralAngles01_23[2])
    c13 = dihedral(dihedralAngles01_23[3])
    k1 = c12
    k2 = (c13 + c23 * c12) / s23
    r = 1 / sqrt(k1 * k1 + k2 * k2 - 1)
    B1 = np.array([k1 * r, k2 * r, r])

    # solve for virtual Ball B0
    # ------
    # x = r * c02
    # x * -c23 + y * s23 = c03
    #
    # r^2 + r1^2 - (x - x1)^2 - (y - y1)^2
    # ------------------------------------ = c01
    #                2 * r * r1
    c02 = dihedral(dihedralAngles01_23[0])
    c03 = dihedral(dihedralAngles01_23[1])
    c01 = dihedral(dihedralAngle0_1)
    k1 = c02
    k2 = (c03 + c23 * c02) / s23
    # quadratic equation for r
    # ar^2 - 2br + c = 0
    # a = k1^2 + k2^2 - 1
    # b = k1x1 + k2y1 + c01r1
    # c = x1^2 + y1^2 - r1^2
    a = k1 * k1 + k2 * k2 - 1
    b = np.dot([k1, k2, c01], B1)
    c = np.dot(B1[:2], B1[:2]) - B1[2] * B1[2]

    # there are two solutions for B0
    r = b / a + sqrt(b * b - a * c) / a
    r_ = b / a - sqrt(b * b - a * c) / a
    B0 = np.array([k1 * r_, k2 * r_, r_])
    return B0, B1, B2, B3


def L2(d1, d2):
    return np.dot(d1 - d2, d1 - d2)


def getIntersection(B1, B2, B3):
    n = np.array([B3[1], -B3[0]])
    k = (
        np.dot(B1[:2], B1[:2])
        - np.dot(B2[:2], B2[:2])
        - (B1[2] * B1[2] - B2[2] * B2[2])
    )
    k /= 2 * np.dot(B1[:2] - B2[:2], n)
    cen = k * n
    return cen


def solveBall(B1, B2, B3):
    """Solve the ball that is orthogonal to all three other balls B1, B2, B3
    where B1, B2 are circles and B3 is a line
    """
    # C = k * n, n is orthogonal to B3's normal
    n = np.array([B3[1], -B3[0]])
    k = (
        np.dot(B1[:2], B1[:2])
        - np.dot(B2[:2], B2[:2])
        - (B1[2] * B1[2] - B2[2] * B2[2])
    )
    k /= 2 * np.dot(B1[:2] - B2[:2], n)
    cen = k * n
    r = sqrt(np.dot(cen - B1[:2], cen - B1[:2]) - B1[2] * B1[2])
    return np.array([cen[0], cen[1], r])


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


init("compute_example.eps", 400, 400)
center()
scale(120, 120)
translate(-0.2, -0.2)


B0, B1, B2, B3 = get_circles(4, (4, 4, 4, 4), 4)

C0 = np.array([0, 0, 1])
C1 = np.array([0, 0, sqrt(np.dot(B0[:2], B0[:2]) - B0[2] * B0[2])])
C2 = solveBall(B0, B1, B3)
C3 = solveBall(B0, B1, B2)

blue = (0, 0, 1)
green = (0, 0.6, 0.2)
red = (1, 0, 0)
yellow = (0.7, 0.7, 0)


draw_circle(C0[:2], C0[2], blue, "C")
draw_circle(C1[:2], C1[2], green, "C")
draw_circle(C2[:2], C2[2], red, "C")
draw_circle(C3[:2], C3[2], yellow, "C")

setdash([4, 4])
scalelinewidth(0.5)
draw_circle(B0[:2], B0[2], blue, "C")
draw_circle(B1[:2], B1[2], green, "C")
draw_circle(B2, 0, red, "L")
draw_circle(B3, 0, yellow, "L")

inv = "\\ast"

fc = 1.5
setcolor(red)
t = texinsert(r"$\alpha_3$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, 0, 1.7)

t = texinsert(r"$\hat{\omega}_3$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, C2[0], C2[1])

setcolor(yellow)
t = texinsert(r"$\alpha_4$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, 1.35, 1.4)

t = texinsert(r"$\hat{\omega}_4$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, C3[0] - 0.1, C3[1])

setcolor(green)
t = texinsert(r"$\alpha_2^{\ast}$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, B1[0], B1[1])

t = texinsert(r"$\hat{\omega}_2$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, C1[0], C1[1])

setcolor(blue)
t = texinsert(r"$\alpha_1^{\ast}$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, B0[0] - 0.025, B0[1])

t = texinsert(r"$\hat{\omega}_1^{\ast}$")
t.scale(fc)
t.translate(-t.width / 2, -t.height / 2)
place(t, -1.15, 0)
finish()
