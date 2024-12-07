from piscript.PiModule import *
from math import *

L = 0.8
A = Vector(1, 1) * L
B = Vector(-1, 1) * L
C = Vector(-1, -1) * L
D = Vector(1, -1) * L
corners = [A, B, C, D]
out = [2 * p for p in corners]
fontscale = 1.3
rad = 0.08
lw = 3


def fork(p, n, ll):
    gsave()
    setdash([4, 4])
    scalelinewidth(0.5)
    p = Vector(p)
    n = Vector(n)
    q = p + n * ll
    newpath()
    moveto(p)
    lineto(q)
    stroke()
    grestore()


def fork_all(pts, ll=0.5):
    for p, n in zip(pts, corners):
        fork(p, n, ll)


def dots(pts, rad):
    for i, p in enumerate(pts):
        newpath()
        circle(p, rad)
        if i % 2 == 0:
            fill(0)
        else:
            fill(1)
        stroke()


def line(p, q, color=None):
    newpath()
    moveto(p)
    lineto(q)
    if color:
        stroke(*color)
    else:
        stroke()


def dashline(p, q, color=None):
    gsave()
    setdash([4, 4], 0)
    newpath()
    moveto(p)
    lineto(q)
    if color:
        stroke(*color)
    else:
        stroke()
    grestore()


def path(plist, color=None, dash=False):
    gsave()
    if dash:
        setdash([4, 4])

    newpath()
    moveto(plist[0])
    for p in plist[1:]:
        lineto(p)
    lineto(plist[0])
    closepath()
    if color:
        stroke(*color)
    else:
        stroke()
    grestore()


def text(string, pos, sc):
    t = texinsert(string)
    t.scale(sc)
    t.translate(-t.width / 2, -t.height / 2)
    place(t, pos)


def draw_square(draw_texts=False, weights=True, dash=False, red_pairs=(), flip=False):
    path(corners, dash=dash)
    fork_all(corners)
    gsave()
    scalelinewidth(lw)
    for p, q in red_pairs:
        line(p, q, color=(1, 0, 0))
    grestore()

    if flip:
        dots(corners[::-1], rad)
    else:
        dots(corners, rad)

    if draw_texts:
        text("$A$", A + (0.2, -0.2), fontscale)
        text("$B$", B + (-0.5, -0.15), fontscale)
        text("$C$", C + (-0.15, -0.5), fontscale)
        text("$D$", D + (-0.1, -0.5), fontscale)

    if weights:
        pos = Vector(0, L) + Vector(0, 0.3)
        text(r"$x$", pos, fontscale)

        pos = Vector(L, 0) + Vector(0.3, 0)
        text(r"$y$", pos, fontscale)

        pos = Vector(0, -L) + Vector(0, -0.35)
        text(r"$z$", pos, fontscale)

        pos = Vector(-L, 0) + Vector(-0.35, 0)
        text(r"$w$", pos, fontscale)


def draw_transformed(draw_texts=False, weights=True, dash=False, red_pairs=()):
    path(corners, dash=dash)
    fork_all(out)

    for p, q in zip(corners, out):
        if dash:
            dashline(p, q)
        else:
            line(p, q)

    for p, q in red_pairs:
        gsave()
        scalelinewidth(lw)
        for p, q in red_pairs:
            line(p, q, color=(1, 0, 0))
        grestore()

    if draw_texts:
        text("$A$", A + (0.2, -0.2), fontscale)
        text("$B$", B + (-0.4, -0.3), fontscale)
        text("$C$", C + (-0.1, -0.4), fontscale)
        text("$D$", D + (-0.2, -0.4), fontscale)

    if weights:
        for s, t in zip(corners, out):
            text("$1$", (s + t) / 2, fontscale)

        pos = Vector(0, -L) + Vector(0, -0.35)
        text(r"$x/\Delta$", pos, fontscale)

        pos = Vector(-L, 0) + Vector(-0.6, 0)
        text(r"$y/\Delta$", pos, fontscale)

        pos = Vector(0, L) + Vector(0, 0.4)
        text(r"$z/\Delta$", pos, fontscale)

        pos = Vector(L, 0) + Vector(0.4, 0)
        text(r"$w/\Delta$", pos, fontscale)

    dots(corners[::-1] + out, rad)


def case1():
    init("case1.eps", 560, 200)
    center()
    scale(40)

    gsave()
    translate(-5, 0)
    draw_square(weights=False, dash=True, red_pairs=((A, B), (C, D)))
    grestore()

    gsave()
    # translate(0, 0)
    draw_transformed(weights=False, dash=True, red_pairs=list(zip(corners, out)))
    grestore()

    setarrowdims(0.06, 0.25)
    arrow((-3.2, 0), (-2, 0))
    stroke()

    arrow((2, 0), (3.2, 0))
    stroke()

    gsave()
    translate(5, 0)
    oout = [p * 0.75 for p in out]
    draw_square(weights=False, dash=True, flip=True, red_pairs=list(zip(corners, oout)))
    grestore()
    finish()


def case2():
    init("case2.eps", 560, 200)
    center()
    scale(40)

    gsave()
    translate(-5, 0)
    draw_square(
        weights=False,
        dash=True,
        red_pairs=[(A, B), (C, C * 1.5), (D, D * 1.5)],
    )
    grestore()

    gsave()
    draw_transformed(
        weights=False,
        dash=True,
        red_pairs=[
            (C, D),
            (A, out[0]),
            (B, out[1]),
            (out[2], out[2] * 1.25),
            (out[3], out[3] * 1.25),
        ],
    )
    grestore()

    setarrowdims(0.06, 0.25)
    arrow((-3.2, 0), (-2, 0))
    stroke()

    arrow((2, 0), (3.2, 0))
    stroke()

    gsave()
    translate(5, 0)
    draw_square(
        weights=False,
        dash=True,
        red_pairs=[(C, D), (A, A * 1.5), (B, B * 1.5)],
        flip=True,
    )
    grestore()

    finish()


def case3():
    init("case3.eps", 560, 200)
    center()
    scale(40)

    gsave()
    translate(-5, 0)
    draw_square(
        weights=False, dash=True, red_pairs=list(zip(corners, [p * 0.75 for p in out]))
    )
    grestore()

    oout = [p * 1.25 for p in out]
    pairs = list(zip(out, oout))

    gsave()
    draw_transformed(weights=False, dash=True, red_pairs=[(A, B), (C, D)] + pairs)
    grestore()

    setarrowdims(0.06, 0.25)
    arrow((-3.2, 0), (-2, 0))
    stroke()
    arrow((2, 0), (3.2, 0))
    stroke()

    gsave()
    translate(5, 0)
    draw_square(weights=False, dash=True, red_pairs=[(A, B), (C, D)], flip=True)
    grestore()

    finish()


# case1()
# case2()
case3()
