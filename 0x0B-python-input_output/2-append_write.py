#!/usr/bin/python3
def append_write(filename="", text=""):
    char_count = 0
    with open(filename, 'a', encoding=UTF8) as file:
        for char in text:
            file.write(char)
            char_count++
    return char_count
