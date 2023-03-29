from __future__ import division
from sympy import *

def diag_symmetric(A) :
    temp = A.diagonalize()[0]
    Q, R = temp.QRdecomposition()
    return Q

def main() :
    # Define matrices
    Q = Matrix([ [1, -1, -1, -1], [-1, 1, -1, -1],
                [-1, -1, 1, -1], [-1, -1, -1, 1] ])
    Qt = Matrix([ [0, 0, 0, Rational(1,2)], [0, 1, 0, 0],
                 [0, 0, 1, 0], [Rational(1,2), 0, 0, 0] ])

    # Diagonalize
    V = diag_symmetric(Q)
    Vt = diag_symmetric(Qt)

    # Multiply by diagonal
    D = Matrix([ [2, 0, 0, 0], [0, 2, 0, 0], [0, 0, sqrt(2), 0], [0, 0, 0, sqrt(2)] ])
    B = Vt*D*V.T
    # invB = simplify(B.inv())
    invB = Matrix([[-Rational(1, 4) - sqrt(2)/8, -sqrt(3)/6, -sqrt(6)/12, Rational(1, 4) + sqrt(2)/8],
            [-sqrt(2)/8 + Rational(1, 4), -sqrt(3)/6, -sqrt(6)/12, sqrt(2)/8 + Rational(1, 4)],
            [-sqrt(2)/8, sqrt(3)/3, -sqrt(6)/12, sqrt(2)/8],
            [-sqrt(2)/8, 0, sqrt(6)/4, sqrt(2)/8]])

    # Check answer
    # print(simplify(B.T*Qt*B))

    # Define rho_tilde
    a, b, c, d = symbols('a b c d')
    rho_tilde = Matrix([[a**2, 2*a*c, 0, -c**2],
                        [a*b, a*d + b*c, 0, -c*d],
                        [0, 0, a*d - b*c, 0],
                        [-b**2, -2*b*d, 0, d**2]])

    # rho is obtained by conjugating rho_tilde by B^{-1}
    rho = invB*rho_tilde*B

    # get <e4, rho(*, *, 2k, ell)v0>
    v0 = Matrix([ -10, 18, 23, 27 ])
    rho = rho.subs(c, 2*c)
    rho = rho.subs(b, (a*d - 1)/2/c)
    A = rho*v0
    B = A.subs( [(a, 1), (c, 1), (d, 1)] )
    print simplify(B[3])

if __name__ == '__main__' :
    main()
