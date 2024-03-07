import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

from billiard import create_hexagon_room, utils, Marker, Vec2, palette


def plot_hexagon(x, y, type, plot_conf, **kwargs):
    vertices = [
        Vec2(x, y),
        Vec2(x + 1, y),
        Vec2(x + 1.5, y + np.sqrt(3) / 2),
        Vec2(x + 1, y + np.sqrt(3)),
        Vec2(x, y + np.sqrt(3)),
        Vec2(x - 0.5, y + np.sqrt(3) / 2),
    ]
    hexagon = Polygon(
        vertices, closed=True, color=palette[type], ec="k", lw=1, **kwargs
    )
    plt.gca().add_patch(hexagon)
    if plot_conf.get("draw_marker", False):
        marker = Marker().scale(0.8)
        marker = Marker(
            [utils.transform_inside_hexagon_hex_lattice(p, type) for p in marker.points]
        )
        marker.translate(Vec2(x + 0.5, y + np.sqrt(3) / 2))
        marker.plot("k", lw=0.8)


n = 7
margin = 0.05


def reset(n):
    plt.gca().clear()
    plt.axis("off")
    plt.gca().set_aspect("equal", adjustable="box")
    plt.xlim(-margin, n + margin)
    plt.ylim(-margin, n + margin)


reset(n)
plot_conf = {"draw_marker": True}
for i in range(-1, n):
    for j in range(-1, n):
        x, y = i * 1.5, j * np.sqrt(3) * 1.5
        plot_hexagon(x, y, 0, plot_conf)

plt.savefig("hexagon_lattice.svg", bbox_inches="tight")
