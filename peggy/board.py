# get constants
from peggy.constants import *

class Board:
    """ Represents a board state using a dictionary """
    def __init__(self, state_dict):
        self.state = state_dict
        self._hash = hash(frozenset(self.state.items()))

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return repr(self.state)

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return self._hash

    def hasPeg(self, hole):
        """ Does this board have a peg in the specified hole? """
        return self.state[hole]

    def numPegs(self):
        count = 0
        for k in iter(self.state):
            if self.state[k]:
                count += 1
        return count

    def pretty(self):
        """ Return nice formatted string representation of the board.
        Could maybe be implemented in __format__(self) instead? """

        def getHoleStrs(stateDict):
            """ Helper method that gets a list of string representing the state of each hole """
            strs = list()
            for l in LABELS:
                if stateDict[l]:
                    strs.append("o")
                else:
                    strs.append(".")
            return strs

        fmtStr = "\n".join([
            "    {}",
            "   {} {}",
            "  {} {} {}",
            " {} {} {} {}",
            "{} {} {} {} {}"
            ])
        return fmtStr.format(*getHoleStrs(self.state))

    def isValidJump(self, jump):
        """ Check if the given jump is valid for this board """
        s = self.state
        return jump in EVERY_JUMP and s[jump.origin] and s[jump.over] and not s[jump.dest]

    def getValidJumps(self):
        """ Get a set of jumps which are valid for this board """
        return {j for j in EVERY_JUMP if self.isValidJump(j)}

    def finished(self):
        """ this board is in a finished state when there are no valid moves """
        return len(self.getValidJumps()) == 0

    def victory(self):
        return self.finished() and self.numPegs() == 1

    def doJump(self, jump):
        """ Return a new board representing the game state after executing the given jump """
        # FIXME: raise exception instead
        if not self.isValidJump(jump):
            return self

        s = self.state.copy()

        s[jump.origin] = False
        s[jump.over] = False
        s[jump.dest] = True

        return Board(s)

    def genNexts(self):
        """ Generate sequence of next valid boards from this board """
        for move in self.getValidJumps():
            yield self.doJump(move)

    @staticmethod
    def genAllNexts(boardList):
        """ Generate seq of next valid boards for a list of boards """
        for b in boardList:
            for n in b.genNexts():
                yield n

    @staticmethod
    def getStartingBoard(empty_hole='A0'):
        return Board({lbl: (lbl != empty_hole) for lbl in LABELS})

