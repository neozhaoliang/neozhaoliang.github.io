import matplotlib.pyplot as plt
import matplotlib
import numpy as np

plt.rcParams.update({"text.usetex": True, "font.family": "Helvetica"})

plt.gcf().set_size_inches(3, 3)
plt.axis("off")
plt.gca().set_aspect("equal")


def f(z):
    a = -0.5 + 0.5j
    return (z - a) / (1 - z * a.conjugate()) * (z - 1 - 1j)


N = 1000
pts = np.linspace(0, 2 * np.pi, N)
pts = np.exp(1j * pts)
pts = [f(z) for z in pts]
xx = [p.real for p in pts]
yy = [p.imag for p in pts]

plt.plot(xx, yy, "k-", lw=0.8)

rad = 0.05
w0 = 0.1 + 1j
w1 = 0.8 + 1j
plt.plot(w0.real, w0.imag, "ko", markersize=3)
plt.plot(w1.real, w1.imag, "ko", markersize=3)
c = plt.Circle(
    (w0.real, w0.imag), radius=abs(w0 - w1), ls="--", fc="none", ec="k", lw=0.8
)
c.set_linestyle((0, (4, 4)))
plt.gca().add_patch(c)
fs = 16
plt.text(w0.real - 0.3, w0.imag - 0.3, r"$w_0$", fontdict={"fontsize": fs})
plt.text(w1.real + 0.05, w0.imag - 0.3, r"$w_1$", fontdict={"fontsize": fs})
plt.text(-2, 1, r"$f(\gamma)$", fontdict={"fontsize": fs})
plt.gcf().tight_layout()
plt.savefig("winding_number.svg", transparent=True, bbox_inches="tight")
