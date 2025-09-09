# # in this file we are gonna test the hello program by splitting the test cases into two different functions
# # one function will test the default case and the other function will test the argument case

from hello import hello


def test_default():
    assert hello() == "Hello, World"


def test_argument():
    assert hello("Marin") == "Hello, Marin"