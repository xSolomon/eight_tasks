''' Length of list with only pop(0) and len() functions permitted. '''

import ctypes

def list_length(list_object : list[ctypes.py_object], current_length : int = 0) -> int:
    ''' Calculate length of list via popping all items from it. '''
    if len(list_object) == 0:
        return current_length
    list_object.pop(0)
    return list_length(list_object, current_length + 1)
