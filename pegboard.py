#! /usr/bin/env python3

# import Jump class
from constants import *
from board import Board


if __name__ == '__main__':
    # what is a "board?" just a dictionary of labels -> pegs
    # peg is T/F to show whether or not the hole is occupied

    empty_hole = 'C1'
    board = Board.getStartingBoard(empty_hole)
    print(board.pretty())
    print(board.getValidJumps())

