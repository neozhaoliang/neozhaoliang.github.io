from piscript.PiModule import *
from math import *

L = 0.25
A = Vector(L, L)
B = Vector(L + 0.5, L)
C = Vector(L + 0.5, L + 0.5)
D = Vector(L, L + 0.5)
corners = [A, B, C, D]
out = [Vector(0, 0), Vector(1, 0), Vector(1, 1), Vector(0, 1)]
fontscale = 1.3
rad = 0.04
lw = 2


def dot(p, rad, color=(1, 1, 1)):
    newpath()
    circle(p, rad)
    fill(*color)
    stroke()


def dots(pts, rad):
    for i, p in enumerate(pts):
        color = (1, 1, 1) if i % 2 == 0 else (0, 0, 0)
        dot(p, rad, color)


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


def fillpoly(plist, color=(1, 1, 1)):
    newpath()
    moveto(plist[0])
    for p in plist[1:]:
        lineto(p)
    lineto(plist[0])
    closepath()
    fill(*color)


def path(plist, color=None, dash=False, fc=None):
    gsave()
    if dash:
        setdash([4, 4])

    newpath()
    moveto(plist[0])
    for p in plist[1:]:
        lineto(p)
    lineto(plist[0])
    closepath()
    if fc:
        fill(*fc)
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


def draw_square(vertices, dash=False, red_pairs=(), flip=False, fc=None):
    path(vertices, dash=dash, fc=fc)
    gsave()
    scalelinewidth(lw)
    for p, q in red_pairs:
        line(p, q, color=(1, 0, 0))
    grestore()

    if flip:
        dots(vertices, rad)
    else:
        dots(vertices[::-1], rad)


def draw_transformed(vertices, out, dash=False, red_pairs=(), lc=(0, 0, 0), fc=None):
    path(vertices, dash=dash, color=lc, fc=fc)
    for p, q in zip(vertices, out):
        if dash:
            dashline(p, q, color=lc)
        else:
            line(p, q, color=lc)

    for p, q in red_pairs:
        gsave()
        scalelinewidth(lw)
        for p, q in red_pairs:
            line(p, q, color=(1, 0, 0))
        grestore()


def gridlines(n, dash=False, flip=False):
    line_func = line if not dash else dashline
    for x in range(-n, n + 1):
        line_func((x, -n), (x, n))
        line_func((-n, x), (n, x))

    for x in range(-n, n + 1):
        for y in range(-n, n + 1):
            if ((x + y) % 2 == 1 and not flip) or ((x + y) % 2 == 0 and flip):
                fillpoly([p + Vector(x, y) for p in out], color=(0.9,) * 3)


def griddots(n, flip=False):
    for x in range(-n, n + 1):
        for y in range(-n, n + 1):
            if ((x + y) % 2 == 1 and not flip) or ((x + y) % 2 == 0 and flip):
                dot((x, y), rad, color=(1, 1, 1))
            else:
                dot((x, y), rad, color=(0, 0, 0))


def picture1():
    init("trans1.eps", 300, 300)
    center()
    scale(80)
    translate(0.5, -0.5)
    n = 3
    gridlines(n, dash=True)
    scalelinewidth(lw)
    for p, q in [
        [(0, 1), (1, 1)],
        [(0, 0), (1, 0)],
        [(-2, 0), (-1, 0)],
        [(-2, 1), (-2, 2)],
        [(-1, 1), (-1, 2)],
        [(0, 2), (0, 3)],
        [(1, 2), (1, 3)],
    ]:
        line(p, q, color=(1, 0, 0))
    griddots(n)

    text(r"\uppercase\expandafter{\romannumeral 1\relax}", (-1.5, 1.5), 1.5)
    text(r"\uppercase\expandafter{\romannumeral 2\relax}", (0.5, 1.5), 1.5)
    text(r"\uppercase\expandafter{\romannumeral 3\relax}", (-0.5, 0.5), 1.5)
    finish()


def picture2():
    init("trans2.eps", 300, 300)
    center()
    scale(80)
    translate(0.5, -0.5)
    n = 3
    gridlines(n)
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            if (i + j) % 2 == 1:
                verts = [p + Vector(i, j) for p in corners]
                oout = [p + Vector(i, j) for p in out]
                if i == -2 and j == 1:
                    pairs = list(zip(verts, oout))
                elif i == 0 and j == 1:
                    pairs = [
                        [verts[2], verts[3]],
                        [verts[0], oout[0]],
                        [verts[1], oout[1]],
                    ]
                elif i == -1 and j == 0:
                    pairs = [[verts[0], verts[1]], [verts[2], verts[3]]]
                else:
                    pairs = []
                draw_transformed(verts, oout, dash=True, red_pairs=pairs)
                dots(verts[::-1], rad)

    griddots(n)
    finish()


def picture3():
    init("trans3.eps", 300, 300)
    center()
    scale(80)
    translate(0.5, -0.5)
    n = 3
    for i in range(-n, n + 1):
        for j in range(-n, n + 1):
            if (i + j) % 2 == 1:
                verts = [p + Vector(i, j) for p in corners]
                oout = [p + Vector(i, j) for p in out]
                if i == -2 and j == 1:
                    pairs = list(zip(verts, oout))
                elif i == 0 and j == 1:
                    pairs = [
                        [verts[2], verts[3]],
                        [verts[0], oout[0]],
                        [verts[1], oout[1]],
                    ]
                elif i == -1 and j == 0:
                    pairs = [[verts[0], verts[1]], [verts[2], verts[3]]]
                else:
                    pairs = []
                draw_transformed(verts, oout, dash=True, red_pairs=pairs, fc=(0.9,) * 3)
                dots(verts[::-1], rad)

    griddots(n)
    finish()


def picture4():
    init("trans4.eps", 300, 300)
    center()
    scale(80)
    translate(0.5, -0.5)
    n = 3
    gridlines(n, dash=True, flip=True)
    scalelinewidth(lw)
    for p, q in [
        [(-1, 0), (0, 0)],
        [(-1, 1), (0, 1)],
        [(0, 2), (1, 2)],
    ]:
        line(p, q, color=(1, 0, 0))
    griddots(n, flip=True)

    text(r"\uppercase\expandafter{\romannumeral 1\relax}", (-1.5, 1.5), 1.5)
    text(r"\uppercase\expandafter{\romannumeral 2\relax}", (0.5, 1.5), 1.5)
    text(r"\uppercase\expandafter{\romannumeral 3\relax}", (-0.5, 0.5), 1.5)
    finish()


picture1()
picture2()
picture3()
picture4()
