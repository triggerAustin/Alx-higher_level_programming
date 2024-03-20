#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    items = a_dictionary.copy().items()
    updated_dict = dict(map(lambda x: (x[0], x[1]*2), items))
    return updated_dict
