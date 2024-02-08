from piscript.PiModule import *
import numpy as np
from colorsys import hls_to_rgb

def caustics():

    init("caustics.eps", 400, 400)
    center()
    scale(180)
    newpath()
    circle(0, 0, 1)
    stroke(0)
    gsave()
    setarrowdims(0.02, 0.05)
    ylist = np.linspace(-1, 1, 20)
    y = 0.6
    theta = np.arcsin(y) / 2
    newpath()
    x = (1 - y * y)**0.5
    arrow((-1, 0), (x, y))
    fill(1, 1, 0)
    stroke()

    x1 = -cos(4*theta)
    y1 = -sin(4*theta)
    newpath()
    arrow((x, y), (x1, y1))
    fill(1, 1, 0)
    stroke()

    setdash([2, 2])
    newpath()
    arc(x, y, 0.15, np.pi+theta, np.pi + 2*theta)
    stroke()
    newpath()
    arc(x, y, 0.15, np.pi + 2*theta, np.pi + 3*theta)
    stroke()

    setdash([4, 4])
    newpath()
    moveto(x, y)
    lineto(0, 0)
    lineto(-1, 0)
    stroke(0)

    newpath()
    circle(0, 0, 0.01)
    fill(0)

    dir = Vector([-np.sin(2*theta), np.cos(2*theta)])
    start = Vector([x, y]) + dir * 0.5
    end = Vector([x, y]) - dir * 0.5
    newpath()
    moveto(start)
    lineto(end)
    stroke()
    grestore()

    gsave()
    scalelinewidth(3)
    newpath()
    arc(0, 0, 1, 2*theta, np.pi)
    stroke(0.8, 0, 0)
    newpath()
    arcn(0, 0, 1, 2*theta, 4*theta-np.pi)
    stroke(0, 0, 0.8)

    newpath()
    circle(-1, 0, 0.02)
    fill(0)

    grestore()
    newpath()
    arcnarrow(0, 0, 1.1, np.pi/5*4, np.pi*2/3)
    fill(0.8, 0, 0)
    stroke()

    newpath()
    arcnarrow(0, 0, 1.1, -np.pi/5, -np.pi/3)
    fill(0, 0, 0.8)
    stroke()

    t = texinsert("$A$")
    t.scale(1.5)
    t.translate(-t.width, -t.height)
    place(t, -1.05, -0.05)

    t = texinsert("$t$")
    t.scale(1.5)
    t.translate(-t.width, -t.height)
    place(t, 0, 0.1)

    flush()

caustics()
