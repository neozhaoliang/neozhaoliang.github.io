import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from billiard import Vec2, polygon, create_hexagon_room, utils, Marker

room = create_hexagon_room()
sq3 = np.sqrt(3)


def reset():
    plt.clf()
    plt.xlim(-1.5, 3.5)
    plt.ylim(-2.5, 2.5)
    plt.axis("off")
    plt.gca().set_aspect("equal", adjustable="box")

    n = 5
    for i in range(-n, n):
        for j in range(-n, n):
            k = (i - j) % 3
            x, y = utils.triangle_to_cartesian(i, j)
            if k == 0:
                polygon.plot_hexagon(x, y)


def draw_arrow(p1, p2, shorten=0.9, shift=(0, 0)):
    c = (1 - shorten) * 0.5
    start = p1 + c * (p2 - p1) + shift
    end = p2 - c * (p2 - p1) + shift
    plt.gca().add_patch(FancyArrowPatch(start, end, mutation_scale=10))


reset()
marker = Marker().scale(0.8).translate((0.5, 0.33))
p0 = marker.center()
marker.plot("r-", lw=1, label="0-th reflection")
marker.transform_by_group_element(utils.get_affine_group_element(0, 0))
p1 = marker.center()
marker.plot("g-", lw=1, label="1-th reflection")
marker.transform_by_group_element(utils.get_affine_group_element(1, 1))
p2 = marker.center()
draw_arrow(p0, p1, shorten=0.6, shift=(0.1, 0))
marker.plot("y-", lw=1, label="2-th reflection")
marker.transform_by_group_element(utils.get_affine_group_element(2, 1))
p3 = marker.center()
draw_arrow(p1, p2, shorten=0.6, shift=(0, 0))
draw_arrow(p2, p3, shorten=0.6, shift=(0, 0))
marker.plot("b-", lw=1, label="3-th reflection")
plt.savefig("chirality.svg", bbox_inches="tight")

reset()
marker = Marker().scale(0.8).translate((0.5, 0.33))
marker.plot("r-", lw=1, label="0-th reflection")
p0 = marker.center()
marker.transform_by_group_element(utils.get_affine_group_element(0, 0))
marker.plot("g-", lw=1, label="1-th reflection")
p1 = marker.center()
marker.transform_by_group_element(utils.get_affine_group_element(1, 1))
marker.plot("y-", lw=1, label="2-th reflection")
p2 = marker.center()
marker.transform_by_group_element(utils.get_affine_group_element(0, 1))
marker.plot("b-", lw=1, label="3-th reflection")
p3 = marker.center()
marker.transform_by_group_element(utils.get_affine_group_element(1, 2))
marker.plot("c-", lw=1, label="4-th reflection")
p4 = marker.center()
draw_arrow(p0, p1, shorten=0.6, shift=(0.1, 0))
draw_arrow(p1, p2, shorten=0.6, shift=(0, 0))
draw_arrow(p2, p3, shorten=0.6, shift=(0, 0))
draw_arrow(p3, p4, shorten=0.6, shift=(0, 0))

plt.savefig("chirality-2.svg", bbox_inches="tight")
