#!/usr/bin/python3
import json
def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='UTF8') as file:
        filename.write(json.dumps(my_obj))

