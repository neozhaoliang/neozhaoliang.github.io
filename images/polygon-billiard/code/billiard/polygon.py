import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Polygon

from .colors import palette
from .vector import Vec2
from .marker import Marker
from . import utils


def plot_square(x, y, type, **kwargs):
    square = Rectangle((x, y), 1, 1, color=palette[type])
    plt.gca().add_patch(square)
    if kwargs.get("marker", False):
        Marker().transform_by_group_element(utils.K4[type]).translate(
            Vec2(x + 0.5, y + 0.5)
        ).plot("k", lw=0.8)

    target = kwargs.get("target", None)
    if target is not None:
        target = utils.transform_inside_square(target, type) + Vec2(x, y)
        target.plot("o", color="none", markeredgecolor="k", markersize=5)


def plot_triangle(x, y, type, **kwargs):
    sq3 = 3**0.5
    if type % 2 == 0:
        vertices = [Vec2(x, y), Vec2(x + 1, y), Vec2(x + 0.5, y + sq3 / 2)]
    else:
        vertices = [Vec2(x, y), Vec2(x + 0.5, y + sq3 / 2), Vec2(x - 0.5, y + sq3 / 2)]

    tri = Polygon(vertices, closed=True, color=palette[type], ec="k", lw=1)
    plt.gca().add_patch(tri)
    if kwargs.get("marker", False):
        marker = Marker().scale(0.8).transform_by_group_element(utils.D3[type])
        if type % 2 == 0:
            marker.translate(Vec2(x + 0.5, y + 0.5 / sq3))
        else:
            marker.translate(Vec2(x, y + 1 / sq3))
        marker.plot("k", lw=0.8)

    target = kwargs.get("target", None)
    if target is not None:
        q = utils.transform_inside_triangle(target, type)
        q += Vec2(x, y)
        q.plot("o", color=palette[type], markeredgecolor="k", markersize=5)


def plot_hexagon(x, y, **kwargs):
    sq3 = 3**0.5
    vertices = [
        Vec2(x, y),
        Vec2(x + 1, y),
        Vec2(x + 1.5, y + sq3 / 2),
        Vec2(x + 1, y + sq3),
        Vec2(x, y + sq3),
        Vec2(x - 0.5, y + sq3 / 2),
    ]
    for i in range(6):
        tri = Polygon(
            [Vec2(x + 0.5, y + sq3 / 2), vertices[i], vertices[(i + 1) % 6]],
            closed=True,
            lw=0,
            color=palette[i],
        )
        plt.gca().add_patch(tri)
        if kwargs.get("marker", False):
            Marker().scale(0.8).transform_by_group_element(utils.D3[i]).translate(
                (Vec2(x + 0.5, y + sq3 / 2) + vertices[i] + vertices[(i + 1) % 6]) / 3
            ).plot("k", lw=0.8)

    hexagon = Polygon(vertices, closed=True, color="none", ec="k", lw=1)
    plt.gca().add_patch(hexagon)
