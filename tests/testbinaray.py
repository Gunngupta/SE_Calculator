import unittest
from modules.binary import (
    binary_to_decimal, decimal_to_binary,
    binary_add, binary_subtract,
    binary_multiply, binary_divide,
    ones_complement, twos_complement,
)
from modules.exceptions import InvalidBinaryInputError, NegativeBinaryResultError


class TestBinaryConversions(unittest.TestCase):
    def test_bin_to_dec_basic(self):
        self.assertEqual(binary_to_decimal("B'1010"), "D'10")

    def test_bin_to_dec_zero(self):
        self.assertEqual(binary_to_decimal("B'0"), "D'0")

    def test_bin_to_dec_one(self):
        self.assertEqual(binary_to_decimal("B'1"), "D'1")

    def test_dec_to_bin_basic(self):
        self.assertEqual(decimal_to_binary("D'10"), "B'1010")

    def test_dec_to_bin_zero(self):
        self.assertEqual(decimal_to_binary("D'0"), "B'0")


class TestBinaryArithmetic(unittest.TestCase):
    def test_add(self):
        self.assertEqual(binary_add("B'011", "B'010"), "B'101")

    def test_subtract(self):
        self.assertEqual(binary_subtract("B'101", "B'010"), "B'011")

    def test_subtract_negative_raises(self):
        with self.assertRaises(NegativeBinaryResultError):
            binary_subtract("B'001", "B'010")

    def test_multiply(self):
        self.assertEqual(binary_multiply("B'011", "B'010"), "B'110")

    def test_divide(self):
        self.assertEqual(binary_divide("B'110", "B'010"), "B'11")

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            binary_divide("B'110", "B'0")


class TestComplements(unittest.TestCase):
    def test_ones_complement(self):
        self.assertEqual(ones_complement("B'1010"), "B'0101")

    def test_ones_all_zeros(self):
        self.assertEqual(ones_complement("B'0000"), "B'1111")

    def test_twos_complement(self):
        self.assertEqual(twos_complement("B'0111"), "B'1001")


    def test_twos_complement_zero(self):
        self.assertEqual(twos_complement("B'0000"), "B'10000")


class TestInvalidInput(unittest.TestCase):
    def test_invalid_char(self):
        with self.assertRaises(InvalidBinaryInputError):
            binary_to_decimal("B'1021")

    def test_empty_string(self):
        with self.assertRaises(InvalidBinaryInputError):
            binary_to_decimal("B'")

    def test_missing_prefix(self):
        with self.assertRaises(InvalidBinaryInputError):
            binary_to_decimal("1021")


if __name__ == '__main__':
    unittest.main()