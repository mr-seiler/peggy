import pytest

from peggy.constants import *
from peggy.board import Board

some_boards = {
        # one empty hole (two valid moves)
        'basic': { 'A0': False, 'B0': True, 'B1': True, 'C0': True, 'C1': True,
            'C2': True, 'D0': True, 'D1': True, 'D2': True, 'D3': True,
            'E0': True, 'E1': True, 'E2': True, 'E3': True, 'E4': True },
        # no pegs (no valid moves)
        'empty': { 'A0': False, 'B0': False, 'B1': False, 'C0': False, 'C1': False,
            'C2': False, 'D0': False, 'D1': False, 'D2': False, 'D3': False,
            'E0': False, 'E1': False, 'E2': False, 'E3': False, 'E4': False },
        # all pegs (no valid moves)
        'full': { 'A0': True, 'B0': True, 'B1': True, 'C0': True, 'C1': True,
            'C2': True, 'D0': True, 'D1': True, 'D2': True, 'D3': True,
            'E0': True, 'E1': True, 'E2': True, 'E3': True, 'E4': True },
        # two isolated pegs (no valid moves)
        'isle': { 'A0': False, 'B0': False, 'B1': False, 'C0': False, 'C1': False,
            'C2': False, 'D0': False, 'D1': False, 'D2': False, 'D3': False,
            'E0': False, 'E1': False, 'E2': False, 'E3': False, 'E4': False },
        # occupied B0, C0, C1, D1, D0 (four valid moves)
        'max': { 'A0': False, 'B0': True, 'B1': False, 'C0': True, 'C1': True,
            'C2': False, 'D0': True, 'D1': True, 'D2': False, 'D3': False,
            'E0': False, 'E1': False, 'E2': False, 'E3': False, 'E4': False }
        }


# Don't think this really needs to be a fixture, could just create a variable
# for the object and hand it around in parametrize annotatons?
@pytest.fixture(scope='module')
def a_board():
    return Board(some_boards['max'])


# not sure why this passes for 'None', but it does?
@pytest.mark.parametrize("start_hole", ['A0', 'C1', None, 'A1'])
def test_startingBoards(start_hole):
    b = Board.getStartingBoard(start_hole)
    occupied = {l for l in b.state if b.state[l]}
    want_occupied = set(LABELS) - { start_hole }
    assert occupied == want_occupied


@pytest.mark.parametrize("j,ok", [
    (Jump('C0', 'B0', 'A0'), True),
    (Jump('C0', 'D1', 'E2'), True),
    (Jump('E2', 'D1', 'C0'), False),
    (Jump('C2', 'D3', 'E4'), False),
    (Jump('C1', 'C0', 'C2'), False),
    (Jump('C0', 'D0', 'E1'), False)
])
def test_isValidJump(a_board, j, ok):
    assert a_board.isValidJump(j) == ok

# for one particular board, we know exactly which jumps should be valid.
# TODO: need to somehow test edge cases, though!
def test_getValidJumps(a_board):
    assert a_board.getValidJumps() == {
        Jump('C0', 'B0', 'A0'),
        Jump('C0', 'C1', 'C2'),
        Jump('C0', 'D1', 'E2'),
        Jump('C0', 'D0', 'E0'),
        Jump('D0', 'D1', 'D2'),
        Jump('C1', 'D1', 'E1'),
        Jump('D1', 'C1', 'B1'),
        Jump('B0', 'C1', 'D2')
        }


@pytest.mark.parametrize("j,res", [
    # valid move
    (Jump('C0', 'B0', 'A0'), Board({ 'A0': True, 'B0': False, 'B1': False, 'C0': False, 'C1': True,
        'C2': False, 'D0': True, 'D1': True, 'D2': False, 'D3': False,
        'E0': False, 'E1': False, 'E2': False, 'E3': False, 'E4': False })),
    # invalid move - maybe this should raise exception?
    (Jump('C1', 'B0', 'A0'), Board(some_boards['max'])),
    # ridiculous move - maybe this should raise exception?
    (Jump('E0', 'D2', 'E4'), Board(some_boards['max']))
    ])
def test_doJump(a_board, j, res):
    assert a_board.doJump(j) == res


# TODO: doesn't test any exceptional circumstances
# genNexts() uses getValidJumps, which returns a set. Therefore we cannot
# guarantee (and cannot test) the order of the boards in the list, so we
# compare sets of boards here.
@pytest.mark.parametrize("brd", [
    Board(some_boards['basic'])
])
def test_genNexts(brd):
    assert { n for n in brd.genNexts() } == {
        Board({ 'A0': True, 'B0': False, 'B1': True, 'C0': False, 'C1': True,
            'C2': True, 'D0': True, 'D1': True, 'D2': True, 'D3': True,
            'E0': True, 'E1': True, 'E2': True, 'E3': True, 'E4': True }),
        Board({ 'A0': True, 'B0': True, 'B1': False, 'C0': True, 'C1': True,
            'C2': False, 'D0': True, 'D1': True, 'D2': True, 'D3': True,
            'E0': True, 'E1': True, 'E2': True, 'E3': True, 'E4': True })
        }

# this will be incredibly tedious to test thoroughly
def test_genAllNexts():
    pass

