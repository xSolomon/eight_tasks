''' Evaluation of sum of digits in number. '''

def calculate_sum_of_digits(number : int, current_sum_of_digits : int = 0) -> int:
    ''' Add modulo 10 to sum and divide current number by 10 until it is not zero. '''
    if number == 0:
        return current_sum_of_digits
    return calculate_sum_of_digits(number // 10, current_sum_of_digits + number % 10)

def sum_of_digits_in_number(number : int) -> int:
    ''' Sum of digits in integer. '''
    return calculate_sum_of_digits(abs(number))
