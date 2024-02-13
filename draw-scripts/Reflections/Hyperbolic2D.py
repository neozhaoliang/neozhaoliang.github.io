from piscript.PiModule import *
import numpy as np


def hyperbolic2d():
    alpha = np.array([1, 0])
    alpha_vee = np.array([2, 0])

    beta = np.array([-3, 1])
    beta_vee = np.array([-0.8, -0.4])

    mat = np.array([[np.dot(alpha, alpha_vee), np.dot(alpha, beta_vee)],
                    [np.dot(beta, alpha_vee), np.dot(beta, beta_vee)]])
    print(mat)

    def ref(v):
        return v - np.dot(alpha, v) * alpha_vee

    def ref2(v):
        return v - np.dot(beta, v) * beta_vee

    e1 = np.array([1, 0])
    e2 = np.array([0, 1])

    f1 = ref(e1)
    f2 = ref(e2)

    g1 = ref2(e1)
    g2 = ref2(e2)

    init("hyperbolic2d.eps", 400, 400)
    center()
    scale(100)
    translate(0, -1.95)

    newpath()
    moveto(-4, 0)
    lineto(4, 0)
    stroke()

    newpath()
    moveto(0, 0)
    lineto(*np.array([beta[1], -beta[0]]) * 8)
    lineto(0, 8)
    closepath()
    fill(1, 1, 0)

    for word in ["s", "t", "st", "ts", "sts", "tst", "stst"]:
        if word[-1] == "t":
            r = np.array([beta[1], -beta[0]]) * 8
        else:
            r = np.array([0, 1]) * 8

        for w in reversed(word):
            if w == "s":
                r = ref(r)
            else:
                r = ref2(r)

        newpath()
        moveto(0, 0)
        lineto(*r)
        stroke()

    xlist = np.linspace(-2, 2, 50)
    ylist = np.sqrt(xlist * xlist + 1)
    newpath()
    moveto(xlist[0], ylist[0])
    for x, y in zip(xlist, ylist)[1:]:
        lineto(x, y)
    stroke()


    P = np.array([0.3, 1.6])

    sc = 1.5
    t = texinsert("$\mathcal{D}$")
    t.translate(-t.width/2, t.height/2)
    t.scale(sc)
    place(t, *P)

    t = texinsert("$s\mathcal{D}$")
    t.translate(-t.width/2, t.height/2)
    t.scale(sc)
    Q = ref(P)
    place(t, *Q)

    t = texinsert("$t\mathcal{D}$")
    t.translate(-t.width/2, t.height/2)
    t.scale(sc)
    Q = ref2(P)
    place(t, *Q)


    t = texinsert("$st\mathcal{D}$")
    t.translate(-t.width/2, t.height/2)
    t.scale(sc)
    Q = ref(ref2(P))
    place(t, *Q)


    t = texinsert("$ts\mathcal{D}$")
    t.translate(-t.width/2, t.height/2)
    t.scale(sc)
    Q = ref2(ref(P))
    place(t, *Q)

    t = texinsert("$sts\mathcal{D}$")
    t.translate(-t.width/2, t.height/2)
    t.scale(sc)
    Q = ref(ref2(ref(P)))
    place(t, *Q)

    sc = 1.5
    t = texinsert(r"$\alpha=0$")
    t.scale(sc)
    t.translate(-t.width, t.height/2)
    place(t, -0.2, 3)

    t = texinsert(r"$\beta=0$")
    t.scale(sc)
    t.translate(-t.width, t.height/2)
    place(t, 1, 3)

    newpath()
    moveto(0, 0)
    lineto(10, 10)
    stroke(1, 0, 0)

    newpath()
    moveto(0, 0)
    lineto(-10, 10)
    stroke(1, 0, 0)

    flush()

#reflection()
hyperbolic2d()
