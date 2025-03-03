from piscript.PiModule import *


init(480, 200)
center()
scale(39)
translate(0, -0.4)

sw = 0.045
hw = 5 * sw
setarrowdims(sw, hw)

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


space1 = 1
space2 = 2
space3 = space1
ht = 0.4
nx = -6
sx = nx + 2 + space1
wx = sx + 2 + space2
ex = wx + 1 + space3

# ----------------
rectangle(nx, 0, nx + 1, 1, 1)
rectangle(nx + 1, 0, nx + 2, 1, gray)

newpath()
arrow((nx + 1, 1 + ht), (nx + 1, 2 + ht))
fill(1)
scalelinewidth(0.5)
stroke()


# ------------------
scalelinewidth(2)
rectangle(sx, 0, sx + 1, 1, gray)
rectangle(sx + 1, 0, sx + 2, 1, 1)

newpath()
arrow((sx + 1, -ht), (sx + 1, -1 - ht))
fill(1)
scalelinewidth(0.5)
stroke()

# -----------------------
scalelinewidth(2)
rectangle(wx, 0.5, wx + 1, 1.5, 1)
rectangle(wx, -0.5, wx + 1, 0.5, gray)
newpath()
arrow((wx - ht, 0.5), (wx - ht - 1, 0.5))
fill(1)
scalelinewidth(0.5)
stroke()
# ----------------------
scalelinewidth(2)
rectangle(ex, 0.5, ex + 1, 1.5, gray)
rectangle(ex, -0.5, ex + 1, 0.5, 1)
newpath()
arrow((ex + 1 + ht, 0.5), (ex + 2 + ht, 0.5))
fill(1)
scalelinewidth(0.5)
stroke()

finish()
