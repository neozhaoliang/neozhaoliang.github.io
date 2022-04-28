import matplotlib.pyplot as plt
import numpy as np


def vec(*args):
    return np.array(args)


alpha_vee = vec(2, 0)
beta_vee = -alpha_vee

alpha = (1, 0)
beta = (-1, 1)


def s(v):
    v = np.asarray(v)
    return v - np.dot(alpha, v) * alpha_vee


def t(v):
    v = np.asarray(v)
    return v - np.dot(beta, v) * beta_vee


def draw_mirror(ax, n, *args, **kwargs):
    x, y = n
    L = 10
    vx = -y
    vy = x
    if x < 0:
        vx, vy = -vx, -vy
    ax.plot([0, L*vx], [0, L*vy], *args, **kwargs)


fig = plt.figure(figsize=(6, 4), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis([-4, 4, -0.5, 2])

draw_mirror(ax, alpha, "r-")
draw_mirror(ax, beta, "b-")
ax.plot([-10, 10], [1, 1], "k-")
fig.savefig("test.png")
