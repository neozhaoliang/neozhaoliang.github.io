from piscript.PiModule import *
from math import *

init(300, 300)
scale(300/1.1)
translate(0.05, 0.05)
b = sqrt(3) / 2

newpath()
moveto(0, 0)
lineto(1, 0)
lineto(0.25, b / 2)
closepath()
fill(0.6)
stroke()

newpath()
moveto(1, 0)
lineto(1, 1)
lineto(1-b/2, 0.25)
closepath()
fill(0.6)
stroke()

newpath()
moveto(1, 1)
lineto(0, 1)
rlineto(0.75, -b/2)
closepath()
fill(0.6)
stroke()

newpath()
moveto(0, 1)
lineto(0, 0)
rlineto(b/2, 0.75)
closepath()
fill(0.6)
stroke()

finish()
