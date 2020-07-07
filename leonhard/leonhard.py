from functools import reduce


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
