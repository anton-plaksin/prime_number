import sys
import os

# Add project root to sys.path so that prime_number module can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from check import is_prime


def test_negative_and_zero():
    # Negative numbers, zero and one are not prime
    for n in (-10, 0, 1):
        assert not is_prime(n)


def test_small_primes():
    # Test some small prime numbers
    for p in (2, 3, 5, 7, 11, 13, 17, 19):
        assert is_prime(p)


def test_small_non_primes():
    # Test some small composite numbers
    for n in (4, 6, 8, 10, 12, 14):
        assert not is_prime(n)


def test_large_prime():
    # Test a larger prime (10000th prime)
    assert is_prime(104729)


def test_large_non_prime():
    # Test a large composite number
    assert not is_prime(100000)
