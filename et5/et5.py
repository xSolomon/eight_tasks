''' Print only even values from list. '''

def print_even_vals_from_list(values : list[int], print_from_index : int) -> None:
    ''' Recursively prints values by iterating through the list via second argument. '''
    if print_from_index >= len(values):
        return
    if values[print_from_index] % 2 == 0:
        print(values[print_from_index])
    print_even_vals_from_list(values, print_from_index + 1)
