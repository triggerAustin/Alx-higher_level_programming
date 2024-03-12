#!/usr/bin/python3
def print_last_digit(number):
    value = 0
    if number < 0:
        value = ((number * -1) % 10)
    else:
        value = number % 10
    print("{:d}".format(value), end="")
    return value
