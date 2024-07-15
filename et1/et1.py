''' Number N in power M. '''

def potentiate(number : int, exponent : int, product : int) -> int:
    ''' Potentiates integer in natural exponent. '''
    if exponent == 0:
        return product
    return potentiate(number, exponent - 1, product * number)
