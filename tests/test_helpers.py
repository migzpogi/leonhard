import unittest
from leonhard import helpers


class TestHelpers(unittest.TestCase):

    def test_if_input_is_negative_then_it_must_raise_value_error(self):
        with self.assertRaises(ValueError):
            helpers.raise_if_not_positive_int(-1)

    def test_if_input_is_string_then_it_must_raise_type_error(self):
        with self.assertRaises(TypeError):
            helpers.raise_if_not_positive_int("a")

    def test_if_input_is_zero_then_it_must_return_none(self):
        self.assertEqual(None, helpers.raise_if_not_positive_int(0))

    def test_if_input_is_positive_int_then_it_must_return_none(self):
        self.assertEqual(None, helpers.raise_if_not_positive_int(100))


if __name__ == '__main__':
    unittest.main()