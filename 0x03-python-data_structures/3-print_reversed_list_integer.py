#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        a = my_list[::-1]
        for item in a:
            print("{:d}".format(item))
