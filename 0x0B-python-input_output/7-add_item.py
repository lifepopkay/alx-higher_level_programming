#!/usr/bin/python3
"""
    7-add_item: load, add, and save
"""
import sys
"""
    import the file for saving into file and loading the file
"""
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    """
        call the file name
    """
    filename = "add_item.json"

    try:
        items = load(filename)  # this load the file containing the json
    except FileNotFoundError:
        items = []

    for arg in sys.argv[1:]:  # reads the terminal arguments
        items.append(arg)
    save(items, filename)
