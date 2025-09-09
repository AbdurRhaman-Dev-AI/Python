from hello import hello


def test_hello():
    assert hello("Marin") == "Hello, Marin"
    assert hello() == "Hello, World"