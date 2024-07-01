''' Length of list with only pop(0) and len() functions permitted. '''

import ctypes

def calculate_list_length(list_object : list[ctypes.py_object], current_length : int = 0):
    ''' Pops one item from list and increase counter until we get an empty list. '''
    if len(list_object) == 0:
        return current_length
    list_object.pop(0)
    return calculate_list_length(list_object, current_length + 1)

def list_length(list_object : list[ctypes.py_object]) -> int:
    ''' Calculate length of list via popping all items from it. '''
    return calculate_list_length(list_object)
