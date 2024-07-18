''' Check if string is palindrom. '''

def is_palindrom(string_to_check : str, check_from_index : int) -> bool:
    ''' For strings with length > 1, checks whether it is palindrom. '''
    if check_from_index >= len(string_to_check):
        return True
    if string_to_check[check_from_index] != string_to_check[-check_from_index - 1]:
        return False
    return is_palindrom(string_to_check, check_from_index + 1)
