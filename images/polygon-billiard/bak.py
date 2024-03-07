import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.patches import Polygon
from matplotlib.transforms import Affine2D, blended_transform_factory

plt.rcParams["font.size"] = 16

lw = 0.025

colors = [
    (251.0 / 255, 210.0 / 255, 1.0),
    (179 / 255, 179 / 255, 1.0),
    (162 / 255, 1.0, 240 / 255),
    (1, 224 / 255, 177 / 255),
    (234 / 255, 1, 240 / 255),
    (236 / 255, 194 / 255, 179 / 255),
]


def rotate_marker(p, theta):
    q = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]])
    return [np.dot(q, z) for z in p]


def reflect_marker(pts, normal):
    def reflect(xy, normal):
        xy = np.array(xy)
        n = np.array(normal)
        d = np.dot(xy, n)
        return xy - 2 * d * n

    return [reflect(xy, normal) for xy in pts]


def plot_hexagon(i, j, **kwargs):
    x = i + j / 2
    y = j * np.sqrt(3) / 2
    vertices = [
        [x, y],
        [x + 1, y],
        [x + 1.5, y + np.sqrt(3) / 2],
        [x + 1, y + np.sqrt(3)],
        [x, y + np.sqrt(3)],
        [x - 0.5, y + np.sqrt(3) / 2],
    ]
    hex = Polygon(vertices, closed=True, color="none", ec="k", lw=1, **kwargs)
    plt.gca().add_patch(hex)


def plot_triangle(i, j, type, **kwargs):
    x = i + j / 2
    y = j * np.sqrt(3) / 2
    if type % 2 == 0:
        vertices = [[x, y], [x + 1, y], [x + 0.5, y + np.sqrt(3) / 2]]
    else:
        vertices = [
            [x, y],
            [x + 0.5, y + np.sqrt(3) / 2],
            [x - 0.5, y + np.sqrt(3) / 2],
        ]
    tri = Polygon(vertices, closed=True, color=colors[type], **kwargs)
    plt.gca().add_patch(tri)
    s = 0.08
    p = [[-s, -s], [-s, s], [s, s]]
    if type == 1:
        p = reflect_marker(p, [np.sqrt(3) / 2, 0.5])
    elif type == 2:
        p = rotate_marker(p, 2 * np.pi / 3)
    elif type == 3:
        p = reflect_marker(p, [0, 1])
    elif type == 4:
        p = rotate_marker(p, -2 * np.pi / 3)
    elif type == 5:
        p = reflect_marker(p, [np.sqrt(3) / 2, -0.5])

    if type % 2 == 0:
        p = [(a + x + 0.5, b + y + 0.5 / np.sqrt(3)) for a, b in p]
    else:
        p = [(a + x, b + y + 1 / np.sqrt(3)) for a, b in p]
    xx, yy = zip(*p)
    plt.plot(xx, yy, "k", lw=0.8)


m = 3
n = m + 5
for i in range(-n, n):
    for j in range(-n, n):
        type = (i - j) % 3
        if type == 0:
            plot_triangle(i, j, 0)
            plot_triangle(i, j, 5)
        elif type == 1:
            plot_triangle(i, j, 1)
            plot_triangle(i, j, 4)
        elif type == 2:
            plot_triangle(i, j, 2)
            plot_triangle(i, j, 3)


for i in range(-n, n):
    for j in range(-n, n):
        if (i - j) % 3 == 0:
            plot_hexagon(i, j)


def plot_line(normal, offset, len=20):
    p = np.array(normal) * offset
    dir = np.array([normal[1], -normal[0]])
    start = p - dir * len
    end = p + dir * len
    plt.gca().plot([start[0], end[0]], [start[1], end[1]], "k", lw=1)


d = 0.05
plt.xlim(-m - 1 - d, m + 1 + d)
plt.ylim(-m - 1 - d, m + 1 + d)
plt.axis("off")

plt.gca().set_aspect("equal", adjustable="box")
plt.savefig("hexagon_lattices.svg", bbox_inches="tight")
