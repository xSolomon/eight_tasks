''' Tests for task 7 solution function. '''

import unittest
from random import randint
from et7 import find_second_maximum as find_max

class FindSecondMaximumTests(unittest.TestCase):
    ''' Tests for find_second_maximum function. '''
    def test_on_empty_list(self) -> None:
        ''' Must return "None" value. '''
        self.assertIsNone(find_max([]))

    def test_on_singleval_list(self) -> None:
        ''' Must return "None" value. '''
        self.assertIsNone(find_max([5]))

    def test_on_two_elem_list(self) -> None:
        ''' Must return smallest of two values. '''
        self.assertEqual(find_max([3, 5]), 3)
        self.assertEqual(find_max([7, 2]), 2)

    def test_on_three_elem_lists(self) -> None:
        ''' Must return second biggest of three values. '''
        test_lists : list[list[int]] = [[1, 2, 3], [2, 1, 3], [1, 3, 2], [2, 3, 1], [3, 1, 2],
            [3, 2, 1], [3, 3, 3], [3, 2, 3], [3, 2, 2]]
        results : list[int] = [2, 2, 2, 2, 2, 2, 3, 3, 2]
        for i, elem in enumerate(test_lists):
            with self.subTest(list = elem, expected = results[i]):
                self.assertEqual(find_max(elem), results[i])

    def test_on_large_random_lists(self) -> None:
        ''' For each list expected the same value as calculated in test. '''
        times_to_test : int = 1000
        test_list_length : int = 500
        for _ in range(times_to_test):
            test_values : list[int] = [randint(-500, 500) for _ in range (test_list_length)]
            result : int = find_max(test_values)
            test_values.sort()
            expected_result : int = test_values[-2]
            with self.subTest():
                self.assertEqual(result, expected_result)
            test_values.clear()

unittest.main()
