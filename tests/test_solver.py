import pytest

import peggy.solver as s

def test_insideOut():
    start = [ [1, 2, 3], [1, 2, 3], [1, 2, 3], [1, 2, 3] ]
    end = [ [1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3] ]
    assert s.insideOut(start) == end
