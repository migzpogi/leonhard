import unittest
from leonhard import leonhard


class TestGetFactorsOfPositiveIntegers(unittest.TestCase):

    def test_if_input_is_negative_integer_then_it_must_raise_type_error(self):
        with self.assertRaises(TypeError):
            leonhard.get_factors_of_positive_integer(-1)

    def test_if_input_is_not_an_integer_then_it_must_raise_type_error(self):
        with self.assertRaises(TypeError):
            leonhard.get_factors_of_positive_integer("foo")

    def test_result_must_be_of_type_list(self):
        self.assertTrue(issubclass(type(leonhard.get_factors_of_positive_integer(10)), list))

    def test_if_input_is_0_then_it_must_be_0(self):
        self.assertEqual(leonhard.get_factors_of_positive_integer(0), [0])

    def test_if_input_is_1_then_it_must_be_1(self):
        self.assertEqual(leonhard.get_factors_of_positive_integer(1), [1])

    def test_if_input_is_4_then_it_must_be_124(self):
        self.assertEqual(leonhard.get_factors_of_positive_integer(4), [1, 2, 4])

    def test_if_input_is_12345678(self):
        self.assertEqual(leonhard.get_factors_of_positive_integer(12345678),
                         [1, 2, 3, 6, 9, 18, 47, 94, 141, 282, 423, 846, 14593, 29186, 43779, 87558, 131337, 262674,
                          685871, 1371742, 2057613, 4115226, 6172839, 12345678])


class TestGenerateFibonacciSequence(unittest.TestCase):

    def test_if_number_of_terms_is_less_than_2_then_it_must_raise_a_value_error(self):
        with self.assertRaises(ValueError):
            leonhard.generate_fibonacci_sequence(1)

    def test_if_first_term_is_less_than_0_then_it_must_raise_a_value_error(self):
        with self.assertRaises(ValueError):
            leonhard.generate_fibonacci_sequence(2, -1)

    def test_if_second_term_is_less_than_first_then_it_must_raise_a_value_error(self):
        with self.assertRaises(ValueError):
            leonhard.generate_fibonacci_sequence(2, 1, 0)

    def test_if_first_term_is_provided_and_no_second_term_then_it_must_be_less_than_1(self):
        with self.assertRaises(ValueError):
            leonhard.generate_fibonacci_sequence(2, 5)

    def test_if_number_of_terms_is_not_integer_then_it_must_raise_a_type_error(self):
        with self.assertRaises(TypeError):
            leonhard.generate_fibonacci_sequence("a")

    def test_if_first_term_is_not_integer_then_it_must_raise_a_type_error(self):
        with self.assertRaises(TypeError):
            leonhard.generate_fibonacci_sequence(2, "a")

    def test_if_second_term_is_not_integer_then_it_must_raise_a_type_error(self):
        with self.assertRaises(TypeError):
            leonhard.generate_fibonacci_sequence(2, 0, "a")

    def test_if_no_parameters_are_passed_then_it_must_return_01(self):
        expected = [0, 1]
        actual = leonhard.generate_fibonacci_sequence()
        self.assertEqual(expected, actual)

    def test_if_number_of_terms_is_3_then_it_must_return_011(self):
        expected = [0, 1, 1]
        actual = leonhard.generate_fibonacci_sequence(3)
        self.assertEqual(expected, actual)

    def test_if_number_of_terms_is_8_then_it_must_return_011235813(self):
        expected = [0, 1, 1, 2, 3, 5, 8, 13]
        actual = leonhard.generate_fibonacci_sequence(8)
        self.assertEqual(expected, actual)

    def test_if_default_2_4_then_it_must_return_24(self):
        """
        No number of terms is given but first and second terms are provided
        :return:
        """
        expected = [2, 4]
        actual = leonhard.generate_fibonacci_sequence(first_term=2, second_term=4)
        self.assertEqual(expected, actual)

    def test_if_default_default_4_then_it_must_return_04(self):
        """
        No number of terms and first term given but second term is provided
        :return:
        """
        expected = [0, 4]
        actual = leonhard.generate_fibonacci_sequence(second_term=4)
        self.assertEqual(expected, actual)

    def test_if_default_1_default_then_it_must_return_11(self):
        """
        No number of terms and second term given but first term is provided
        :return:
        """
        expected = [1, 1]
        actual = leonhard.generate_fibonacci_sequence(first_term=1)
        self.assertEqual(expected, actual)

    def test_811_then_it_must_return_1123581321(self):
        """
        number_of_terms: 8
        first_term: 1
        second_term: 1
        :return:
        """
        expected = [1, 1, 2, 3, 5, 8, 13, 21]
        actual = leonhard.generate_fibonacci_sequence(8, 1, 1)
        self.assertEqual(expected, actual)

    def test_456_then_it_must_return_561117(self):
        """
        number_of_terms: 4
        first_term: 5
        second_term: 6
        :return:
        """
        expected = [5, 6, 11, 17]
        actual = leonhard.generate_fibonacci_sequence(4, 5, 6)
        self.assertEqual(expected, actual)


class TestIsPrime(unittest.TestCase):

    def test_if_negative_input_then_it_must_raise_value_error(self):
        with self.assertRaises(ValueError):
            leonhard.is_prime(-1)

    def test_if_1_then_it_must_return_false(self):
        self.assertFalse(leonhard.is_prime(1))

    def test_if_0_then_it_must_return_false(self):
        self.assertFalse(leonhard.is_prime(0))

    def test_if_input_is_string_then_it_must_raise_type_error(self):
        with self.assertRaises(TypeError):
            leonhard.is_prime("test")

    def test_if_2_then_it_must_return_true(self):
        self.assertTrue(leonhard.is_prime(2))

    def test_if_4_then_it_must_return_false(self):
        self.assertFalse(leonhard.is_prime(4))

    def test_if_7652413_then_it_must_return_true(self):
        self.assertTrue(leonhard.is_prime(7652413))

    def test_if_600851475143_then_it_must_return_false(self):
        self.assertFalse(leonhard.is_prime(600851475143))


if __name__ == '__main__':
    unittest.main()