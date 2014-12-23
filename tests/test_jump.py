import pytest
from peggy.jump import Jump

@pytest.fixture(scope='module')
def j1():
    return Jump('A0', 'B0', 'C0')

@pytest.fixture(scope='module')
def j2():
    return Jump('A0', 'B0', 'C0')

@pytest.fixture(scope='module')
def j3():
    return Jump('A0', 'B1', 'C2')

def test_jump(j1):
    assert hasattr(j1, 'origin')
    assert hasattr(j1, 'over')
    assert hasattr(j1, 'dest')

def test_jump_eq(j1, j2, j3):
    assert j1 == j2
    assert not j2 == j3

def test_jump_hash(j1, j2, j3):
    assert j1.__hash__() == j2.__hash__()
    assert not j2.__hash__() == j3.__hash__()
