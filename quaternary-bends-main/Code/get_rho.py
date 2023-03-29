from numpy import dot, transpose, array
from numpy.linalg import inv, eigh

def main() :
    # Define matrices
    Q = array([ [1, -1, -1, -1], [-1, 1, -1, -1],
                [-1, -1, 1, -1], [-1, -1, -1, 1] ])
    Qt = array([ [0, 0, 0, 1/2], [0, 1, 0, 0],
                 [0, 0, 1, 0], [1/2, 0, 0, 0] ])

    # Diagonalize
    w, v = eigh(Q)
    wt, vt = eigh(Qt)
    print(v)
    print()
    print(transpose(v))
    print()
    print(Q)
    print()
    print(dot(inv(v), dot(Q, v)))
    print()
    print(dot(transpose(v), v))

if __name__ == '__main__' :
    main()
