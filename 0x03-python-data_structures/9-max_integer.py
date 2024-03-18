#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list and len(my_list) > 0:
        a = my_list[0]
        for item in my_list:
            if item > a:
                a = item
    else:
        return "None"
    return a
