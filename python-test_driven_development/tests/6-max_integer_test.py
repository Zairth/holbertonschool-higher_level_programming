#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_regular_case(self):
        """Test with a normal list of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_another_regular_case(self):
        """Test another normal list"""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test with a list containing a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers"""
        self.assertEqual(max_integer([-5, -2, -9]), -2)

    def test_mixed_numbers(self):
        """Test with a list containing both positive and negative numbers"""
        self.assertEqual(max_integer([1, -1, 0, 3]), 3)

    def test_float_numbers(self):
        """Test with float numbers"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)

    def test_large_numbers(self):
        """Test with very large numbers"""
        self.assertEqual(max_integer([99999999, 100000000, 100000001]),
                         100000001)

    def test_large_numbers(self):
        """Test with a string"""
        self.assertEqual(max_integer([99999999, 100000000, 100000001]),
                         100000001)

    def test_max_at_the_beginning(self):
        """Test with the max at the beginning"""
        self.assertEqual(max_integer([4, 2, 3, 1]), 4)


if __name__ == '__main__':
    unittest.main()
