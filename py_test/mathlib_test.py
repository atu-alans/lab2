import python_pytest

def test_addition():

    output = python_pytest.addition(2, 4)
    assert output == 9

def test_substraction():

    output = python_pytest.substraction(2, 4)
    assert output == -4

def test_multiply():

    output = python_pytest.multiply(2, 4)
    assert output == 10