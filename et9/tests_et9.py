''' Tests for task 9 solution function. '''

import unittest
from et9 import generate_all_correct_bracket_sequences as gen

class FindSecondMaximumTests(unittest.TestCase):
    ''' Tests for generate_all_correct_bracket_sequences function. '''
    def test_on_some_predefined_values(self) -> None:
        ''' Must generate exactly the same list as in the corresponding result list. '''
        results : list[list[str]] = [None, ["()"], ["(())", "()()"],
            ["((()))", "(()())", "(())()", "()(())", "()()()"]]
        for i, result in enumerate(results):
            with self.subTest():
                self.assertEqual(gen(i),result)

unittest.main()
