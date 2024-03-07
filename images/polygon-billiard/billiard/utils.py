import numpy as np
from .vector import Vec2


def triangle_to_cartesian(x, y):
    return Vec2(x + y / 2, y * 3**0.5 / 2)


def reflect_about_line(p, normal, offset=0):
    """
    Reflects a point p about a line defined by a normal vector and an offset.
    """
    return p - 2 * (np.dot(p, normal) - offset) * normal


def rotate_about_point(p, center=(0, 0), angle=0):
    angle = np.deg2rad(angle)
    c, s = np.cos(angle), np.sin(angle)
    x, y = Vec2(p) - center
    return Vec2(c * x - s * y, s * x + c * y) + center


def get_dihedral_group_elements(order, angle):
    n1 = Vec2(0, 1)
    theta = np.deg2rad(angle)
    n2 = Vec2(np.sin(theta), -np.cos(theta))
    s0 = lambda p: Vec2(p)
    s1 = lambda p: reflect_about_line(p, n1)
    s2 = lambda p: reflect_about_line(p, n2)
    s2s1 = lambda p: s2(s1(p))
    s1s2s1 = lambda p: s1(s2s1(p))
    s1s2 = lambda p: s1(s2(p))
    if order == 4:
        return [s0, s2, s2s1, s1]
    else:
        return [s0, s2, s2s1, s1s2s1, s1s2, s1]


K4 = get_dihedral_group_elements(4, 90)
D3 = get_dihedral_group_elements(6, 60)


def transform_inside_square(p, type):
    q = K4[type](p)
    if type == 0:
        return q
    elif type == 1:
        return q + Vec2(1, 0)
    elif type == 2:
        return q + Vec2(1, 1)
    else:
        return q + Vec2(0, 1)


def transform_inside_triangle(p, type):
    q = Vec2(p)
    q = D3[type](q)
    if type == 0 or type == 1:
        return q
    elif type == 2:
        return q + triangle_to_cartesian(1, 0)
    elif type == 3 or type == 4:
        return q + triangle_to_cartesian(0, 1)
    elif type == 5:
        return q + triangle_to_cartesian(-1, 1)


def get_affine_group_element(i, k):
    n1 = Vec2(0, 1)
    n2 = Vec2(3**0.5 / 2, 0.5)
    n3 = Vec2(3**0.5 / 2, -0.5)
    normal = [n1, n2, n3][i]
    offset = 3**0.5 * k / 2
    return lambda p: reflect_about_line(p, normal, offset)
