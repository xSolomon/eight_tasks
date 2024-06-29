''' Number N in power M. '''

def potentiate(number : int, exponent : int) -> int:
    ''' Potentiates integer in natural exponent. '''
    return 1 if exponent == 0 else number * potentiate(number, exponent - 1)
