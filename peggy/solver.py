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
        solveBoard(b)

def insideOut(history_lists):
    """ No idea what to call this method.  Takes a 2D list of the form
    [ [1, 2], [1, 2] ] and transforms it to [ [1, 1], [2, 2] ].  Of course
    this only works when the 2D list is not 'ragged' (the sublists are all
    the same length) """

    res = []

    # for each generation in the histories
    for i in range(len(history_lists[0])):
        res.insert(i, [])
        # and for each different history
        for l in history_lists:
            # state from the current gen from this solution
            res[i].append(l[i])

    return res

def getGenerationStrs(generationList):
    """ Produces a list of strings, where each string shows the current
    board state at a particular step for multiple solutions in parallel.
    For the output to make any sense, the list passed to this method should
    specifically be in the format produced by insideOut() """

    str_list = []
    # for each generation...
    for g in generationList:
        lines_list = [ "", "", "", "", "" ]
        # for every solution in that generation:
        for s in g:
            # list of lines for just this solution
            lines = s.pretty().splitlines()
            # take each of those lines
            for i in range(len(lines)):
                # ...and append them to create one big line w/ all solutions
                lines_list[i] = lines_list[i] + lines[i]

        # at this point, we have a list of lines for a single generation
        # combine that into a single string for the generation
        str_list.append("\n".join(lines_list))

    # this should be a list of strings where each string shows all the
    # solutions in parallel for a single generation
    return str_list


def solveOne(start_pos):
    """ wrapper for solveBoard() that takes a start position string
    instead of a board object """
    solveBoard(Board.getStartingBoard(start_pos))

def solveBoard(board):
    """ Prints the solution for a single board """

    # get all final states and filter down to winning states
    win_states = { s for s in getEndStates(board) if s.victory() }
    print("Winning states: {:d}".format(len(win_states)))

    # histories will be a list of lists where each sublist is its own solution
    histories = []
    for s in win_states:
        histories.append(s.getHistory())

    # transform that 2D list into a single list where each item is a string
    # showing one step for all known solutions in parallel
    gen_strs = getGenerationStrs(insideOut(histories))

    # print that^
    for i in range(len(gen_strs)):
        print("Step #{:d}:".format(i))
        print(gen_strs[i])

    # provide some sort of terminator
    print("--------------------------------------------")


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
