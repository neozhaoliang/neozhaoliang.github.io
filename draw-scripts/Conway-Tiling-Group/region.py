from piscript.PiModule import *
from math import *

size = 400
n = 7
sqrt3 = 3**0.5
init("bone.eps", size, size)
scale(size / (1.5 * (n - 1) + 4))
translate(n * sqrt3 / 4 - sqrt3, n * sqrt3 / 4 -1)

def hexagon():
    newpath()
    start = Vector(0, 1)
    moveto(start)
    for i in range(5):
        start.rotate(pi/3)
        lineto(start)
    closepath()
    stroke()

for i in range(0, n):
    for k in range(n-i):
        gsave()
        translate((k+0.5*i) * sqrt3, 1.5*i )
        hexagon()
        grestore()

finish()
