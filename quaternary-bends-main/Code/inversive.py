from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
from math import floor
from getForms import *
from sympy import *

# This file contains code for plotting inverive coordinates in the plane
# We write inversive coordinates as a vector in R^4
#           (b, bx, by, bhat)
# where b is the bend (reciprocal of the radius), (x, y) is the center of
# the circle (or a unit normal vector pointing to the interior in the case
# of a line), and bhat is the cobend (bend after inversion through unit circle)
#   NOTE: the sign of the bend gives orientation (positive points towards
# interior)

# plots the inversive coordinate vector v on the axis ax
def plot_inv(v, ax, color='k') :
    # if bend is 0, we have a line
    if v[0] == 0 :
        # if cobend is 0, line passes through origin
        if v[3] == 0 :

            # if by = 0, it's a vertical line
            if v[2] == 0 :
                x_vals = np.array([0, 0])
                y_vals = np.array(ax.get_ylim())
                ax.plot(x_vals, y_vals, color=color)

            # otherwise, use normal vector to compute slope
            else :
                slope = -v[1]/v[2]
                x_vals = np.array(ax.get_xlim())
                y_vals = slope*x_vals
                ax.plot(x_vals, y_vals, color=color)

        # if cobend is nonzero, line doesn't pass through origin
        else :
            # the point bhat*(bx, by)/2 is always on the line
            x = v[3]*v[1]/2
            y = v[3]*v[2]/2

            # if by = 0, it's a vertical line
            if y == 0 :
                x_vals = np.array([x, x])
                y_vals = np.array(ax.get_ylim())
                ax.plot(x_vals, y_vals, color=color)

            # otherwise, use normal vector to compute slope
            else :
                slope = -v[1]/v[2]
                intercept = -slope*x + y
                x_vals = np.array(ax.get_xlim())
                y_vals = slope*x_vals + intercept
                ax.plot(x_vals, y_vals, color=color)

    # if bend is nonzero, we have a circle
    else :
        x_center = v[1]/v[0]
        y_center = v[2]/v[0]
        radius = 1/abs(v[0])

        circle = plt.Circle((x_center, y_center), radius,
                            fill=False, color=color)
        ax.add_artist(circle)

# plot one realization of the Apollonian cluster/cocluster
def plot_Apollonian(lbl=False) :
    # here are the inversive coordinates
    v1, cocluster = Apollonian_example()

    # set up the figure
    fig = plt.figure()
    ax = plt.axes( xlim=(-3, 3), ylim=(-3, 3), aspect='equal')

    # put the cluster in blue
    plot_inv(v1, ax, 'b')

    # put cocluster in red
    for v in cocluster :
        plot_inv(v, ax, 'r')

    # label circles
    if lbl :
        plt.text(2.5, -0.15, '$v_1$')
        plt.text(2.5, 1.1, '$v_2$')
        plt.text(-1.6, 1.5, '$v_3$')
        plt.text(1.1, 2.5, '$v_4$')
        plt.text(-0.2, 2.5, '$v_5$')

    return ax

# plot circles in Apollonian packing out to width wid
#   - including n^th circle to right of center circle hits x = 2*n + 1
def plot_A_width(wid) :
    # set up the figure
    fig = plt.figure()
    ax = plt.axes( xlim=(-wid, wid), ylim=(-1, 3), aspect='equal')

    # get cluster/cocluster
    v1, cocluster = Apollonian_example()

    # get reflection matrices
    Rs = get_reflections(cocluster)
    R2, R3, R4, R5 = Rs

    # plot the bounding lines and first circle
    plot_inv(v1, ax, 'b')
    v = v1*R2
    plot_inv(v, ax, 'b')
    v = v*R3
    plot_inv(v, ax, 'b')

    # how many circles to the right?
    n = floor(wid/2)
    for i in range(n) :
        v = v*R4
        plot_inv(v, ax, 'b')
        v = v*R5
        plot_inv(v, ax, 'b')

    return ax

# plot some circles in the Apollonian packing in blue along with
#   - v in red
#   - v_1W in yellow
def plot_A(v, W) :
    # get v1 and w = v1W
    v1, _ = Apollonian_example()
    w = v1*W

    # What's the max width we'll need?
    wid_v = 0
    if v[0] != 0 :
        wid_v = v[1]/v[0] + 1
    wid_w = 0
    if w[0] != 0 :
        wid_w = w[1]/w[0] + 1
    wid = max(wid_v, wid_w, 3)

    # plot base Apollonian circles
    ax = plot_A_width(wid)

    # plot v and w
    plot_inv(v, ax, 'r')
    plot_inv(w, ax, 'y')

    return ax

# plot Kontorovich's non-congruence example
def plot_nonc() :
    cluster, cocluster = K_N_example()

    # set up the figure
    fig = plt.figure()
    ax = plt.axes( xlim=(-4.5, -1), ylim=(-1.5, 1.5), aspect='equal')

    # plot cluster in blue
    for v in cluster :
        plot_inv(v, ax, 'b')

    # plot cocluster in red
    for v in cocluster :
        plot_inv(v, ax, 'r')

    plt.show()

if __name__ == '__main__' :
    plot_nonc()
