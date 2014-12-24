# after some experimenting... I think we're going to use sets instead of lists
# for the states.  There are just too many ways to end up in duplicate states,
# so we're going to implicitly filter out extra paths that lead to a state
# we've already reached some other way

from peggy.constants import *
from peggy.board import Board

def solveAll():
    """ Prints solutions for all possible boards """
    initial_boards = [ Board.getStartingBoard(l) for l in LABELS ]

    for b in initial_boards:
        solveOne(b)

def solveOne(board):
    """ Prints the solution for a single board """
    end_states = getEndStates(board)
    victory_states = { s for s in end_states if s.victory() }
    print("Starting board:")
    print(board.pretty())
    print("Winning states: {:d}".format(len(victory_states)))
    for s in victory_states:
        print(s.pretty())
    print("-----")


def getEndStates(start_state):
    """ Produces the set of end states for a given single seed state """
    current_states = { start_state }
    end_states = set()

    while len(current_states) != 0:
        # get the next seq of states
        next_states = { s for s in Board.genAllNexts(current_states) }
        # separate end states from seed states
        current_states = set()
        for s in next_states:
            if s.finished():
                end_states.add(s)
            else:
                current_states.add(s)
        # if we have no more seed states, then we're done

    # return sequence of end states
    return end_states
