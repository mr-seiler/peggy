from peggy.jump import Jump


def genHoleNames():
    """
    Generator for the keys used in board dictionaries
    """
    rows = ['A', 'B', 'C', 'D', 'E']
    for row in range(len(rows)):
        for idx in range(row + 1):
            yield rows[row] + str(idx)

LABELS = [l for l in genHoleNames()]

# This is a set of every conceivale jump, regardless of board configuration
EVERY_JUMP = {
        # starting at A0
        Jump('A0', 'B0', 'C0'),
        Jump('A0', 'B1', 'C2'),
        # start at B0
        Jump('B0', 'C0', 'D0'),
        Jump('B0', 'C1', 'D2'),
        # start at B1
        Jump('B1', 'C1', 'D1'),
        Jump('B1', 'C2', 'D3'),
        # start at C0
        Jump('C0', 'B0', 'A0'),
        Jump('C0', 'C1', 'C2'),
        Jump('C0', 'D0', 'E0'),
        Jump('C0', 'D1', 'E2'),
        # start at C1
        Jump('C1', 'D1', 'E1'),
        Jump('C1', 'D2', 'E3'),
        # start at C2
        Jump('C2', 'B1', 'A0'),
        Jump('C2', 'C1', 'C0'),
        Jump('C2', 'D2', 'E2'),
        Jump('C2', 'D3', 'E4'),
        # start  at D0
        Jump('D0', 'C0', 'B0'),
        Jump('D0', 'D1', 'D2'),
        # start at D1
        Jump('D1', 'C1', 'B1'),
        Jump('D1', 'D2', 'D3'),
        # start at D2
        Jump('D2', 'C1', 'B0'),
        Jump('D2', 'D1', 'D0'),
        # start at D3
        Jump('D3', 'C2', 'B1'),
        Jump('D3', 'D2', 'D1'),
        # start at E0
        Jump('E0', 'D0', 'C0'),
        Jump('E0', 'E1', 'E2'),
        # start at E1
        Jump('E1', 'D1', 'C1'),
        Jump('E1', 'E2', 'E3'),
        # start at E2
        Jump('E2', 'E1', 'E0'),
        Jump('E2', 'D1', 'C0'),
        Jump('E2', 'D2', 'C2'),
        Jump('E2', 'E3', 'E4'),
        # start at E3
        Jump('E3', 'D2', 'C1'),
        Jump('E3', 'E2', 'E1'),
        # start at E4
        Jump('E4', 'D3', 'C2'),
        Jump('E4', 'E3', 'E2')
    }
