import sys

def main():
    print("""
    Two things are infinite:
    the universe and human stupidity;
    and I'm not sure about the universe.
    - Christopher Walken""" + str(sys.version_info))
    if sys.version_info >= (3, 6) and sys.version_info < (3, 7):
        # let's make this script fail for Python 3.6
        raise Exception('Python version 3.6.x is unsupported!')


if __name__ == "__main__":
    main()
