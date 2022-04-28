from piscript.PiModule import *
from math import *


N = Vector(0, 1)
S = Vector(0, -1)
W = Vector(-1, 0)
E = Vector(1, 0)


def fork(p, n, L):
    p = Vector(p)
    n = Vector(n)
    q1 = p + n * L
    q2 = p + n.rotated(pi/4) * L
    q3 = p + n.rotated(-pi/4) * L
    for q in [q1, q2, q3]:
        newpath()
        moveto(p)
        lineto(q)
        stroke()

def fork_all(pts, L):
    for p, n in zip(pts, [E, N, W, S]):
        fork(p, n, L)

def dots(pts, rad):
    for p in pts:
        newpath()
        circle(p, rad)
        fill(1, 0, 0)
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

def path(plist, color=None):
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

def text(string, pos, sc):
    newpath()
    t = texinsert(string)
    t.scale(sc)
    place(t, pos)

def spidermove():
    init("spidermove.eps", 600, 250)
    center()
    scale(50)

    center1 = Vector(-3.5, 0)
    lpoints = [center1 + p for p in [E, N, W, S]]
    center2 = Vector(3.5, 0)
    rpoints = [center2 + 2 * p for p in [E, N, W, S]]
    out = [center1 + 2 * p for p in [E, N, W, S]]

    path(lpoints)
    path(rpoints)
    fork_all(out, 0.3)
    fork_all(rpoints, 0.3)

    for p, q in zip(lpoints, out):
        line(p, q)

    fontscale = 1.5
    pos = out[0] + (-0.2, 0.2)
    text("$A$", pos, fontscale)

    pos = out[1] + (-0.4, -0.3)
    text("$B$", pos, fontscale)

    pos = out[2] + (-0.1, -0.4)
    text("$C$", pos, fontscale)

    pos = out[3] + (0.1, 0.1)
    text("$D$", pos, fontscale)

    pos = rpoints[0] + (-0.1, 0.3)
    text("$A$", pos, fontscale)

    pos = rpoints[1] + (-0.5, -0.15)
    text("$B$", pos, fontscale)

    pos = rpoints[2] + (-0.15, -0.5)
    text("$C$", pos, fontscale)

    pos = rpoints[3] + (0.2, -0.1)
    text("$D$", pos, fontscale)

    pos = center1 + Vector(cos(pi/4), sin(pi/4)) * .8
    text("$x$", pos, fontscale)

    pos = center1 + Vector(cos(3*pi/4), sin(3*pi/4)) - (0, 0.1)
    text("$y$", pos, fontscale)

    pos = center1 + Vector(cos(5*pi/4), sin(5*pi/4)) * 1.05
    text("$z$", pos, fontscale)

    pos = center1 + Vector(cos(-pi/4), sin(-pi/4)) * .8 - (0.05, 0.2)
    text("$w$", pos, fontscale)

    pos = center2 + Vector(cos(pi/4), sin(pi/4)) * 1.6 - (0.1, 0)
    text(r"$z/\Delta$", pos, fontscale)

    pos = center2 + 2 * Vector(cos(3*pi/4), sin(3*pi/4)) - (0.35, 0.25)
    text(r"$w/\Delta$", pos, fontscale)

    pos = center2 + 2 * Vector(cos(5*pi/4), sin(5*pi/4)) + (-0.35, 0.1)
    text(r"$x/\Delta$", pos, fontscale)

    pos = center2 + 2 * Vector(cos(-pi/4), sin(-pi/4)) * .8 - (0.1, 0.2)
    text(r"$y/\Delta$", pos, fontscale)

    arrow_size = 0.7
    setarrowdims(0.06, 0.25)
    arrow((-arrow_size, 0), (arrow_size, 0))
    stroke()
    dots(lpoints + rpoints + out, 0.07)
    finish()

