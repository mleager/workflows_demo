def main():
    print("""
    Two things are infinite:
    the universe and human stupidity;
    and I'm not sure about the universe.
    - Christopher Walken
    From Python:""" + str(sys.version_info))
    if sys.version_info >= (3, 6) and sys.version_info < (3, 7):
        raise Exception("Python version 3.6x is unsupported!")


if __name__ == "__main__":
    main()
