from collections import deque
from functools import reduce

from leonhard.helpers import raise_if_not_positive_int


def get_factors_of_positive_integer(n):
    """
    Gets the factors of a positive integer n
    :param int n: number to get the factors of
    :return [int]: a unique list of factors of n arranged in ascending order
    """
    try:
        if n == 0:
            return [0]

        midpoint = int(n**0.5)
        list_of_factor_pairs = ([i, n//i] for i in range(1, midpoint+1) if n % i == 0)
        factors = sorted(list(set(reduce((lambda a, b: a+b), list_of_factor_pairs))))
        return factors
    except TypeError:
        raise TypeError("Input must be >= 0.")


def generate_fibonacci_sequence(number_of_terms=2, first_term=0, second_term=1):
    """
    Generates a Fibonacci sequence
    :param int number_of_terms: the number of terms to be generated including the first and second
    :param int first_term: first number in the sequence, must be >= 0
    :param int second_term: second number in the sequence, must be >= first_term
    :return [int]: Fibonacci sequence
    """

    try:
        if number_of_terms < 2:
            raise ValueError("Number of terms must be >= 2")
        if first_term < 0:
            raise ValueError("First term must be >= 0")
        if second_term < first_term:
            raise ValueError("Second term must be >= first term")

        sequence = [first_term, second_term]
        while len(sequence) != number_of_terms:
            next_number = sequence[-1] + sequence[-2]
            sequence.append(next_number)

        return sequence
    except TypeError:
        raise TypeError("Input parameters must be positive integers")


def is_prime(n):
    """
    Checks if the given number n is prime or not
    :param int n: positive number to be checked
    :return bool: returns true if prime, else false
    """

    try:
        if n < 0:
            raise ValueError("Input must be >= 0")
        if n == 0 or n == 1:
            return False

        factors = get_factors_of_positive_integer(n)
        if len(factors) > 2:
            return False
        else:
            return True
    except TypeError:
        raise TypeError("Input must be positive integers")


def is_pythagorean_triplet(a, b, c):
    """
    A Pythagorean triplet is a set of three natural numbers a < b < c for which:
    a^2 + b^2 = c^2
    Example:    3,4,5
                3^2 + 4^2 = 5^2
                9 + 16 = 25
    :param int a: first number
    :param int b: second number
    :param int c: third number
    :return bool: returns True if a,b, and c are triplets
    """

    try:
        if a < b < c:
            if (a**2 + b**2) == c**2:
                return True
            else:
                return False
        else:
            return False
    except TypeError:
        raise TypeError("Input must be positive integers")


def count_digits(n):
    """
    Returns the number of digits of a given positive integer
    :param int n: number to count the digits of
    :return int: number of digits
    """
    raise_if_not_positive_int(n)

    return len(str(n))



def generate_collatz_sequence(n, sequence):
    """
    A sequence defined by:
        n -> n/2 (n is even)
        n -> 3n + 1 (n is odd)
    :param int n: term
    :param list sequence: list that will contain the collatz sequence
    :return:
    """
    raise_if_not_positive_int(n)
    if n == 0:
        raise ValueError("N must be a positive integer")

    sequence.append(n)
    get_next = lambda x: int(x / 2) if x % 2 == 0 else (3 * x) + 1
    next_number = get_next(n)
    if next_number != 1:
        generate_collatz_sequence(next_number, sequence)
    else:
        sequence.append(1)

    return sequence



def generate_cyclic_permutation(n):
    """
    A permutation which shifts all elements of a set by a fixed offset, with the elements shifted off the end inserted
    back at the beginning

    Given 123, its cyclic permutations are: 123, 312, and 231
    :param int n: number to get the permutations
    :return [int]: list of cyclic permutations of n
    """
    raise_if_not_positive_int(n)

    deque_object = deque([char for char in str(n)])
    cyclic_permutations = []
    for i in range(len(deque_object)):
        cyclic_permutations.append(list(deque_object))
        deque_object.rotate(1)

    return [int("".join(p)) for p in cyclic_permutations]



def is_triangle_number(n):
    """
    A triangular number or triangle number counts objects arranged in an equilateral triangle.

    0, 1, 3, 6, 10, 15, 21 ... 210, 231, etc.

    Explanation of ((8 * n) + 1) ** 0.5) % 1 == 0
        * An integer x is triangular if and only if 8x + 1 is a square
        * We get the square root by using `** 0.5`
        * To check if it is a whole number, we use `% 1`

    :param int n: number to check if it is triangular or not
    :return bool: True if triangular, else False
    """
    raise_if_not_positive_int(n)

    if (((8 * n) + 1) ** 0.5) % 1 == 0:
        return True
    else:
        return False
