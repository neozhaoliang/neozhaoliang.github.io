import numpy as np
from numpy import sin, cos, pi, sqrt
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams.update({"text.usetex": True, "font.family": "Courier", "font.size": 12})

inf = -1.0


def dihedral(x):
    if x == inf:
        return 1
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


def draw_circle(ax, cen, rad, col, type, ls="-"):
    if type == "C":
        ax.add_patch(plt.Circle(cen, rad, ec=col, fc="none", ls=ls))
    else:
        n = complex(*cen)
        x = rad * n
        v = n * 1j
        start = x - 10 * v
        end = x + 10 * v
        ax.plot([start.real, end.real], [start.imag, end.imag], color=col, ls=ls)


def main():
    fig = plt.figure(figsize=(6, 6), dpi=100)
    ax = fig.add_axes([0, 0, 1, 1], aspect=1)
    ax.axis([-1.2, 1.6, -1.2, 2])
    ax.axis("off")

    B0, B1, B2, B3 = get_circles(4, (4, 4, 4, 4), 4)

    C0 = np.array([0, 0, 1])  # 第一个实球是单位圆
    C1 = np.array([0, 0, sqrt(np.dot(B0[:2], B0[:2]) - B0[2] * B0[2])])
    C2 = solveBall(B0, B1, B3)
    C3 = solveBall(B0, B1, B2)

    draw_circle(ax, C0[:2], C0[2], "b", "C")
    draw_circle(ax, B0[:2], B0[2], "b", "C", ls="--")

    draw_circle(ax, B1[:2], B1[2], "g", "C", ls="--")
    draw_circle(ax, C1[:2], C1[2], "g", "C")

    draw_circle(ax, B2, 0, "r", "L", ls="--")
    draw_circle(ax, C2[:2], C2[2], "r", "C")

    draw_circle(ax, B3, 0, "y", "L", ls="--")
    draw_circle(ax, C3[:2], C3[2], "y", "C")

    ax.text(-0.15, 1.7, r"$B_3=\alpha_3$", fontsize="large", color="r")
    ax.text(1.3, 1.5, r"$B_4=\alpha_4$", fontsize="large", color="y")
    ax.text(0.5, 1.6, r"$B_2^{\rm inv}=\alpha_2$", fontsize="large", color="g")
    ax.text(-0.3, 0.35, r"$B_1^{\rm inv}=\alpha_1$", fontsize="large", color="b")

    ax.text(0.4, 0.68, r"$C_3=\hat{\omega_3}$", fontsize="large", color="r")
    ax.text(0.05, 0.82, r"$C_4=\hat{\omega_4}$", fontsize="large", color="y")
    ax.text(-0.5, 0.0, r"$C_2=\hat{\omega_3}$", fontsize="large", color="g")
    ax.text(-0.9, 0.7, r"$C_1^{\rm inv}=\hat{\omega_1}$", fontsize="large", color="b")
    P = getIntersection(B0, B1, B2)

    fig.savefig("compute_example.svg")


if __name__ == "__main__":
    main()
