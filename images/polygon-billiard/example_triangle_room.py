import numpy as np
import matplotlib.pyplot as plt
from billiard import Vec2, create_triangle_room, utils, polygon

margin = 0.05
room = create_triangle_room()
sq3 = np.sqrt(3)


def plot_plane(n, **kwargs):
    for i in range(-3, n):
        for j in range(-1, n):
            x, y = utils.triangle_to_cartesian(i, j)
            k = (i - j) % 3
            if k == 0:
                type1, type2 = 0, 1
            elif k == 1:
                type1, type2 = 4, 3
            else:
                type1, type2 = 2, 5
            polygon.plot_triangle(x, y, type1, **kwargs)
            polygon.plot_triangle(x, y, type2, **kwargs)


def reset(n):
    plt.clf()
    plt.xlim(-margin, (n - 1) * sq3 / 2 + margin)
    plt.ylim(-margin, (n - 1) * sq3 / 2 + margin)
    plt.axis("off")
    plt.gca().set_aspect("equal", adjustable="box")


n = 7
reset(n)
plot_plane(n, marker=True)
plt.savefig("triangle_lattice.svg", bbox_inches="tight")


n = 6
reset(n)
assin = Vec2(0.3, 0.35)
target = Vec2(0.68, 0.24)
virtual_target = target + utils.triangle_to_cartesian(1, 4)
virtal_guard = assin.midpoint(virtual_target)
_, real_guard = room.draw_trajectory(assin, virtual_target)
plot_plane(n, target=target)

assin.plot("ro", markersize=5, markeredgecolor="k")
virtal_guard.plot("o", color="gray", markersize=4, markeredgecolor="k", lw=0.5)
real_guard.plot("o", color="gray", markersize=4, markeredgecolor="k", lw=0.5)
plt.savefig("triangle_lattice_with_targets.svg", bbox_inches="tight")
