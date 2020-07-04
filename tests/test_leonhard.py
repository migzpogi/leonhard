import unittest
from leonhard import leonhard


class TestLeonhard(unittest.TestCase):

    def test_foo(self):
        self.assertEqual(1, leonhard.foo())


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


if __name__ == '__main__':
    unittest.main()