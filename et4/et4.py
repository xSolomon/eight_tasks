''' Check if string is palindrom. '''

def is_palindrom(string_to_check : str) -> bool:
    ''' For strings with length > 1, check equality of first and last character, and repeat. '''
    if string_to_check == "":
        return True
    return is_palindrom(string_to_check[1:-1]) if string_to_check[0] == string_to_check[-1] \
        else False
