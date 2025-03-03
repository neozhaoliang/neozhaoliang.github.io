from piscript.PiModule import *
from math import *

size = 400
G = (0.4, 1.0, 0.1)
n = 6
sqrt3 = 3**0.5
init("addrow.eps", size, size)
scale(size / (1.5 * (n - 1) + 4))
translate(n / 4 + .5, n / 4 + 1)

def hexagon(col=None):
    newpath()
    start = Vector(0, 1)
    moveto(start)
    for i in range(5):
        start.rotate(pi/3)
        lineto(start)
    closepath()
    if col:
        fill(*col)
    stroke()

for i in range(0, n):
    for k in range(n-i):
        gsave()
        translate((k+0.5*i) * sqrt3, 1.5*i )
        if i == 0:
            hexagon(G)
        else:
            hexagon()
        grestore()

finish()
