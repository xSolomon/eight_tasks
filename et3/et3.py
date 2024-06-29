''' Length of list with only pop(0) and len() functions permitted. '''

import ctypes

def list_length(list_object : list[ctypes.py_object]) -> int:
    ''' Increase counter and pop item from list until we get an empty list. '''
    if len(list_object) == 0:
        return 0
    list_object.pop(0)
    return 1 + list_length(list_object)
