from src.math_operations import add,sub

def test_add():
    assert add(5,7)==12
    assert add(-10,11)==1
    assert add(10,2)==12

def test_sub():
    assert sub(1,2)==-1
    assert sub(4,2)==2
    assert sub(999,100)==899