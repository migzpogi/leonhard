def raise_if_not_positive_int(n):
    """
    Raises a ValueError if n is not a positive integer
    Raises a TypeError if n is not an integer
    :param n: value provided
    :return:
    """
    try:
        if n < 0:
            raise ValueError("N must be a positive integer")
    except TypeError:
        raise TypeError("Input must be positive integers.")
