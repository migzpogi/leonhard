from functools import reduce


def foo():
    return 1


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