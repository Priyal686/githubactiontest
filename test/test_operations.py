from src.math_operations import add,sub

def test_add():
    assert add(2,3) == 5
    assert add(-1,1) == 0

def test_sub():
    assert sub(4,5) == -1
    assert sub(8,6) == 2
    assert sub(1,1) == 0
    assert sub(0,9) == -9