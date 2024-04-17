#!/usr/bin/python3
import json
import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

def add_item(sys.argv):
    filename = "add_item.json"
    save_to_json_file(sys.argv, filename)
    data = load_from_json_file(filename)
