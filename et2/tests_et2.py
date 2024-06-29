''' Tests for sum_of_digits_in_number function. '''

import unittest
from random import randint, choice
from et2 import sum_of_digits_in_number as digits_sum

class DigitsSumTests(unittest.TestCase):
    ''' Regression, border and random tests. '''
    def test_on_zero(self) -> None:
        ''' Expected 0 '''
        self.assertEqual(digits_sum(0), 0)

    def test_on_five(self) -> None:
        ''' Expected 5 '''
        self.assertEqual(digits_sum(5), 5)

    def test_on_142(self) -> None:
        ''' Expected 7 '''
        self.assertEqual(digits_sum(142), 7)

    def test_on_large_random_numbers(self) -> None:
        ''' Expected each value to be the same that counted inside subtest. '''
        subtest_number : int = 10
        digits : list[int] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        max_digits_in_number : int = 15
        for _ in range(subtest_number):
            number : int = 0
            sum_of_digits : int = 0
            for i in range(randint(0, max_digits_in_number)):
                digit : int = choice(digits)
                sum_of_digits += digit
                number += digit * 10 ** i
            with self.subTest(number = number, sum = sum_of_digits):
                self.assertEqual(digits_sum(number), sum_of_digits)

unittest.main()
