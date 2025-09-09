# # in hear we are gonna test the hello program by help of pytest and assert

from hello import hello


def test_hello():
    hello("David") == "Hello, David"