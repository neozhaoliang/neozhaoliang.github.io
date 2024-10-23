import matplotlib.pyplot as plt
import numpy as np


def f(z):
    a = -0.5 + 0.5j
    return (z - a) / (1 - z * a.conjugate()) * (z - 1 - 1j)


N = 1000
pts = np.linspace(0, 2 * np.pi, N)
pts = np.exp(1j * pts)
pts = [f(z) for z in pts]
xx = [p.real for p in pts]
yy = [p.imag for p in pts]

plt.plot(xx, yy, lw=0.75)

rad = 0.05
w0 = 0.1 + 1j
w1 = 0.8 + 1j
plt.Circle((w0.real, w0.imag), rad)
plt.Circle((w1.real, w1.imag), rad)
plt.Circle((w0.real, w0.imag), abs(w0 - w1))

plt.text(w0.real - 0.3, w0.imag - 0.25, r"$w_0$")
plt.text(w1.real + 0.1, w0.imag - 0.25, r"$w_1$")
plt.text(-2, 1, r"$f(\gamma)$")
plt.show()
