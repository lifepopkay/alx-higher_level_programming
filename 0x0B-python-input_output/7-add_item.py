#!/usr/bin/bin/python3
"""
    7-add_item: load, add, and save
"""
import sys
import os.path


save = __import__('7-save_to_json_file').save_to_json_file
load = __import__('8-load_from_json_file').load_from_json_file



if __name__ == "__main__":

    filename = "add_item.json"

    try:
        items = load(filename)
    except FileNotFoundError:
        items = []

    for arg in sys.argv[1:]:
        items.append(arg)
    save(items, filename)
