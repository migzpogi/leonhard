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


class TestIsPythagoreanTriplet(unittest.TestCase):

    def test_if_input_are_letters_then_it_must_raise_a_type_error(self):
        with self.assertRaises(TypeError):
            leonhard.is_pythagorean_triplet('a', 'b', 'c')

    def test_if_input_are_not_a_less_b_less_c_then_it_must_return_false(self):
        self.assertFalse(leonhard.is_pythagorean_triplet(3, 2, 1))

    def test_if_input_is_345_then_it_must_return_true(self):
        self.assertTrue(leonhard.is_pythagorean_triplet(3, 4, 5))

    def test_if_input_is_6810_then_it_must_return_true(self):
        self.assertTrue(leonhard.is_pythagorean_triplet(6, 8, 10))

    def test_if_input_is_17144145_then_it_must_return_true(self):
        self.assertTrue(leonhard.is_pythagorean_triplet(17, 144, 145))

    def test_if_input_is_123_then_it_must_return_false(self):
        self.assertFalse(leonhard.is_pythagorean_triplet(1, 2, 3))


class TestCountDigits(unittest.TestCase):

    def test_if_input_are_letters_then_it_must_raise_a_type_error(self):
        with self.assertRaises(TypeError):
            leonhard.count_digits('a')

    def test_if_input_is_less_than_0_then_it_must_raise_a_value_error(self):
        with self.assertRaises(ValueError):
            leonhard.count_digits(-1)

    def test_if_input_is_123_then_it_must_return_3(self):
        self.assertEqual(leonhard.count_digits(123), 3)

    def test_if_input_is_123456789_then_it_must_return_9(self):
        self.assertEqual(leonhard.count_digits(123456789), 9)

    def test_if_input_is_0_then_it_must_return_1(self):
        self.assertEqual(leonhard.count_digits(0), 1)


