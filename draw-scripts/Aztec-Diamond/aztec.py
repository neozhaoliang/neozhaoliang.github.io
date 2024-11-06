# -*- coding: utf-8 -*-

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Domino shuffling algorithm on Aztec diamond graphs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This script samples a random domino tiling of an Aztec diamond graph
with uniform probability.

Usage: python aztec.py [-s] [-o] [-f]

Optional arguments:
    -s    size of the image.
    -o    order of the Aztec diamond graph.
    -f    output file.

:copyright (c) 2015 by Zhao Liang.
"""
import argparse
import random

# 4 colors for the 4 types of dominoes
N_COLOR = (1, 0, 0)
S_COLOR = (0.75, 0.75, 0)
W_COLOR = (0, 0.5, 0)
E_COLOR = (0, 0, 1)


class AztecDiamond(object):
    """Use a dict to represent a tiling of an Aztec diamond graph.
    Items in the dict are of the form {cell: type} where a cell is a
    1x1 unit square and is specified by the coordinate of its left bottom
    corner. Each cell has five possible types: 'n', 's', 'w', 'e', None,
    here None means it's an empty cell.

    Be careful that one should always start from the boundary when
    deleting or filling blocks, this is an implicit but important
    part in the algorithm.
    """

    def __init__(self, n):
        """Create an Aztec diamond graph of order n with an empty tiling."""
        self.order = n

        self.cells = []
        for j in range(-n, n):
            k = min(n+1+j, n-j)
            for i in range(-k, k):
                self.cells.append((i, j))

        self.tile = {cell: None for cell in self.cells}

    @staticmethod
    def block(i, j):
        """Return the 2x2 block with its bottom-left cell at (i, j)."""
        return [(i, j), (i+1, j), (i, j+1), (i+1, j+1)]

    def is_black(self, i, j):
        """Check if cell (i, j) is colored black.
        Note that the chessboard is colored in the fashion that the
        leftmost cell in the top row is white.
        """
        return (i + j + self.order) % 2 == 1

    def check_block(self, i, j, dominoes):
        """Check whether a block is filled with dominoes of given orientations."""
        return all(self.tile[cell] == fill for cell, fill in zip(self.block(i, j), dominoes))

    def fill_block(self, i, j, dominoes):
        """Fill a block with two parallel dominoes of given orientations."""
        for cell, fill in zip(self.block(i, j), dominoes):
            self.tile[cell] = fill

    def delete(self):
        """Delete all bad blocks in a tiling.
        A block is called bad if it contains a pair of parallel dominoes that
        have orientations toward each other.
        """
        for i, j in self.cells:
            try:
                if (self.check_block(i, j, ['n', 'n', 's', 's'])
                        or self.check_block(i, j, ['e', 'w', 'e', 'w'])):
                    self.fill_block(i, j, [None]*4)
            except KeyError:
                pass
        return self

    def slide(self):
        """Move all dominoes one step according to their orientations."""
        new_board = AztecDiamond(self.order + 1)
        for (i, j) in self.cells:
            if self.tile[(i, j)] == 'n':
                new_board.tile[(i, j+1)] = 'n'
            if self.tile[(i, j)] == 's':
                new_board.tile[(i, j-1)] = 's'
            if self.tile[(i, j)] == 'w':
                new_board.tile[(i-1, j)] = 'w'
            if self.tile[(i, j)] == 'e':
                new_board.tile[(i+1, j)] = 'e'
        return new_board

    def create(self):
        """Fill all holes with pairs of dominoes that leaving each other.
        This is a somewhat subtle step since the new Aztec graph returned
        by the sliding step is placed on a different chessboard which is
        colored in the opposite fashion!
        """
        for i, j in self.cells:
            try:
                if self.check_block(i, j, [None]*4):
                    if random.random() > 0.5:
                        self.fill_block(i, j, ['s', 's', 'n', 'n'])
                    else:
                        self.fill_block(i, j, ['w', 'e', 'w', 'e'])
            except KeyError:
                pass
        return self
