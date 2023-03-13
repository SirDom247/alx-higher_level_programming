#!/usr/bin/python3
def element_at(my_list, idx):
    """ a function that prints the value and index of a list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        idx += 1
        return idx