def case1():
    init("case1.eps", 800, 250)
    center()
    scale(50)

    center1 = Vector(-5.5, 0)
    center2 = Vector(0, 0)
    center3 = Vector(5.5, 0)

    lpoints = [center1 + p for p in [E, N, W, S]]
    mpoints = [center2 + p for p in [E, N, W, S]]
    rpoints = [center3 + 2 * p for p in [E, N, W, S]]

    out1 = [center1 + 2 * p for p in [E, N, W, S]]
    out2 = [center2 + 2 * p for p in [E, N, W, S]]

    fork_all(out1, 0.3)
    fork_all(out2, 0.3)
    fork_all(rpoints, 0.3)


    color = (0, 0, 1)
    line(lpoints[0], lpoints[1], color)
    line(lpoints[2], lpoints[3], color)
    line(mpoints[1], mpoints[2], color)
    line(mpoints[3], mpoints[0], color)

    setarrowdims(0.06, 0.2)
    arrow_size = Vector(0.3, 0)
    arrow_pos = (center2 + center3) / 2
    newpath()
    arrow(arrow_pos-arrow_size, arrow_pos+arrow_size)
    stroke()

    add_pos = (center1 + center2) / 2
    add_x = Vector(0.2, 0)
    add_y = Vector(0, 0.2)
    scalelinewidth(4)
    line(add_pos-add_x, add_pos+add_x)
    line(add_pos-add_y, add_pos+add_y)
    scalelinewidth(1.0/4)

    gsave()
    setdash([4, 4], 0)
    line(lpoints[1], lpoints[2])
    line(lpoints[0], lpoints[3])
    line(mpoints[0], mpoints[1])
    line(mpoints[2], mpoints[3])

    for p, q in zip(lpoints, out1):
        line(p, q)

    for p, q in zip(mpoints, out2):
        line(p, q)

    path(rpoints)
    grestore()

    fontscale = 1.5
    pos = out1[0] + (-0.2, 0.2)
    text("$A$", pos, fontscale)

    pos = out1[1] + (-0.4, -0.3)
    text("$B$", pos, fontscale)

    pos = out1[2] + (-0.1, -0.4)
    text("$C$", pos, fontscale)

    pos = out1[3] + (0.1, 0.1)
    text("$D$", pos, fontscale)

    pos = out2[0] + (-0.2, 0.2)
    text("$A$", pos, fontscale)

    pos = out2[1] + (-0.4, -0.3)
    text("$B$", pos, fontscale)

    pos = out2[2] + (-0.1, -0.4)
    text("$C$", pos, fontscale)

    pos = out2[3] + (0.1, 0.1)
    text("$D$", pos, fontscale)

    pos = center1 + Vector(cos(pi/4), sin(pi/4)) * .8
    text("$x$", pos, fontscale)

    pos = center1 + Vector(cos(3*pi/4), sin(3*pi/4)) - (0, 0.1)
    text("$y$", pos, fontscale)

    pos = center1 + Vector(cos(5*pi/4), sin(5*pi/4)) * 1.05
    text("$z$", pos, fontscale)

    pos = center1 + Vector(cos(-pi/4), sin(-pi/4)) * .8 - (0.05, 0.2)
    text("$w$", pos, fontscale)

    pos = center2 + Vector(cos(pi/4), sin(pi/4)) * .8
    text("$x$", pos, fontscale)

    pos = center2 + Vector(cos(3*pi/4), sin(3*pi/4)) - (0, 0.1)
    text("$y$", pos, fontscale)

    pos = center2 + Vector(cos(5*pi/4), sin(5*pi/4)) * 1.05
    text("$z$", pos, fontscale)

    pos = center2 + Vector(cos(-pi/4), sin(-pi/4)) * .8 - (0.05, 0.2)
    text("$w$", pos, fontscale)

    pos = rpoints[0] + (-0.1, 0.3)
    text("$A$", pos, fontscale)

    pos = rpoints[1] + (-0.5, -0.15)
    text("$B$", pos, fontscale)

    pos = rpoints[2] + (-0.15, -0.5)
    text("$C$", pos, fontscale)

    pos = rpoints[3] + (0.2, -0.1)
    text("$D$", pos, fontscale)

    pos = center3 + Vector(cos(pi/4), sin(pi/4)) * 1.6 - (0.1, 0)
    text(r"$z/\Delta$", pos, fontscale)

    pos = center3 + 2 * Vector(cos(3*pi/4), sin(3*pi/4)) - (0.35, 0.25)
    text(r"$w/\Delta$", pos, fontscale)

    pos = center3 + 2 * Vector(cos(5*pi/4), sin(5*pi/4)) + (-0.35, 0.1)
    text(r"$x/\Delta$", pos, fontscale)

    pos = center3 + 2 * Vector(cos(-pi/4), sin(-pi/4)) * .8 - (0.1, 0.2)
    text(r"$y/\Delta$", pos, fontscale)

    dots(lpoints + mpoints + rpoints + out1 + out2, 0.07)
    finish()

