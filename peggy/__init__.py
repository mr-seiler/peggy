"""Package for peg game simulation code"""

# import constants
from peggy.constants import *
# import board class
from peggy.board import Board


def main():
    empty_hole = 'C1'
    board = Board.getStartingBoard(empty_hole)
    print(board.pretty())
    print(board.getValidJumps())
