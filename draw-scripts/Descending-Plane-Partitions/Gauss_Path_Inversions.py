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

moveto(1, 2)
lineto(2, 2)
lineto(2, 3)
lineto(1, 3)
lineto(1, 2)
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

x, y = 1, 2
newpath()
circle(x + 0.5, y + 0.5, crad)
fill(1, 0, 0)
stroke()

t0 = texinsert("$\\bf{{1}}$")
t0.translate(-t0.width/2, 0)
t0.scale(1.5)
for x1, x2, ht in [(0, 1, 5), (1, 2, 5),
                   (2, 3, 5), (3, 4, 3),
                   (4, 5, 3)]:
    if ((x1, x2) != (1, 2)):
        place(t0, x1 + 0.5, ht+0.2)

t1 = texinsert("$\\bf{{0}}$")
t1.translate(0, -t1.height/2)
t1.scale(1.5)
for y1, y2, x in [(5, 4, 3), (4, 3, 3),
                  (3, 2, 5), (2, 1, 5),
                  (1, 0, 5)]:
    if (y1, y2) != (3, 2):
        place(t1, x + 0.1, y2+0.5)
setcolor(1, 0, 0)
place(t0, 1.5, 5.2)
place(t1, 5.1, 2.5)
finish()
