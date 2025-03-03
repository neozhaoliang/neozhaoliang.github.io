import numpy as np
from piscript.PiModule import *


init(400, 400)
center()
scale(80)

ts = 1.2
h = 0.1
r = 0.08

for i in range(-1, 2):
    newpath()
    moveto(-2, i)
    lineto(2, i)
    closepath()
    stroke()

    newpath()
    moveto(i, -2)
    lineto(i, 2)
    closepath()
    stroke()

for x, y in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    t = texinsert(r"$1$")
    t.scale(ts)
    t.translate(0, t.height)
    place(t, x + h, y + h)

    newpath()
    circle(x, y, r)
    fill(1, 0.5, 0)
    stroke()

for x, y in [(1, 1), (-1, 1), (-1, -1), (1, -1)]:
    t = texinsert(r"$4/\pi$")
    t.scale(ts)
    t.translate(-t.width/2, t.height)
    place(t, x, y + h)

    newpath()
    circle(x, y, r)
    fill(0, 1, 0.5)
    stroke()

t = texinsert(r"$0$")
t.scale(ts)
t.translate(-t.width/2, t.height)
place(t, h, h)

newpath()
circle(0, 0, r)
fill(0)
stroke()

for x, y in [(2, 0), (0, 2), (-2, 0), (0, -2)]:
    t = texinsert(r"$4-8/\pi$")
    t.scale(ts)
    t.translate(-t.width/2, t.height)
    place(t, x, y + h)

    newpath()
    circle(x, y, r)
    fill(1, 0, 1)
    stroke()

finish()
