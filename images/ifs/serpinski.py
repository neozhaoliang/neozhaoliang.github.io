import cairo
import numpy as np
import drawsvg as draw

lev = 6
name = f"dot{lev}.svg"
surface = cairo.SVGSurface(name, 64, 64)
ctx = cairo.Context(surface)
ctx.scale(64, 64)
ctx.set_source_rgb(1, 1, 1)
ctx.paint()


def draw_circle(center, radius, fc, lw):
    ctx.arc(center[0], center[1], radius, 0, 2 * np.pi)
    ctx.set_source_rgb(*fc)
    ctx.fill_preserve()
    ctx.set_source_rgb(0, 0, 0)
    ctx.set_line_width(lw)
    ctx.stroke()


def level0():
    global surface
    draw_circle((0.5, 0.5), 0.4, (1, 1, 1), 0.09)
    surface.finish()


def T1(x, y):
    return x / 2, y / 2


def T2(x, y):
    return x / 2 + 0.5, y / 2 + 0.5


def T3(x, y):
    return x / 2, y / 2 + 0.5


trans = [T1, T2, T3]
colors = [
    (0, 1, 0),
    (0, 0, 1),
    (1, 0, 0),
]


def level1(k):
    global surface
    p0 = [0.5, 0.5]
    pts = [p0]
    for i in range(k):
        result = []
        for t in trans:
            li = [t(*p) for p in pts]
            result += li
        pts = result

    for i, p in enumerate(pts):
        j = 3 * i // len(pts)
        draw_circle(p, 0.4 / 2**k, colors[j], 0.09 / 2**k)

    surface.finish()


level1(lev)
