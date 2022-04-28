from piscript.PiModule import *


pcolor = (0, 0.5, 1)
init("dpp-path-system.eps", 450, 450, "noclip")
scale(50)
translate(1, 1)
setarrowdims(0.08, 0.15)

gsave()
setdash([6, 6], 0)
for k in range(0, 8):
    moveto(k, 0)
    lineto(k, 7)
    stroke(0.8)

    moveto(0, k)
    lineto(7, k)
    stroke(0.8)
grestore()

newpath()
arrow([7, 0], [7.5, 0])
stroke()

newpath()
arrow([0, 7], [0, 7.5])
stroke()

ts = 2.0
t = texinsert("$x$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 7.5, -0.5)

t = texinsert("$y$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, -0.4, 7.5)

scalelinewidth(2.2)
newpath()
#moveto(0, 7)
#lineto(1, 7)
#lineto(1, 6)
moveto(1, 6)
lineto(3, 6)
lineto(3, 3)
lineto(4, 3)
lineto(4, 1)
lineto(5, 1)
lineto(5, 0)
stroke(*pcolor)

newpath()
moveto(0, 6)
lineto(0, 5)
lineto(1, 5)
lineto(1, 4)
lineto(2, 4)
lineto(2, 2)
lineto(3, 2)
lineto(3, 0)
lineto(4, 0)
stroke(*pcolor)

newpath()
moveto(0, 3)
lineto(1, 3)
lineto(1, 0)
stroke(*pcolor)

newpath()
moveto(0, 2)
lineto(0, 0)
stroke(*pcolor)

scalelinewidth(0.5)
crad = 0.1
for x, y in [#(0, 7),
        (1, 6),
        (5, 0), (0, 6), (4, 0), (0, 3), (1, 0), (0, 0), (0, 2)]:
    newpath()
    circle(x, y, crad)
    fill(1, 0.5, 0)
    stroke()


for x1, x2, y in [#(0, 1, 7),
        (1, 2, 6), (2, 3, 6),
        (3, 4, 3), (4, 5, 1), (0, 1, 5),
        (1, 2, 4), (2, 3, 2), (0, 1, 3)]:
    t = texinsert("${}$".format(y))
    t.translate(-t.width/2, 0)
    t.scale(ts)
    place(t, x1+0.5, y+0.2)

finish()
