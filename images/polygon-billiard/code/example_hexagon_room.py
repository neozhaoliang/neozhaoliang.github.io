import numpy as np
import matplotlib.pyplot as plt

from billiard import Vec2, polygon, create_hexagon_room, utils

room = create_hexagon_room()
sq3 = np.sqrt(3)

plt.clf()
plt.xlim(-4, 5)
plt.ylim(-4, 5)
plt.axis("off")
plt.gca().set_aspect("equal", adjustable="box")

n = 9
for i in range(-n, n):
    for j in range(-n, n):
        k = (i - j) % 3
        x, y = utils.triangle_to_cartesian(i, j)
        if k == 0:
            polygon.plot_hexagon(x, y, marker=True)


plt.savefig("hexagon_lattice.svg", bbox_inches="tight")
