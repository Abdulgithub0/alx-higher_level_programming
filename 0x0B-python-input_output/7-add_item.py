#!/usr/bin/python3
"""function that add all arg to list obj"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    my_list = []
length = len(sys.argv)
i = 1
while i < length:
    my_list.append(sys.argv[i])
    i += 1
save_to_json_file(my_list, 'add_item.json')
