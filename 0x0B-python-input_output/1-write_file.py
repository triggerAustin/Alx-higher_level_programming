#!/usr/bin/python3
def write_file(filename="", text=""):
    char_count = 0
    with open(filename, 'w', encoding='UTF8') as file:
        for char in text:
            file.write(char)
            char_count++
    return char_count
