''' Number N in power M. '''

def do_potentiate(number : int, exponent : int, current_squared_value : int,
    product : int = 1) -> int:
    ''' Uses successive squaring algorithm. '''
    if exponent == 0:
        return product
    if exponent % 2 == 0:
        return do_potentiate(number, exponent // 2, current_squared_value * current_squared_value,
            product)
    return do_potentiate(number, exponent - 1, current_squared_value,
        current_squared_value * product)

def potentiate(number : int, exponent : int) -> int:
    ''' Potentiates integer in natural exponent. '''
    return do_potentiate(number, exponent, number)
