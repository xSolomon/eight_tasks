''' Evaluation of sum of digits in number. '''

def sum_of_digits_in_number(number : int, current_sum_of_digits : int = 0) -> int:
    ''' Sum of digits in natural number. '''
    if number == 0:
        return current_sum_of_digits
    return sum_of_digits_in_number(number // 10, current_sum_of_digits + number % 10)
