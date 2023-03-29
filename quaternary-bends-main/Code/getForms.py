from __future__ import division
from sympy import *
import numpy as np
from scipy.optimize import least_squares

# returns I + 2Qv^Tv
def get_R(v, Q) :
    n = len(v)
    return eye(n) + 2*Q*v.T*v

# given cocluster as list of inversive coordinates, returns list of reflections
def get_reflections(cocluster) :
    Q = Matrix([ [0, 0, 0, Rational(1,2)],
                 [0, -1, 0, 0],
                 [0, 0, -1, 0],
                 [Rational(1,2), 0, 0, 0] ])

    Rs = []

    for v in cocluster :
        Rs.append(get_R(v, Q))

    return Rs

# computes spin representation of
# [ [a + alpha*i, b + beta*i]
#   [c + gamma*i, d + delta*i] ]
def get_spin(a, b, c, d, alpha, beta, gamma, delta) :
    rho = Matrix([ [a**2 + alpha**2, a*b + alpha*beta, a*beta - b*alpha, b**2 + beta**2],
                   [2*(a*c + alpha*gamma), a*d + b*c + alpha*delta + beta*gamma, a*delta - b*gamma + c*beta - d*alpha, 2*(b*d + beta*delta)],
                   [2*(-a*gamma + c*alpha), -a*delta - b*gamma + c*beta + d*alpha, a*d - b*c + alpha*delta - beta*gamma, 2*(-b*delta + d*beta)],
                   [c**2 + gamma**2, c*d + delta*gamma, c*delta - d*gamma, d**2 + delta**2] ])
    return rho

# attempts to find the matrix g such that rho(g) = R
def find_inverse(R) :
    a, alpha, b, beta, c, gamma, d, delta = symbols('a alpha b beta c gamma d delta', real=True)
    rho = get_spin(a, b, c, d, alpha, beta, gamma, delta)

    eqns = [(a + alpha*1j)*(d + delta*1j) - (b + beta*1j)*(c + gamma*1j) - 1]
    #eqns = []
    for i in range(4) :
        for j in range(4) :
            eqns.append(rho[i, j] - R[i, j])

    #soln = nsolve(eqns, [a, alpha, b, beta, c, gamma, d, delta], [1, 0, 0, 0, 0, 0, 1, 0], verify=False)
    soln = solve(eqns)
    if len(soln) == 0 :
        print 'No solution found'
        return None

    return Matrix([ [soln[0][a] + soln[0][alpha]*1j, soln[0][b] + soln[0][beta]*1j],
                    [soln[0][c] + soln[0][gamma]*1j, soln[0][d] + soln[0][delta]*1j]])

# returns BAB^{-1}
def conjugate(A, B) :
    return B*A*B.inv()

# gets quadratic form of bends from Stab(v_1W) acting on v
def get_form(v, W) :
    # start with arbitrary matrix in SL(2, Z)
    a, b, c, d = symbols('a b c d')
    M = Matrix([ [a, b],
                 [c, d] ])

    # conjugate back to pre-image of <R5R3, R5R4>
    B = Matrix([ [sqrt(2), 0],
                 [0, 1/sqrt(2)] ])
    A = conjugate(M, B)

    # now apply rho (the spin representation) and conjugate by W
    rho = get_spin(A[0, 0], A[0, 1], A[1, 0], A[1, 1], 0, 0, 0, 0)
    rho_conj = conjugate(rho, W.inv())

    # finally, hit our choice of v with rho, then grab the bend
    inversive = v*rho_conj
    bend = inversive[0]

    # replace ** with ^ for use in Mathematica
    bend = str(bend).replace("**", "^")

    return bend

def print_matrix(M) :
    if M == None :
        return

    n = M.shape[0]
    for i in range(n) :
        print(M[i, :])

def Apollonian_example() :
    cluster = Matrix([0, 0, -1, 0]).T
    cocluster = [[0, 0, 1, 2], [1/2, 0, 0, -2], [0, 1, 0, 2], [0, -1, 0, 0]]

    for i in range(len(cocluster)) :
        cocluster[i] = Matrix(cocluster[i]).T

    return cluster, cocluster

# See Kontorovich Mathematica file for this example
def K_N_example() :
    cluster = [[0, 1, 0, -3], [8, -13, 0, 21], [2, -4, -1, 8], [2, -4, 1, 8], [24, -43, 0, 77], [18, -28, -3, 44], [66, -116, -3, 204], [66, -116, 3, 204], [0, -1, 0, 7], [8, -27, 0, 91], [2, -6, -1, 18], [2, -6, 1, 18], [24, -77, 0, 247], [18, -62, -3, 214], [66, -214, -3, 694], [66, -214, 3, 694]]
    cocluster = [[0, 0, -1, 1], [0, 0, 1, 1], [4, -6, 1, 9], [2, -5, 0, 12], [6, -9, -2, 14], [12, -18, -1, 27], [10, -19, 0, 36], [14, -23, -2, 38], [4, -14, 1, 49], [6, -21, -2, 74], [26, -45, -2, 78], [26, -45, 2, 78], [10, -31, 0, 96], [42, -75, -2, 134], [42, -75, 2, 134], [12, -42, -1, 147], [48, -84, -1, 147], [48, -84, 1, 147], [14, -47, -2, 158], [26, -85, -2, 278], [26, -85, 2, 278], [42, -135, -2, 434], [42, -135, 2, 434], [48, -156, -1, 507], [48, -156, 1, 507]]

    for i in range(len(cluster)) :
        cluster[i] = Matrix(cluster[i]).T

    for i in range(len(cocluster)) :
        cocluster[i] = Matrix(cocluster[i]).T

    return cluster, cocluster

if __name__ == '__main__' :
    v1, cocluster = Apollonian_example()

    Rs = get_reflections(cocluster)
    R2, R3, R4, R5 = Rs

    expr = get_form(v1*R2*R3*R4*R5*R4*R3*R2, R2*R3)

    print(expr)
