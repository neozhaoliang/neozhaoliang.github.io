from piscript.PiModule import *
import numpy as np


def draw_star():
    r = 0.08
    init("div.eps", 300, 300)
    center()
    scale(130)

    newpath()
    circle(0, 0, r)
    fill(1, 0, 0)
    stroke()

    setarrowdims(0.02, 0.1)
    n = 5
    for i in range(n):
        z = np.exp(1j * 2 * np.pi / n * i)
        x = z.real
        y = z.imag
        newpath()
        circle(x, y, r)
        fill(0, 1, 0)
        stroke()

        newpath()
        arrow([0.15*x, 0.15*y], [x*0.85, y*0.85])
        fill(0)
        stroke()
    finish()


def draw_cycle():
    init("cycle.eps", 300, 300)
    center()
    scale(130)
    setarrowdims(0.02, 0.1)
    r = 0.08
    n = 5
    mu = np.exp(np.pi / n / 2 * 1j)
    for i in range(n):
        z = np.exp(1j * 2 * np.pi / n * i) * mu
        x = z.real
        y = z.imag
        newpath()
        circle(x, y, r)
        fill(1, 0.5, 0)
        stroke()


    for i in range(n):
        newpath()
        z = np.exp(1j * 2 * np.pi / n * i) * mu
        x1 = z.real
        y1 = z.imag
        l = (i + 1) % n
        w = np.exp(1j * 2 * np.pi / n * l) * mu
        v = w - z
        arrow([x1 + 0.15*v.real, y1 +0.15*v.imag], [x1 + v.real*0.85, y1+v.imag*0.85])
        fill(0)
        stroke()

    newpath()
    arcarrow([0, 0], 0.4, np.pi/6, -np.pi/6)
    fill(0, 1, 0)
    stroke()
    finish()


draw_star()
draw_cycle()