class TestCollatzSequence(unittest.TestCase):

    def test_if_input_is_0_then_it_must_raise_a_value_error(self):
        with self.assertRaises(ValueError):
            leonhard.generate_collatz_sequence(0, [])

    def test_if_input_is_neg_one_then_it_must_raise_a_value_error(self):
        with self.assertRaises(ValueError):
            leonhard.generate_collatz_sequence(-1, [])

    def test_if_input_is_letter_then_it_must_raise_a_type_error(self):
        with self.assertRaises(TypeError):
            leonhard.generate_collatz_sequence('a', [])

    def test_if_input_is_13_then_it_must_generate_1340(self):
        """
        Must generate [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        :return:
        """
        expected = [13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
        actual = leonhard.generate_collatz_sequence(13, [])
        self.assertEqual(expected, actual)

    def test_if_input_is_837799_then_it_must_generate_(self):
        """
        Must generate [837799, 2513398, 1256699...]
        :return:
        """
        expected = [837799, 2513398, 1256699, 3770098, 1885049, 5655148, 2827574, 1413787, 4241362, 2120681, 6362044,
                    3181022, 1590511, 4771534, 2385767, 7157302, 3578651, 10735954, 5367977, 16103932, 8051966, 4025983,
                    12077950, 6038975, 18116926, 9058463, 27175390, 13587695, 40763086, 20381543, 61144630, 30572315,
                    91716946, 45858473, 137575420, 68787710, 34393855, 103181566, 51590783, 154772350, 77386175,
                    232158526, 116079263, 348237790, 174118895, 522356686, 261178343, 783535030, 391767515, 1175302546,
                    587651273, 1762953820, 881476910, 440738455, 1322215366, 661107683, 1983323050, 991661525,
                    2974984576, 1487492288, 743746144, 371873072, 185936536, 92968268, 46484134, 23242067, 69726202,
                    34863101, 104589304, 52294652, 26147326, 13073663, 39220990, 19610495, 58831486, 29415743, 88247230,
                    44123615, 132370846, 66185423, 198556270, 99278135, 297834406, 148917203, 446751610, 223375805,
                    670127416, 335063708, 167531854, 83765927, 251297782, 125648891, 376946674, 188473337, 565420012,
                    282710006, 141355003, 424065010, 212032505, 636097516, 318048758, 159024379, 477073138, 238536569,
                    715609708, 357804854, 178902427, 536707282, 268353641, 805060924, 402530462, 201265231, 603795694,
                    301897847, 905693542, 452846771, 1358540314, 679270157, 2037810472, 1018905236, 509452618, 254726309,
                    764178928, 382089464, 191044732, 95522366, 47761183, 143283550, 71641775, 214925326, 107462663,
                    322387990, 161193995, 483581986, 241790993, 725372980, 362686490, 181343245, 544029736, 272014868,
                    136007434, 68003717, 204011152, 102005576, 51002788, 25501394, 12750697, 38252092, 19126046, 9563023,
                    28689070, 14344535, 43033606, 21516803, 64550410, 32275205, 96825616, 48412808, 24206404, 12103202,
                    6051601, 18154804, 9077402, 4538701, 13616104, 6808052, 3404026, 1702013, 5106040, 2553020, 1276510,
                    638255, 1914766, 957383, 2872150, 1436075, 4308226, 2154113, 6462340, 3231170, 1615585, 4846756,
                    2423378, 1211689, 3635068, 1817534, 908767, 2726302, 1363151, 4089454, 2044727, 6134182, 3067091,
                    9201274, 4600637, 13801912, 6900956, 3450478, 1725239, 5175718, 2587859, 7763578, 3881789, 11645368,
                    5822684, 2911342, 1455671, 4367014, 2183507, 6550522, 3275261, 9825784, 4912892, 2456446, 1228223,
                    3684670, 1842335, 5527006, 2763503, 8290510, 4145255, 12435766, 6217883, 18653650, 9326825, 27980476,
                    13990238, 6995119, 20985358, 10492679, 31478038, 15739019, 47217058, 23608529, 70825588, 35412794,
                    17706397, 53119192, 26559596, 13279798, 6639899, 19919698, 9959849, 29879548, 14939774, 7469887,
                    22409662, 11204831, 33614494, 16807247, 50421742, 25210871, 75632614, 37816307, 113448922, 56724461,
                    170173384, 85086692, 42543346, 21271673, 63815020, 31907510, 15953755, 47861266, 23930633, 71791900,
                    35895950, 17947975, 53843926, 26921963, 80765890, 40382945, 121148836, 60574418, 30287209, 90861628,
                    45430814, 22715407, 68146222, 34073111, 102219334, 51109667, 153329002, 76664501, 229993504,
                    114996752, 57498376, 28749188, 14374594, 7187297, 21561892, 10780946, 5390473, 16171420, 8085710,
                    4042855, 12128566, 6064283, 18192850, 9096425, 27289276, 13644638, 6822319, 20466958, 10233479,
                    30700438, 15350219, 46050658, 23025329, 69075988, 34537994, 17268997, 51806992, 25903496, 12951748,
                    6475874, 3237937, 9713812, 4856906, 2428453, 7285360, 3642680, 1821340, 910670, 455335, 1366006,
                    683003, 2049010, 1024505, 3073516, 1536758, 768379, 2305138, 1152569, 3457708, 1728854, 864427,
                    2593282, 1296641, 3889924, 1944962, 972481, 2917444, 1458722, 729361, 2188084, 1094042, 547021,
                    1641064, 820532, 410266, 205133, 615400, 307700, 153850, 76925, 230776, 115388, 57694, 28847, 86542,
                    43271, 129814, 64907, 194722, 97361, 292084, 146042, 73021, 219064, 109532, 54766, 27383, 82150,
                    41075, 123226, 61613, 184840, 92420, 46210, 23105, 69316, 34658, 17329, 51988, 25994, 12997, 38992,
                    19496, 9748, 4874, 2437, 7312, 3656, 1828, 914, 457, 1372, 686, 343, 1030, 515, 1546, 773, 2320,
                    1160, 580, 290, 145, 436, 218, 109, 328, 164, 82, 41, 124, 62, 31, 94, 47, 142, 71, 214, 107, 322,
                    161, 484, 242, 121, 364, 182, 91, 274, 137, 412, 206, 103, 310, 155, 466, 233, 700, 350, 175, 526,
                    263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283,
                    850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822,
                    911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650,
                    325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2,
                    1]
        actual = leonhard.generate_collatz_sequence(837799, [])
        self.assertEqual(expected, actual)


class TestCyclicPermutation(unittest.TestCase):

    def test_if_input_are_letters_then_it_must_raise_a_type_error(self):
        with self.assertRaises(TypeError):
            leonhard.generate_cyclic_permutation('a')

    def test_if_input_is_less_than_0_then_it_must_raise_a_value_error(self):
        with self.assertRaises(ValueError):
            leonhard.generate_cyclic_permutation(-1)

    def test_if_input_is_123_then_it_must_return_valid(self):
        expected = [123, 312, 231]
        actual = leonhard.generate_cyclic_permutation(123)
        self.assertEqual(expected, actual)

    def test_if_input_is_1_then_it_must_return_valid(self):
        expected = [1]
        actual = leonhard.generate_cyclic_permutation(1)
        self.assertEqual(expected, actual)

    def test_if_input_is_0_then_it_must_return_valid(self):
        expected = [0]
        actual = leonhard.generate_cyclic_permutation(0)
        self.assertEqual(expected, actual)


class TestIsTriangleNumber(unittest.TestCase):

    def test_if_input_is_less_than_0_then_it_must_raise_a_value_error(self):
        with self.assertRaises(ValueError):
            leonhard.is_triangle_number(-1)

    def test_if_input_are_letters_then_it_must_raise_a_type_error(self):
        with self.assertRaises(TypeError):
            leonhard.is_triangle_number('a')

    def test_if_input_is_3_then_it_must_return_true(self):
        self.assertTrue(leonhard.is_triangle_number(3))

    def test_if_input_is_4_then_it_must_return_false(self):
        self.assertFalse(leonhard.is_triangle_number(4))

    def test_if_input_is_0_then_it_must_return_true(self):
        self.assertTrue(leonhard.is_triangle_number(0))


if __name__ == '__main__':
    unittest.main()