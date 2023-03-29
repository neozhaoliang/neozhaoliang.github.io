from __future__ import division
from sympy import *

# returns I + 2Qv^Tv
def get_R(v, Q) :
    n = len(v)
    return eye(n) + 2*Q*v.T*v

def get_rotations() :
    v1 = [0, 0, -1, 0]
    v2 = [0, 0, 1, 2]
    v3 = [Rational(1, 2), 0, 0, -2]
    v4 = [0, 1, 0, 2]
    v5 = [0, -1, 0, 0]
    V = Matrix([v1, v2, v3, v4, v5])
    Q = Matrix([ [0, 0, 0, Rational(1,2)],
                 [0, -1, 0, 0],
                 [0, 0, -1, 0],
                 [Rational(1,2), 0, 0, 0] ])
    #print(V*Q*V.T)
    #print()

    v1 = Matrix([v1])
    v2 = Matrix([v2])
    v3 = Matrix([v3])
    v4 = Matrix([v4])
    v5 = Matrix([v5])

    R2 = get_R(v2, Q)
    R3 = get_R(v3, Q)
    R4 = get_R(v4, Q)
    R5 = get_R(v5, Q)

    return R2, R3, R4, R5, [v1, v2, v3, v4, v5]

def test_V() :
    v1 = [0, 0, -1, 0]
    v2 = [0, 0, 1, 2]
    v3 = [Rational(1, 2), 0, 0, -2]
    v4 = [0, 1, 0, 2]
    v5 = [0, -1, 0, 0]
    V = Matrix([v1, v2, v3, v4, v5])
    Q = Matrix([ [0, 0, 0, Rational(1,2)],
                 [0, -1, 0, 0],
                 [0, 0, -1, 0],
                 [Rational(1,2), 0, 0, 0] ])
    #print(V*Q*V.T)
    #print()

    v1 = Matrix([v1])
    v2 = Matrix([v2])
    v3 = Matrix([v3])
    v4 = Matrix([v4])
    v5 = Matrix([v5])

    R2 = get_R(v2, Q)
    R3 = get_R(v3, Q)
    R4 = get_R(v4, Q)
    R5 = get_R(v5, Q)
    #print(v1*R3)
    #print(v1*R4)
    #print(v1*R5)
    #print()

    v = v1*R2*R3
    #print(v)
    #print()

    S = R5*R3
    T = R5*R4

    w = v*T*S*T*S
    #print(w)

    # compute spin representation
    x, y, z, w = symbols('x y z w', real=True)
    M = Matrix([ [x, y + 1j*z], [y - 1j*z, w] ])
    a, alpha, b, beta, c, gamma, d, delta = symbols('a alpha b beta c gamma d delta', real=True)
    g = Matrix([ [a + alpha*1j, b + beta*1j],
                 [c + gamma*1j, d + delta*1j]])
    print('M')
    print(M)
    print ''
    print('g')
    print(g)
    print ''

    f11, f12, f22 = symbols('f11 f12 f22')
    expr1 = solve([f11 - (g.H*M*g)[0, 0], g.det() - 1], f11)[f11]
    expr2 = solve([f12 - (g.H*M*g)[0, 1], g.det() - 1], f12)[f12]
    expr3 = solve([f22 - (g.H*M*g)[1, 1], g.det() - 1], f22)[f22]
    print('x_prime is [0, 0] entry of gMg^H')
    print('x: ' + str(simplify(expr1.coeff(x))))
    print('y: ' + str(simplify(expr1.coeff(y))))
    print('z: ' + str(simplify(expr1.coeff(z))))
    print('w: ' + str(simplify(expr1.coeff(w))))
    print ''
    print('y_prime + I*z_prime is real part [0, 1] entry of gMg^H')
    print('x: ' + str(simplify(expr2.coeff(x))))
    print('y: ' + str(simplify(expr2.coeff(y))))
    print('z: ' + str(simplify(expr2.coeff(z))))
    print('w: ' + str(simplify(expr2.coeff(w))))
    print ''
    print('w_prime is [1, 1] entry of gMg^H')
    print('x: ' + str(simplify(expr3.coeff(x))))
    print('y: ' + str(simplify(expr3.coeff(y))))
    print('z: ' + str(simplify(expr3.coeff(z))))
    print('w: ' + str(simplify(expr3.coeff(w))))

def get_spin(a, b, c, d, alpha, beta, gamma, delta) :
    rho = Matrix([ [a**2 + alpha**2, a*b + alpha*beta, a*beta - b*alpha, b**2 + beta**2],
                   [2*(a*c + alpha*gamma), a*d + b*c + alpha*delta + beta*gamma, a*delta - b*gamma + c*beta - d*alpha, 2*(b*d + beta*gamma)],
                   [2*(-a*gamma + c*alpha), -a*delta - b*gamma + c*beta + d*alpha, a*d - b*c + alpha*delta - beta*gamma, 2*(-b*delta + d*beta)],
                   [c**2 + gamma**2, c*d + delta*gamma, c*delta - d*gamma, d**2 + delta**2] ])
    return rho

# attempts to find the matrix g such that rho(g) = R
def find_inverse(R) :
    a, alpha, b, beta, c, gamma, d, delta = symbols('a alpha b beta c gamma d delta', real=True)
    rho = get_spin(a, b, c, d, alpha, beta, gamma, delta)

    eqns = [(a + alpha*1j)*(d + delta*1j) - (b + beta*1j)*(c + gamma*1j) - 1]
    for i in range(4) :
        for j in range(4) :
            eqns.append(rho[i, j] - R[i, j])

    soln = solve(eqns)
    if len(soln) == 0 :
        print 'No solution found'
        return None
    soln = soln[0]

    return Matrix([ [soln[a] + soln[alpha]*1j, soln[b] + soln[beta]*1j],
                    [soln[c] + soln[gamma]*1j, soln[d] + soln[delta]*1j]])

# returns BAB^{-1}
def conjugate(A, B) :
    return B*A*B.inv()

def get_form(v) :
    # start with arbitrary matrix in SL(2, Z)
    a, b, c, d = symbols('a b c d')
    M = Matrix([ [a, b],
                 [c, d] ])

    # conjugate back to pre-image of <R5R3, R5R4>
    B = Matrix([ [sqrt(2), 0],
                 [0, 1/sqrt(2)] ])
    A = conjugate(M, B)

    # now apply rho (the spin representation)
    rho = get_spin(A[0, 0], A[0, 1], A[1, 0], A[1, 1], 0, 0, 0, 0)

    # finally, hit our choice of v with rho
    inversive = v*rho
    return inversive

def print_matrix(M) :
    if M == None :
        return

    n = M.shape[0]
    for i in range(n) :
        print(M[i, :])

if __name__ == '__main__' :

    R2, R3, R4, R5, Vs = get_rotations()

    print get_form(Vs[0]*R2)
    print get_form(Vs[0]*R2*R3)
    print get_form(Vs[0]*R2*R3*R4*R5*R4*R5*R3*R2)

    #v = Vs[0]*R2
    #a, b, x, y = symbols('a b x y')
    #rho = get_spin(a, 0, b, 0, 2*x, 0, y, 0)

    #print v*rho
    #r = get_spin(0, -1/2, 2, 0, 0, 0, 0, 0)
    #print_matrix(r)
