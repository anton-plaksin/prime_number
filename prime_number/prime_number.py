"""
Module providing primality test function.
"""

def is_prime(n: int) -> bool:
    """
    Checks whether a number is prime.

    :param n: integer to check for primality
    :return: True if the number is prime, False otherwise
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
