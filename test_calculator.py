import calculator

def test_add():
    assert calculator.add(2, 3) == 5

def test_subtract():
    assert subtract(10, 5) == 5
    
def test_multiply():
    assert multiply(3, 4) == 12
   
def test_divide():
    assert divide(10, 2) == 5
    