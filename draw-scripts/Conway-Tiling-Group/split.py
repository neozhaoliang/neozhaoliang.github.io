from piscript.PiModule import *
from math import *

init("split.eps", 150, 150)
scale(150/1.2)
translate(0.1, 0.1)
newpath()
moveto(0, 0)
lineto(1, 0)
lineto(1, 1)
lineto(0, 1)
closepath()
stroke()

newpath()
moveto(0.5, 0)
lineto(0.5, 1)
stroke()

t = texinsert("$R_1$")
t.translate(-t.width/2, -t.height/4)
t.scale(1.5)
place(t, 0.25, 0.5)

t = texinsert("$R_2$")
t.translate(-t.width/2, -t.height/4)
t.scale(1.5)
place(t, 0.75, 0.5)


col = (0, 0.2, 0.7)
setarrowdims(0.02, 0.05)

x = 0.1
y = 0.3

for stard, end in [
    [(x, 0), (0.5 - x, 0)],
    [(0.45, y), (0.45, 1 - y)],
    [(0.5 - x, 1), (x, 1)],
    [(0, 1 - y), (0, y)],
    ]:
    newpath()
    arrow(stard, end)
    fill(*col)

for stard, end in [
    [(x + 0.5, 0), (1 - x, 0)],
    [(0.55, 1-y), (0.55, y)],
    [(1 - x, 1), (x + 0.5, 1)],
    [(1, y), (1, 1-y)],
    ]:
    newpath()
    arrow(stard, end)
    fill(0.8, 0, 0.2)


finish()
