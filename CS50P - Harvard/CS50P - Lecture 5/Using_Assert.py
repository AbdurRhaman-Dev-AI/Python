from calculator import square


def main():
    test_square()


def test_square():
    try:
        assert square(2) == 4
    
    except AssertionError:
        assert square(3) == 9
    
    try:
        assert square(3) == 9
    
    except AssertionError:
        print("Test failed: square(3) should be 9")
        try:
            assert square(-2) == 4

        except AssertionError:
            print("Test failed: square(-2) should be 4")

    try:
        assert square(-3) == 9
    
    except AssertionError:
        print("Test failed: square(-3) should be 9")

    try:
        assert square(0) == 0
    
    except AssertionError:
        print("Test failed: square(0) should be 0")


if __name__ == "__main__":
    main()