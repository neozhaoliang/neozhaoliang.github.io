from piscript.PiModule import *
import numpy as np


init(400, 400, "weights.eps")
setfont("CMR10", 10)
center()
scale(25)
translate(-0.3, 0.3)


def dir(ang):
    a = np.radians(ang)
    return complex(np.cos(a), np.sin(a))

# basis of dual space
e1 = dir(0)
e2 = dir(120)
e3 = -(e1 + e2)

# fundamental integral weights
w1 = e1
w2 = e1 + e2

# positive roots
a1 = e1 - e2
a2 = e2 - e3
a3 = e1 - e3

# rho
rho = (a1 + a2 + a3) / 2

# highest weight
m, n = 3, 2
P = m*w1 + n*w2


def make_fundamental_chamber(bg_col=0.9):
    newpath()
    moveto(P.real, P.imag)
    A = P - a1 * 1000
    B = P - a2 * 1000
    lineto(A.real, A.imag)
    lineto(B.real, B.imag)
    lineto(P.real, P.imag)
    closepath()
    fill(bg_col)
    stroke(0.5)


def make_verma_cone(bg_col=0.8):
    newpath()
    moveto(0, 0)
    lineto(e1.real*100, e1.imag*100)
    lineto(-e3.real*100, -e3.imag*100)
    lineto(0, 0)
    closepath()
    fill(bg_col)
    stroke()


def make_grid(N=15, grid_col=0.75):
    for k in range(-N, N+1):
        for e in [e1, e2, e3]:
            newpath()
            A = e*N + k * e * 1j * np.sqrt(3) / 2
            B = -e*N + k * e * 1j * np.sqrt(3) / 2
            moveto(A.real, A.imag)
            lineto(B.real, B.imag)
            if k != 0:
                stroke(grid_col)
            else:
                gsave()
                scalelinewidth(1.5)
                stroke(0)
                grestore()


def make_sl3_roots(rad=0.12, col=(0, 0.5, 1)):
    for Q in [a1, a2, a3]:
        newpath()
        circle(Q.real, Q.imag, rad)
        fill(*col)
        stroke()

        newpath()
        circle(-Q.real, -Q.imag, rad)
        fill(*col)
        stroke()


def ref(start, dir, draw=True, col=(1, 0, 0.5), rad=0.12, mul=1):
    S = start
    D = dir
    d = S.real * D.real + S.imag * D.imag
    aa = D.real**2 + D.imag**2
    k = np.round(d * 2 / aa).astype(int)
    E = S - k * D
    if not draw:
        return E

    newpath()
    moveto(S.real, S.imag)
    lineto(E.real, E.imag)
    stroke(*col)
    for i in range(k+1):
        Q = S - i * D

        if mul > 2:
            newpath()
            circle(Q.real, Q.imag, rad*2.4)
            fill(1)
            stroke()
        if mul > 1:
            newpath()
            circle(Q.real, Q.imag, rad*1.8)
            fill(1)
            stroke()

        newpath()
        circle(Q.real, Q.imag, rad*1.2)
        fill(*col)
        stroke()

    return E


def make_polygon(P, mul=1):
    P1 = ref(P, a1, mul=mul)
    P2 = ref(P, a2, mul=mul)
    P3 = ref(P1, w1+w2, mul=mul)
    P4 = ref(P3, a2, mul=mul)
    P5 = ref(P2, w1+w2, mul=mul)
    P6 = ref(P5, a1, mul=mul)


def draw_large_circle(col=(0, 0.5, 1)):
    rad = abs(P + a1 + a2)
    cen = -(a1 + a2)
    newpath()
    circle(cen.real, cen.imag, rad)
    stroke(*col)


def make_highest_label():
    t = texinsert(r"$\lambda = {}\omega_1 + {}\omega_2$".format(m, n))
    t.translate(-t.width/2, 0)
    t.scale(1.4)
    place(t, P.real*1.3, P.imag*1.3)


def make_singular_vector(rad=0.12):
    P1 = ref(P + rho, a1, False) - rho
    P2 = ref(P + rho, a2, False) - rho
    P3 = ref(P1 + rho, w1+w2, False) - rho
    P4 = ref(P3 + rho, a2, False) - rho
    P5 = ref(P4 + rho, a1, False) - rho

    Y = P1
    Z = P2
    newpath()
    circle(Y.real, Y.imag, rad*1.2)
    fill(0, 1, .5)
    stroke()

    newpath()
    circle(Z.real, Z.imag, rad*1.2)
    fill(0, 1, .5)
    stroke()

    for G in [P3, P4, P5]:
        newpath()
        circle(G.real, G.imag, rad*1.2)
        fill(0, 1, .5)
        stroke()

    sc = 1.4
    t = texinsert(r"$f_{\alpha_1}^{\lambda(\alpha_1^\vee)+1}v^+$")
    t.scale(sc)
    place(t, Y.real, Y.imag+0.4)

    t = texinsert(r"$f_{\alpha_2}^{\lambda(\alpha_2^\vee)+1}v^+$")
    t.translate(0, -t.height/2)
    t.scale(sc)
    place(t, Z.real+0.4, Z.imag)


def make_simple_roots_label():
    sc = 1.4
    t = texinsert(r"$\alpha_1$")
    t.translate(-t.width/2, 0)
    t.scale(sc)
    Q = e1 - e2
    place(t, Q.real*1.3, Q.imag*1.3)

    t = texinsert(r"$\alpha_2$")
    t.translate(-t.width/2, 0)
    t.scale(sc)
    Q = e2 - e3
    place(t, Q.real*1.2-0.5, Q.imag*1.2-0.2)


def make_rho_label():
    sc = 1.4
    t = texinsert(r"$\rho$")
    t.translate(-t.width/2, 0)
    t.scale(sc)
    place(t, rho.real*1.3, rho.imag*1.3)


def make_fundamental_weights(rad=0.12):
    newpath()
    circle(w2.real, w2.imag, rad*0.8)
    fill(1, 1, 0)
    stroke()

    newpath()
    circle(w1.real, w1.imag, rad*0.7)
    fill(1, 1, 0)
    gsave()
    scalelinewidth(0.5)
    stroke()
    grestore()


def make_arrows():
    sc = 1.4
    A = 1.*w1 + 4*w2
    B = ref(A, a1, False)
    setarrowdims(0.1, 0.3)
    newpath()
    arrow((A.real, A.imag), (B.real, B.imag))
    fill(1)
    stroke()

    t = texinsert(r"$-\alpha_1$")
    t.translate(-t.width/2, 0)
    t.scale(sc)
    Q = (A+B)/2
    place(t, Q.real*1.1+0.5, Q.imag*1.1-0.2)


    A = 5*w1 + 1*w2
    C = ref(A, a2, False)
    newpath()
    arrow((A.real, A.imag), (C.real, C.imag))
    fill(1)
    stroke()

    t = texinsert(r"$-\alpha_2$")
    t.translate(0, -t.height/2)
    t.scale(sc)
    Q = (A+C)/2
    place(t, Q.real*1.1-0.2, Q.imag*1.1-0.4)


if __name__ == "__main__":
    make_fundamental_chamber()
    make_verma_cone()
    make_grid()
    draw_large_circle()
    make_fundamental_weights()
    make_sl3_roots()
    make_singular_vector()
    make_arrows()
    make_highest_label()
    make_rho_label()
    make_simple_roots_label()
    make_polygon(P)
    make_polygon(P - a1 - a2, mul=2)
    make_polygon(P - 2*a1 - 2*a2, mul=3)
    flush()
