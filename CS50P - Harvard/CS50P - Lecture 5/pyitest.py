# # in hear we use assert and pytest to test my calculator.py program
# # bu i'm gonna brack them in small parts to understand them better

from calculator import square


def test_Positive():
    assert square(2) == 4
    assert square(3) == 9


def test_Negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_Zero():
    assert square(0) == 0