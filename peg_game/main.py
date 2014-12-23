# import constants
from peg_game.constants import *
# import board class
from peg_game.board import Board


def main():
    empty_hole = 'C1'
    board = Board.getStartingBoard(empty_hole)
    print(board.pretty())
    print(board.getValidJumps())
