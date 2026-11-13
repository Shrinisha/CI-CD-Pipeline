# test_calculator.py
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(10, 5) == 5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 100) == 0
    
def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"