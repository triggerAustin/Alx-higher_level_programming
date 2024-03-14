#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) != 1:
        (print((len(sys.argv) - 1), "argument:")
            if len(sys.argv) == 2
            else print((len(sys.argv) - 1), "arguments:"))
        i = 0
        for item in sys.argv:
            if i != 0:
                print("{}: {}".format(i, item))
            i += 1
    else:
        print("0 arguments.")
