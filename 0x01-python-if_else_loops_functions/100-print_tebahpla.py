#!/usr/bin/python3
for i in range(122, 96, -1):
    if (i % 10) % 2 == 0:
        print("{:s}".format(chr(i)), end='')
    else:
        print("{:s}".format(chr(i - 32)), end='')
