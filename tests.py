import unittest
from unittest.mock import patch
from main import calculate_digit_sum

class TestCalculateDigitSum(unittest.TestCase):

    @patch('builtins.input', side_effect=['123', '456', '789', '999', '1', '2', '3', '567', '0'])
    def test_max_digit_sum_number(self, mock_input):
        max_number = calculate_digit_sum()
        self.assertEqual(max_number, 999)

    def test_negative_number_digit_sum(self):
        digit_sum = calculate_digit_sum(-1234)
        self.assertEqual(digit_sum, 10)

    def test_positive_number_digit_sum(self):
        digit_sum = calculate_digit_sum(456)
        self.assertEqual(digit_sum, 15)

    @patch('builtins.input', side_effect=['abc', '12.34', '0'])
    def test_input_validation(self, mock_input):
        with self.assertRaises(ValueError):
            calculate_digit_sum()

if __name__ == '__main__':
    unittest.main()
