import numpy as np
import matplotlib.pyplot as plt

from billiard import Vec2, polygon, create_hexagon_room, utils

room = create_hexagon_room()
sq3 = np.sqrt(3)

plt.figure(figsize=(10, 10))
plt.clf()
plt.xlim(-2.5, 3.5)
plt.ylim(-2.2, 3.8)
plt.axis("off")
plt.gca().set_aspect("equal", adjustable="box")

n = 9
for i in range(-n, n):
    for j in range(-n, n):
        k = (i - j) % 3
        x, y = utils.triangle_to_cartesian(i, j)
        if k == 0:
            polygon.plot_hexagon(x, y)


assin = Vec2(0.1, 1.4)
real_guards = []
for i in range(-n, n):
    for j in range(-n, n):
        if (i - j) % 3 != 0:
            continue
        virtual_target = Vec2(0.55, 0.24) + utils.triangle_to_cartesian(i, j)
        virtal_guard = assin.midpoint(virtual_target)
        real_target, real_guard = room.draw_trajectory(assin, virtual_target, lw=0.3)
        virtual_target.plot("yo", markeredgecolor="k", markersize=10)
        virtal_guard.plot("o", color="gray", markersize=6, markeredgecolor="k", lw=0.5)
        real_guards.append(real_guard)

for real_guard in real_guards:
    real_guard.plot("co", markersize=6, markeredgecolor="k", lw=0.5)

assin.plot("ro", markersize=10, markeredgecolor="k")
plt.savefig("24_guards_each_lattice.svg", bbox_inches="tight")