def case2():
    init("case2.eps", 600, 250)
    center()
    scale(50)

    center1 = Vector(-3.5, 0)
    lpoints = [center1 + p for p in [E, N, W, S]]
    center2 = Vector(3.5, 0)
    rpoints = [center2 + 2 * p for p in [E, N, W, S]]
    out = [center1 + 2 * p for p in [E, N, W, S]]

    color = (0, 0, 1)
    fork_all(out, 0.3)
    fork_all(rpoints, 0.3)
    line(lpoints[0], lpoints[3], color)
    line(out[1], lpoints[1], color)
    line(out[2], lpoints[2], color)
    line(rpoints[1], rpoints[2], color)

    dashline(out[0], lpoints[0])
    dashline(out[3], lpoints[3])
    dashline(lpoints[0], lpoints[1])
    dashline(lpoints[1], lpoints[2])
    dashline(lpoints[2], lpoints[3])
    dashline(rpoints[0], rpoints[1])
    dashline(rpoints[0], rpoints[3])
    dashline(rpoints[2], rpoints[3])

    fontscale = 1.5
    pos = out[0] + (-0.2, 0.2)
    text("$A$", pos, fontscale)

    pos = out[1] + (-0.4, -0.3)
    text("$B$", pos, fontscale)

    pos = out[2] + (-0.1, -0.4)
    text("$C$", pos, fontscale)

    pos = out[3] + (0.1, 0.1)
    text("$D$", pos, fontscale)

    pos = rpoints[0] + (-0.1, 0.3)
    text("$A$", pos, fontscale)

    pos = rpoints[1] + (-0.5, -0.15)
    text("$B$", pos, fontscale)

    pos = rpoints[2] + (-0.15, -0.5)
    text("$C$", pos, fontscale)

    pos = rpoints[3] + (0.2, -0.1)
    text("$D$", pos, fontscale)

    pos = center1 + Vector(cos(pi/4), sin(pi/4)) * .8
    text("$x$", pos, fontscale)

    pos = center1 + Vector(cos(3*pi/4), sin(3*pi/4)) - (0, 0.1)
    text("$y$", pos, fontscale)

    pos = center1 + Vector(cos(5*pi/4), sin(5*pi/4)) * 1.05
    text("$z$", pos, fontscale)

    pos = center1 + Vector(cos(-pi/4), sin(-pi/4)) * .8 - (0.05, 0.2)
    text("$w$", pos, fontscale)

    pos = center2 + Vector(cos(pi/4), sin(pi/4)) * 1.6 - (0.1, 0)
    text(r"$z/\Delta$", pos, fontscale)

    pos = center2 + 2 * Vector(cos(3*pi/4), sin(3*pi/4)) - (0.35, 0.25)
    text(r"$w/\Delta$", pos, fontscale)

    pos = center2 + 2 * Vector(cos(5*pi/4), sin(5*pi/4)) + (-0.35, 0.1)
    text(r"$x/\Delta$", pos, fontscale)

    pos = center2 + 2 * Vector(cos(-pi/4), sin(-pi/4)) * .8 - (0.1, 0.2)
    text(r"$y/\Delta$", pos, fontscale)

    arrow_size = 0.7
    setarrowdims(0.06, 0.25)
    arrow((-arrow_size, 0), (arrow_size, 0))
    stroke()
    dots(lpoints + rpoints + out, 0.07)
    finish()

