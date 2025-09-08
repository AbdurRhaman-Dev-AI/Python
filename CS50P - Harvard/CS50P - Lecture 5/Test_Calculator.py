from calculator import square

def main():
    test_square()


def test_square():
    if square(2) != 4:
        print("Test failed: square(2) should be 4")
    elif square(3) != 9:
        print("Test failed: square(3) should be 9")


if __name__ == "__main__":
    main()