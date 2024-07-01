''' Check if string is palindrom. '''

def is_palindrom(string_to_check : str) -> bool:
    ''' For strings with length > 1, check equality of first and last character, and repeat. '''
    if string_to_check == "":
        return True
    if string_to_check[0] != string_to_check[-1]:
        return False
    return is_palindrom(string_to_check[1:-1])
