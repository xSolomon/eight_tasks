''' Tests for list_length function. '''

import unittest
import io
import sys
from et6 import print_even_indexed_vals as print_list

class PrintEvenValsFromListTests(unittest.TestCase):
    ''' Tests for print_even_indexed_vals function. '''
    def setUp(self) -> None:
        ''' Test preparations. '''
        self.result = io.StringIO()
        sys.stdout = self.result

    def tearDown(self) -> None:
        ''' Aftertest cleanup. '''
        sys.stdout = sys.__stdout__

    def test_on_empty_list(self) -> None:
        ''' Must print nothing '''
        print_list([])
        self.assertEqual(self.result.getvalue(), "")

    def test_on_singleval_list(self) -> None:
        ''' Must print exactly that value. '''
        print_list([5])
        self.assertEqual(self.result.getvalue(), "5\n")

    def test_on_two_elem_list(self) -> None:
        ''' Must print only the first value. '''
        print_list([7, 8])
        self.assertEqual(self.result.getvalue(), "7\n")

    def test_on_three_elem_list(self) -> None:
        ''' Must print only the first and third values. '''
        print_list([7, 8, 9])
        self.assertEqual(self.result.getvalue(), "7\n9\n")

    def test_on_some_predefined_lists(self) -> None:
        ''' Expected same result as in corresponding value in the result list. '''
        input_lists : list[list[int]] = [[1, 2, 3, 4, 5, 6], [0, 0, 0, 0], [1, 1, 1, 1, 1],
            [10, 8, 6, 4, 2, 0]]
        expected_results : list[str] = ["1\n3\n5\n", "0\n0\n", "1\n1\n1\n", "10\n6\n2\n"]
        for i, input_list in enumerate(input_lists):
            with self.subTest():
                print_list(input_list)
                self.assertEqual(self.result.getvalue(), expected_results[i])
            self.result.truncate(0)
            self.result.seek(0)

unittest.main()
