''' Find second maximum in the list. '''

def find_second_max_value(values : list[int], first_maximum : int, second_maximum : int,
    find_from_index : int) -> int:
    ''' Given current maximums and index to search from, returns second maximum in the list. '''
    if len(values) <= find_from_index:
        return second_maximum
    if values[find_from_index] > second_maximum:
        second_maximum = values[find_from_index]
    if values[find_from_index] > first_maximum:
        second_maximum = first_maximum
        first_maximum = values[find_from_index]
    return find_second_max_value(values, first_maximum, second_maximum, find_from_index + 1)

def find_second_maximum(values : list[int]) -> int | None:
    ''' Finds value by calling additional recursive function.
        Returns None if list is not big enough. '''
    if len(values) < 2:
        return None
    return find_second_max_value(values, values[0], values[1], 2) if values[0] > values[1] else \
        find_second_max_value(values, values[1], values[0], 2)
