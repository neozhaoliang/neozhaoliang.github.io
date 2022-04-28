from piscript.PiModule import *


init("macdonald-bijection.eps", 320, 220, "noclip")
scale(40)
translate(.6, .6)
setarrowdims(0.08, 0.15)

ts = 1

gsave()
setdash([6, 6], 0)
N = 6
M = 4
for k in range(0, N+1):
    moveto(k, 0)
    lineto(k, M)
    stroke(0.8)
for k in range(0, M+1):
    moveto(0, k)
    lineto(N, k)
    stroke(0.8)
grestore()

newpath()
arrow([6, 0], [6.5, 0])
stroke()

newpath()
arrow([0, 4], [0, 4.5])
stroke()

scalelinewidth(1.5)

newpath()
moveto(0, 0)
lineto(1, 0)
lineto(1, 1)
lineto(3, 1)
lineto(3, 2)
lineto(6, 2)
lineto(6, 4)
lineto(0, 4)
closepath()
stroke()

newpath()
moveto(1, 0)
lineto(1, 4)
stroke()

newpath()
moveto(2, 1)
lineto(2, 4)
stroke()


newpath()
moveto(3, 1)
lineto(3, 4)
stroke()


newpath()
moveto(4, 2)
lineto(4, 4)
stroke()


newpath()
moveto(5, 2)
lineto(5, 4)
stroke()

newpath()
moveto(6, 2)
lineto(6, 4)
stroke()


t = texinsert("$x$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 6, -0.3)

t = texinsert("$y$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, -0.3, 4)

t = texinsert("$O$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, -0.3, -0.3)

t = texinsert("$(r-k+1,\lambda_k)$")
t.translate(-t.width/2, 0)
t.scale(1)
place(t, 6+0.2, 4+0.2)

"""
t = texinsert("$\lambda=(\lambda_1,\lambda_2,\ldots,\lambda_6)=(7, 7, 6, 6, 3, 1)$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 4, 7)


t = texinsert(r"$\{\lambda_i+n-i\ |\ 1\leq i\leq 6\}=\{12, 11, 9, 8, 4, 1\}$")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 4, 6+0.5)
"""

ts = 1
k = -0.3
setcolor(0, 0.5, 1)
t = texinsert("0")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 0.5, k)

t = texinsert("2")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 1.5, k+1)

t = texinsert("3")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 2.5, k+1)

t = texinsert("5")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 3.5, k+2)

t = texinsert("6")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 4.5, k+2)

t = texinsert("7")
t.translate(-t.width/2, 0)
t.scale(ts)
place(t, 5.5, k+2)




setcolor(1, 0.5, 0)
j = 0.2
t = texinsert("1")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, j+1, 0.5)

t = texinsert("4")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, j+3, 1.5)

t = texinsert("8")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, j+6, 2.5)

t = texinsert("9")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, j+6, 3.5)


setcolor(0)
k = 0.3
t = texinsert("$\lambda_k$")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, 0.5, k)

t = texinsert("$\lambda_{k+1}$")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, 1.5, 1+k)

t = texinsert("$\lambda_{r}$")
t.translate(-t.width/2, -t.height/2)
t.scale(ts)
place(t, 5.5, 2+k)

rad = 0.08
"""
for x, y in [(1, 0), (3, 1), (6, 2), (6, 3)]:
    newpath()
    circle(x, y, rad)
    fill(1, 0.5, 0)
    stroke()
"""
for x, y in [(1, 0), (2, 1), (3, 1), (4, 2), (5, 2), (6, 2)]:
    newpath()
    circle(x, y, rad)
    fill(0, 0.5, 1)
    stroke()
finish()
