import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

from billiard import Vec2, polygon, create_hexagon_room, utils

margin = 0.05
room = create_hexagon_room()
sq3 = np.sqrt(3)


def reset(n):
    plt.clf()
    plt.xlim(-2, 9)
    plt.ylim(-2, 9)
    plt.axis("off")
    plt.gca().set_aspect("equal", adjustable="box")


n = 6
reset(n)
for i in range(-n, n + 10):
    for j in range(-n, n + 10):
        k = (i - j) % 3
        x, y = utils.triangle_to_cartesian(i, j)
        if k == 0:
            polygon.plot_hexagon(x, y)

assin = Vec2(0.3, 0.35)
virtual_target = Vec2(0.55, 0.24) + utils.triangle_to_cartesian(1, 7)
virtal_guard = assin.midpoint(virtual_target)
real_target, real_guard = room.draw_trajectory(assin, virtual_target)
real_target.plot("yo", markeredgecolor="k", markersize=5)
virtual_target.plot("yo", markeredgecolor="k", markersize=5)

virtual_target2 = real_target + utils.triangle_to_cartesian(1, 7)
real_target2, real_guard2 = room.draw_trajectory(assin, virtual_target2)
real_target2.plot("co", markeredgecolor="k", markersize=5)
virtual_target2.plot("co", markeredgecolor="k", markersize=5)

assin.plot("ro", markersize=5, markeredgecolor="k")
virtal_guard.plot("o", color="gray", markersize=4, markeredgecolor="k", lw=0.5)
real_guard.plot("o", color="gray", markersize=4, markeredgecolor="k", lw=0.5)

plt.savefig("hhhhhhhh.svg", bbox_inches="tight")
