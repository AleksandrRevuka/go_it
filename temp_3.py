import sys

from temp_1 import main as greeting
from temp_2 import main as exiting


def main():
    try:
        if sys.argv[1] == 'greet':
            greeting()
        elif sys.argv[1] == 'goodbuy':
            exiting()
        else:
            print("Unknown argument")
    except IndexError:
        print("Argument must be 'greet' or 'goodbuy'")

if __name__ == '__main__':
    main()
