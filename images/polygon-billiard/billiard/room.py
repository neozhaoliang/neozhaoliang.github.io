import matplotlib.pyplot as plt

from .mirror import Mirror
from .vector import Vec2


class Room:

    def __init__(self, mirrors):
        self.mirrors = mirrors

    def get_bounce_trajectory(self, origin, target):
        trajectory = []
        while True:
            finish = True
            for mirror in self.mirrors:
                if not mirror.on_positive_side(target):
                    finish = False
                    q = mirror.intersect(origin, target)
                    if q is not None:
                        trajectory.append(q)
                        origin = q
                        target = mirror.reflect(target)
            if finish:
                break

        return trajectory, target

    def draw_trajectory(self, origin, target):
        trajectory, final_position = self.get_bounce_trajectory(origin, target)
        points = [origin] + trajectory + [final_position]
        xx, yy = zip(*points)
        plt.plot(xx, yy, "gray", "-", lw=0.5)
        guard = origin.midpoint(target)
        trajectory, real_guard = self.get_bounce_trajectory(origin, guard)
        for mirror in self.mirrors:
            if not mirror.on_positive_side(guard):
                q = mirror.intersect(origin, guard)
                if q is not None:
                    plt.gca().plot(*zip(q, target), "gray", linestyle="dashed", lw=0.5)
                    break
        return final_position, real_guard


def create_parallel_room(ymin=-0.5, ymax=11):
    m1 = Mirror(Vec2(-1, ymax), Vec2(-1, ymin))
    m2 = Mirror(Vec2(1, ymin), Vec2(1, ymax))
    return Room([m1, m2])


def create_square_room():
    m1 = Mirror(Vec2(0, 0), Vec2(1, 0))
    m2 = Mirror(Vec2(1, 0), Vec2(1, 1))
    m3 = Mirror(Vec2(1, 1), Vec2(0, 1))
    m4 = Mirror(Vec2(0, 1), Vec2(0, 0))
    return Room([m1, m2, m3, m4])


def create_triangle_room():
    m1 = Mirror(Vec2(0, 0), Vec2(1, 0))
    m2 = Mirror(Vec2(1, 0), Vec2(0.5, 0.5 * 3**0.5))
    m3 = Mirror(Vec2(0.5, 0.5 * 3**0.5), Vec2(0, 0))
    return Room([m1, m2, m3])


def create_hexagon_room():
    m1 = Mirror(Vec2(0, 0), Vec2(1, 0))
    m2 = Mirror(Vec2(1, 0), Vec2(1.5, 0.5 * 3**0.5))
    m3 = Mirror(Vec2(1.5, 0.5 * 3**0.5), Vec2(1, 3**0.5))
    m4 = Mirror(Vec2(1, 3**0.5), Vec2(0, 3**0.5))
    m5 = Mirror(Vec2(0, 3**0.5), Vec2(-0.5, 0.5 * 3**0.5))
    m6 = Mirror(Vec2(-0.5, 0.5 * 3**0.5), Vec2(0, 0))
    return Room([m1, m2, m3, m4, m5, m6])
