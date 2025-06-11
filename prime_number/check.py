#!/usr/bin/env python3
"""
Script to check if a number is prime.
Usage:
    python prime_number.py <number>
"""
import argparse


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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Check if a given integer is prime."
    )
    parser.add_argument(
        "number",
        type=int,
        help="Integer to check for primality"
    )
    args = parser.parse_args()
    num = args.number
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")
