''' Length of list with only pop(0) and len() functions permitted. '''

import ctypes

def list_length(objects : list[ctypes.py_object], current_length : int) -> int:
    ''' Calculate length of list via popping all items from it. '''
    if len(objects) == 0:
        return current_length
    objects.pop(0)
    return list_length(objects, current_length + 1)
