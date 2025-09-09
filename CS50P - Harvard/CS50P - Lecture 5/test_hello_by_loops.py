# # in this program we are gonna test the hello program by help of pytest and assert
# # we are gonna test the program by two different wayss
# # one is by splitting the test cases into two different functions
# # the other is by using loops to test the program


from hello import hello


def test_default():
    assert hello() == "Hello, World"


def test_argument():
    for name in ["Marin", "David", "Alice", "Bob"]:
        assert hello(name) == f"Hello, {name}"