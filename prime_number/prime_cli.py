#!/usr/bin/env python3
"""
Command-line interface for primality check.
Usage:
    python prime_cli.py <number>
"""
import argparse
from prime_number import is_prime


def main():
    parser = argparse.ArgumentParser(description="Check if a given integer is prime.")
    parser.add_argument("number", type=int, help="Integer to check for primality")
    args = parser.parse_args()
    num = args.number
    if is_prime(num):
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")


if __name__ == "__main__":
    main()
