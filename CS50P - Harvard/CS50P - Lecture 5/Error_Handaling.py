# # in hear we will use pytest and loop to continio check the test cases

from calculator import square


def test_positive():
    for i in range(1, 10):
        assert square(i) == i * i


def test_negative():
    for i in range(-1, -10, -1):
        assert square(i) == i * i


def test_zero():
    assert square(0) == 0