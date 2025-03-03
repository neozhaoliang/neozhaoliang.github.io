from piscript.PiModule import *


init(200, 200)
center()
scale(100)

gray = 0

def rectangle(x1, y1, x2, y2, gray):
    newpath()
    moveto(x1, y1)
    lineto(x2, y1)
    lineto(x2, y2)
    lineto(x1, y2)
    closepath()
    fill(gray)
    stroke()

rectangle(0, 0, 1, 1, 1)
rectangle(0, 0, -1, 1, gray)
rectangle(0, 0, 1, -1, gray)
rectangle(0, 0, -1, -1, 1)
finish()
