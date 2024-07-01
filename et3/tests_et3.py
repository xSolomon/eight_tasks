''' Tests for list_length function. '''

import unittest
from random import randint
from et3 import list_length

class ListLengthTests(unittest.TestCase):
    ''' Regression, border and random tests. '''
    def test_on_empty_list(self) -> None:
        ''' Expected 0 '''
        self.assertEqual(list_length([]), len([]))

    def test_on_single_elem_list(self) -> None:
        ''' Expected 1 '''
        self.assertEqual(list_length([5]), len([5]))

    def test_on_large_random_lists(self) -> None:
        ''' Expected each value to be the same that counted inside subtest. '''
        subtest_number : int = 10000
        maximum_list_length : int = 970
        for _ in range(subtest_number):
            test_list : list[int] = []
            for _ in range(randint(0, maximum_list_length)):
                test_list.append(randint(-100, 100))
            expected_length : int = len(test_list)
            with self.subTest():
                self.assertEqual(list_length(test_list), expected_length)
            test_list.clear()

unittest.main()
