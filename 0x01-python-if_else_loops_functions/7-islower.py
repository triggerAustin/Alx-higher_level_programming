#!/usr/bin/python3
def islower(c):
    value = ord(c)
    if value <= 122 and value >= 97:
        return True
    elif value <= 91 and value >= 65:
        return False
