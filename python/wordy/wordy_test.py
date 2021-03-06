import unittest

from wordy import calculate


# Tests adapted from `problem-specifications//canonical-data.json` @ v1.1.0

class WordyTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculate("What is 1 plus 1?"), 2)

    def test_more_addition(self):
        self.assertEqual(calculate("What is 53 plus 2?"), 55)

    def test_addition_with_negative_numbers(self):
        self.assertEqual(calculate("What is -1 plus -10?"), -11)

    def test_large_addition(self):
        self.assertEqual(calculate("What is 123 plus 45678?"), 45801)

    def test_subtraction(self):
        self.assertEqual(calculate("What is 4 minus -12?"), 16)

    def test_multiplication(self):
        self.assertEqual(calculate("What is -3 multiplied by 25?"), -75)

    def test_division(self):
        self.assertEqual(calculate("What is 33 divided by -3?"), -11)

    def test_multiple_addition(self):
        self.assertEqual(calculate("What is 1 plus 1 plus 1?"), 3)

    def test_addition_then_subtraction(self):
        self.assertEqual(calculate("What is 1 plus 5 minus -2?"), 8)

    def test_multiple_subtraction(self):
        self.assertEqual(calculate("What is 20 minus 4 minus 13?"), 3)

    def test_subtraction_then_addition(self):
        self.assertEqual(calculate("What is 17 minus 6 plus 3?"), 14)

    def test_multiple_multiplication(self):
        self.assertEqual(
            calculate("What is 2 multiplied by -2 multiplied by 3?"), -12)

    def test_addition_then_multiplication(self):
        self.assertEqual(calculate("What is -3 plus 7 multiplied by -2?"), -8)

    def test_multiple_division(self):
        self.assertEqual(
            calculate("What is -12 divided by 2 divided by -3?"), 2)

    def test_unknown_operation(self):
        with self.assertRaisesWithMessage(ValueError):
            calculate("What is 52 cubed?")

    def test_non_math_question(self):
        with self.assertRaisesWithMessage(ValueError):
            calculate("Who is the President of the United States?")

    # Additional tests for this track

    def test_missing_operation(self):
        with self.assertRaisesWithMessage(ValueError):
            calculate("What is 2 2 minus 3?")

    def test_missing_number(self):
        with self.assertRaisesWithMessage(ValueError):
            calculate("What is 7 plus multiplied by -2?")

    # Utility functions
    def setUp(self):
        try:
            self.assertRaisesRegex
        except AttributeError:
            self.assertRaisesRegex = self.assertRaisesRegexp

    def assertRaisesWithMessage(self, exception):
        return self.assertRaisesRegex(exception, r".+")


if __name__ == '__main__':
    unittest.main()