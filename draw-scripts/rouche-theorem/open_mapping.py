from piscript.PiModule import *
import numpy as np

init("test.eps", 200, 200)
center()
scale(45)
translate(0.25, -0.3)

def f(z):
    a = -0.5 + 0.5j
    return (z - a) / (1 - z * a.conjugate()) * (z - 1  - 1j)

N = 1000
pts = np.linspace(0, 2 * np.pi, N)
pts = np.exp(1j * pts)
pts = [f(z) for z in pts]
newpath()
moveto(pts[0].real, pts[0].imag)
for i in range(1, N):
    lineto(pts[i].real, pts[i].imag)
closepath()
stroke()

rad = 0.05

w0 = 0.1 + 1j
w1 = 0.8 + 1j
newpath()
circle(w0.real, w0.imag, rad)
fill(0)

newpath()
circle(w1.real, w1.imag, rad)
fill(0)

setdash([4, 4])
newpath()
circle(w0.real, w0.imag, abs(w0-w1))
stroke()



sc = 1.2

t1 = texinsert(r"$w_0$")
t1.scale(sc)
place(t1, w0.real - 0.3, w0.imag - 0.25)


t2 = texinsert(r"$w_1$")
t2.scale(sc)
place(t2, w1.real+0.1, w1.imag - 0.25)


t3 = texinsert(r"$f(\gamma)$")
t3.scale(sc)
place(t3, -2, 1)

flush()
