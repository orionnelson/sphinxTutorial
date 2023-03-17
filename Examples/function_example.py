def factorial(n: int) -> int:
    """
    Calculate the factorial of a given number.

    :param n: The number to calculate the factorial of.
    :type n: int
    :return: The factorial of n.
    :rtype: int
    :raises ValueError: If n is negative.

    Example:
    >>> factorial(5)
    120
    """

    if n < 0:
        raise ValueError("n must be non-negative")

    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
