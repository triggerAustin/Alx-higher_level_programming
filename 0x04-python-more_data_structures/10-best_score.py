#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return "None"
    keys = list(a_dictionary.keys())
    max_val = a_dictionary[keys[0]]
    for key in keys:
        if a_dictionary[key] > max_val:
            max_val = a_dictionary[key]
            return_key = key
    return return_key