def case3():
    init("case3.eps", 800, 250)
    center()
    scale(50)

    center1 = Vector(-5.5, 0)
    center2 = Vector(0, 0)
    center3 = Vector(5.5, 0)

    lpoints = [center1 + p for p in [E, N, W, S]]
    mpoints = [center2 + 2 * p for p in [E, N, W, S]]
    rpoints = [center3 + 2 * p for p in [E, N, W, S]]

    out = [center1 + 2 * p for p in [E, N, W, S]]

    fork_all(out, 0.3)
    fork_all(mpoints, 0.3)
    fork_all(rpoints, 0.3)

    color = (0, 0, 1)
    for p, q in zip(out, lpoints):
        line(p, q, color)

    line(mpoints[0], mpoints[1], color)
    line(mpoints[2], mpoints[3], color)
    line(rpoints[1], rpoints[2], color)
    line(rpoints[3], rpoints[0], color)
    setarrowdims(0.06, 0.2)
    arrow_size = Vector(0.3, 0)
    arrow_pos = (center1 + center2) / 2
    newpath()
    arrow(arrow_pos-arrow_size, arrow_pos+arrow_size)
    stroke()

    add_pos = (center2 + center3) / 2
    add_x = Vector(0.2, 0)
    add_y = Vector(0, 0.2)
    scalelinewidth(4)
    line(add_pos-add_x, add_pos+add_x)
    line(add_pos-add_y, add_pos+add_y)
    scalelinewidth(1.0/4)

    gsave()
    setdash([4, 4], 0)
    path(lpoints)
    line(mpoints[1], mpoints[2])
    line(mpoints[3], mpoints[0])
    line(rpoints[1], rpoints[0])
    line(rpoints[3], rpoints[2])

    grestore()

    fontscale = 1.5
    pos = out[0] + (-0.2, 0.2)
    text("$A$", pos, fontscale)

    pos = out[1] + (-0.4, -0.3)
    text("$B$", pos, fontscale)

    pos = out[2] + (-0.1, -0.4)
    text("$C$", pos, fontscale)

    pos = out[3] + (0.1, 0.1)
    text("$D$", pos, fontscale)

    pos = mpoints[0] + (-0.1, 0.3)
    text("$A$", pos, fontscale)

    pos = mpoints[1] + (-0.5, -0.15)
    text("$B$", pos, fontscale)

    pos = mpoints[2] + (-0.15, -0.5)
    text("$C$", pos, fontscale)

    pos = mpoints[3] + (0.2, -0.1)
    text("$D$", pos, fontscale)

    pos = center1 + Vector(cos(pi/4), sin(pi/4)) * .8
    text("$x$", pos, fontscale)

    pos = center1 + Vector(cos(3*pi/4), sin(3*pi/4)) - (0, 0.1)
    text("$y$", pos, fontscale)

    pos = center1 + Vector(cos(5*pi/4), sin(5*pi/4)) * 1.05
    text("$z$", pos, fontscale)

    pos = center1 + Vector(cos(-pi/4), sin(-pi/4)) * .8 - (0.05, 0.2)
    text("$w$", pos, fontscale)

    pos = center2 + Vector(cos(pi/4), sin(pi/4)) * 1.6 - (0.1, 0)
    text(r"$z/\Delta$", pos, fontscale)

    pos = center2 + 2 * Vector(cos(3*pi/4), sin(3*pi/4)) - (0.35, 0.25)
    text(r"$w/\Delta$", pos, fontscale)

    pos = center2 + 2 * Vector(cos(5*pi/4), sin(5*pi/4)) + (-0.35, 0.1)
    text(r"$x/\Delta$", pos, fontscale)

    pos = center2 + 2 * Vector(cos(-pi/4), sin(-pi/4)) * .8 - (0.1, 0.2)
    text(r"$y/\Delta$", pos, fontscale)

    pos = rpoints[0] + (-0.1, 0.3)
    text("$A$", pos, fontscale)

    pos = rpoints[1] + (-0.5, -0.15)
    text("$B$", pos, fontscale)

    pos = rpoints[2] + (-0.15, -0.5)
    text("$C$", pos, fontscale)

    pos = rpoints[3] + (0.2, -0.1)
    text("$D$", pos, fontscale)

    pos = center3 + Vector(cos(pi/4), sin(pi/4)) * 1.6 - (0.1, 0)
    text(r"$z/\Delta$", pos, fontscale)

    pos = center3 + 2 * Vector(cos(3*pi/4), sin(3*pi/4)) - (0.35, 0.25)
    text(r"$w/\Delta$", pos, fontscale)

    pos = center3 + 2 * Vector(cos(5*pi/4), sin(5*pi/4)) + (-0.35, 0.1)
    text(r"$x/\Delta$", pos, fontscale)

    pos = center3 + 2 * Vector(cos(-pi/4), sin(-pi/4)) * .8 - (0.1, 0.2)
    text(r"$y/\Delta$", pos, fontscale)

    dots(lpoints + mpoints + rpoints + out, 0.07)
    finish()


spidermove()
case1()
case2()
case3()
