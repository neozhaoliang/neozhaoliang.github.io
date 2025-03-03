from piscript.PiModule import *
from aztec import *


def rectangle(x1, y1, x2, y2, fc, ec=None):
    newpath()
    moveto(x1, y1)
    lineto(x2, y1)
    lineto(x2, y2)
    lineto(x1, y2)
    closepath()
    fill(*fc)
    if ec is not None:
        stroke(*ec)


def render(az, size, filename, chess_board=False):
    if chess_board:
        board = AztecDiamond(az.order + 1)
        extent = az.order + 1
    else:
        board = az
        extent = az.order
        
    init(filename, size, size)
    center()
    scale(size / (2.0 * extent) - 0.2)
    

    margin = 0
    for i, j in board.cells:
        if not board.is_black(i, j):
            rectangle(i, j, i+1, j+1, (0.6,) * 3, (0,) * 3)
        else:
            rectangle(i+margin, j+margin, i+1-margin, j+1-margin, (1, 1, 1), (0, 0, 0))
        
    margin = 0.2
    for i, j in az.cells:
        if (az.is_black(i, j) and az.tile[(i, j)] is not None):
            if az.tile[(i, j)] == 'n':
                rectangle(i-1+margin, j+margin , i+1-margin, j+1-margin, N_COLOR)

            if az.tile[(i, j)] == 's':
                rectangle(i+margin, j+margin, i+2-margin, j+1-margin, S_COLOR)


            if az.tile[(i, j)] == 'w':
                rectangle(i+margin, j+margin, i+1-margin, j+2-margin, W_COLOR)


            if az.tile[(i, j)] == 'e':
                rectangle(i+margin, j-1+margin, i+1-margin, j+1-margin, E_COLOR)
    finish()


order = 7
az = AztecDiamond(0)
size = 300

for i in range(order):
    az.delete()
    if i == order - 1:
        render(az, size, 'step{:03d}.eps'.format(3 * i), True)

    az = az.slide()
    if i == order - 1:
        render(az, size, 'step{:03d}.eps'.format(3 * i + 1))

    az.create()
    if i == order - 2:
        render(az, size, 'step{:03d}.eps'.format(3 * i + 2), True)
    elif i == order - 1:
        render(az, size, 'step{:03d}.eps'.format(3 * i + 2), False)
