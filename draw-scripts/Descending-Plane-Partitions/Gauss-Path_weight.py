from piscript.PiModule import *


init("dpp-path-system.eps", 350, 350, "noclip")
scale(50)
translate(0.5, 0.5)
setarrowdims(0.08, 0.15)

gsave()
setdash([6, 6], 0)
for k in range(0, 7):
    moveto(k, 0)
    lineto(k, 6)
    stroke(0.8)

    moveto(0, k)
    lineto(6, k)
    stroke(0.8)
grestore()

newpath()
arrow([6, 0], [6.5, 0])
stroke()

newpath()
arrow([0, 6], [0, 6.5])
stroke()

ts = 2.0
t = texinsert("$x$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 6, -0.4)

t = texinsert("$y$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, -0.3, 6)

scalelinewidth(2.2)
newpath()
moveto(0, 5)
lineto(3, 5)
lineto(3, 3)
lineto(5, 3)
lineto(5, 0)
stroke()

scalelinewidth(0.5)
crad = 0.1
for x in range(5):
    for y in range(5):
        if not (x >= 3 and y >= 3):
            newpath()
            circle(x + 0.5, y + 0.5, crad * 2/ 3)
            fill(1)
            stroke()

t = texinsert("$B$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 5, -0.4)


t = texinsert("$A$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, -0.3, 5)

t = texinsert("$O$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, -0.3, -0.3)
finish()
