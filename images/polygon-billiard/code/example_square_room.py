import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from billiard import create_square_room, Vec2, polygon

margin = 0.05


def reset(n):
    plt.gca().clear()
    plt.axis("off")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.xlim(-margin, n + margin)
    plt.ylim(-margin, n + margin)


def plot_plane(n, **kwargs):
    for i in range(n):
        for j in range(n):
            k = (i % 2, j % 2)
            if k == (0, 0):
                type = 0
            if k == (1, 0):
                type = 1
            if k == (0, 1):
                type = 3
            if k == (1, 1):
                type = 2
            polygon.plot_square(i, j, type, **kwargs)

    for i in range(n + 1):
        plt.plot([i, i], [0, n], "k-", lw=1)
        plt.plot([0, n], [i, i], "k-", lw=1)


n = 8
reset(n)
plot_plane(n, marker=True)
plt.savefig("square_lattice.svg", bbox_inches="tight")

n = 5
reset(n)
room = create_square_room()
assin = Vec2(0.1, 0.7)
target = Vec2(0.8, 0.35)
virtual_target = target + Vec2(4, 4)
virtal_guard = assin.midpoint(virtual_target)
_, real_guard = room.draw_trajectory(assin, virtual_target)
plot_plane(n, target=target)
assin.plot("ro", markersize=5, markeredgecolor="k")
virtal_guard.plot("o", color="gray", markersize=4, markeredgecolor="k", lw=0.5)
real_guard.plot("o", color="gray", markersize=4, markeredgecolor="k", lw=0.5)
plt.savefig("square_lattice_with_targets.svg", bbox_inches="tight")
