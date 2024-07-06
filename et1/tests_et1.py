''' Tests for potentiate function. '''

import unittest
from random import randint
from et1 import potentiate

class PotentiateTests(unittest.TestCase):
    ''' Regression, border and random tests. '''
    def test_on_zero_number_and_power(self) -> None:
        ''' 0 ^ 0 == 1 '''
        self.assertEqual(potentiate(0, 0), 1)

    def test_on_zero_in_one(self) -> None:
        ''' 0 ^ 1 == 0 '''
        self.assertEqual(potentiate(0, 1), 0)

    def test_on_zero_in_two(self) -> None:
        ''' 0 ^ 2 == 0 '''
        self.assertEqual(potentiate(0, 2), 0)

    def test_on_one_in_zero(self) -> None:
        ''' 1 ^ 0 == 1 '''
        self.assertEqual(potentiate(1, 0), 1)

    def test_on_one_in_two(self) -> None:
        ''' 1 ^ 2 == 1 '''
        self.assertEqual(potentiate(1, 2), 1)

    def test_on_two_in_two(self) -> None:
        ''' 2 ^ 2 == 4 '''
        self.assertEqual(potentiate(2, 2), 4)

    def test_on_three_in_five(self) -> None:
        ''' 3 ^ 5 == 243 '''
        self.assertEqual(potentiate(3, 5), 243)

    def test_on_large_random_input(self) -> None:
        ''' Using python ** function for checking correctness. '''
        subtest_number : int = 100000
        for _ in range(subtest_number):
            number : int = randint(0, 500)
            exponent : int = randint(0, abs(500 // number)) if number != 0 else randint(0, 500)
            with self.subTest():
                self.assertEqual(potentiate(number, exponent), number ** exponent)

unittest.main()
