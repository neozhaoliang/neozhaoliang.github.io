import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
from billiard import Vec2, polygon, Room, Marker
from billiard.transform import triangle_to_cartesian, get_affine_group_element

room = Room("hexagon")
sq3 = np.sqrt(3)


def reset(xmin=-0.5, xmax=3.0, ymin=-1.75, ymax=1.75):
    plt.clf()
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.axis("off")
    plt.gca().set_aspect("equal", adjustable="box")


def draw_arrow(p1, p2, shorten=0.9, shift=(0, 0), **kwargs):
    c = (1 - shorten) * 0.5
    start = p1 + c * (p2 - p1) + shift
    end = p2 - c * (p2 - p1) + shift
    plt.gca().add_patch(FancyArrowPatch(start, end, mutation_scale=10, **kwargs))


reset()
for i, j in [(0, 0), (2, -1), (1, -2)]:
    xy = triangle_to_cartesian(i, j)
    polygon.plot_hexagon(xy)

marker = Marker().scale(0.8).translate((0.5, 0.33))
p0 = marker.center()
marker.plot("r-", lw=1, label="0-th reflection")
marker.transform_by_group_element(get_affine_group_element(0, 0))
p1 = marker.center()
marker.plot("g-", lw=1, label="1-th reflection")
marker.transform_by_group_element(get_affine_group_element(1, 1))
p2 = marker.center()
draw_arrow(p0, p1, shorten=0.6, shift=(0.1, 0))
marker.plot("y-", lw=1, label="2-th reflection")
marker.transform_by_group_element(get_affine_group_element(2, 1))
p3 = marker.center()
draw_arrow(p1, p2, shorten=0.6, shift=(0, 0))
draw_arrow(p2, p3, shorten=0.6, shift=(0, 0))
marker.plot("b-", lw=1, label="3-th reflection")
plt.savefig("chirality.svg", bbox_inches="tight")

n = 10
reset(-0.5, 4.5, -1.5, 3.5)
for i in range(-4, n + 1):
    for j in range(-4, n + 1):
        if (i - j) % 3 == 0:
            xy = triangle_to_cartesian(i, j)
            polygon.plot_hexagon(xy)

style = "r-"
marker = Marker().scale(0.8).translate((0, 1.2))
marker.plot(style)
p0 = marker.center()
marker.transform_by_group_element(get_affine_group_element(2, 1))
marker.plot(style)
p1 = marker.center()
marker.transform_by_group_element(get_affine_group_element(1, 3))
marker.plot(style)
p2 = marker.center()
pts = [p0, p1, p2]
for i in range(len(pts) - 1):
    draw_arrow(pts[i], pts[i + 1], fc="y", ec="k", lw=0.5, shorten=0.8, shift=(0, 0))

draw_arrow(p0, p2, fc="none", ec="k", lw=0.8, shorten=0.9, linestyle="--")
style = "b-"
marker = Marker().scale(0.8).translate((0, 1.2))
q0 = marker.center()
marker.transform_by_group_element(get_affine_group_element(1, 2))
marker.plot(style)
q1 = marker.center()
marker.transform_by_group_element(get_affine_group_element(2, 2))
marker.plot(style)
q2 = marker.center()

pts = [q0, q1, q2]
for i in range(len(pts) - 1):
    draw_arrow(pts[i], pts[i + 1], fc="c", ec="k", lw=0.5, shorten=0.8, shift=(0, 0))
draw_arrow(q0, q2, fc="none", ec="k", lw=0.8, shorten=0.9, linestyle="--")

plt.savefig("chirality-2.svg", bbox_inches="tight")
