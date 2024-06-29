''' Evaluation of sum of digits in number. '''

def sum_of_digits_in_number(number : int) -> int:
    ''' Sum of digits of natural number. '''
    return 0 if number == 0 else number % 10 + sum_of_digits_in_number(number // 10)
