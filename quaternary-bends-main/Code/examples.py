from __future__ import division
from getForms import *
from inversive import *

# get plot of v and W and the corresponding form
def one_apollonian_example(v, W) :
    ax = plot_A(v, W)
    expr = get_form(v, W)
    return ax, expr

# print Mathematica command to full simplify expression with determinant
# condition
def print_simplify(expr) :
    str1 = 'FullSimplify['
    str2 = ', Assumptions->{Element[{a, b, c, d}, Integers], a*d - b*c == 1}]'
    print str1 + expr + str2

# for a bunch of v, W pairs, plot v and W and print out the
# corresponding form
def apollonian_examples() :
    # get v1 and reflection matrices
    v1, cocluster = Apollonian_example()
    Rs = get_reflections(cocluster)
    R2, R3, R4, R5 = Rs

    # simple example
    v = v1*R2
    W = R2*R2
    ax, expr = one_apollonian_example(v, W)
    print_simplify(expr)
    plt.show()

    # example where circle is tangent to stabilizer
    v = v1*R2*R3*R4*R5*R4*R3*R2
    W = R2*R3
    ax, expr = one_apollonian_example(v, W)
    print_simplify(expr)
    plt.show()

    # example where circle is NOT tangent to stabilizer
    v = v1*R2*R3*R4*R5*R4*R3*R2
    W = R2*R3*R4*R5
    ax, expr = one_apollonian_example(v, W)
    print_simplify(expr)
    plt.show()

if __name__ == '__main__' :
    apollonian_examples()
