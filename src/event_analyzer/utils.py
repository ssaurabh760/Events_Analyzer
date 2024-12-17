#!/usr/bin/env python3
"""Utility functions for numerical operations."""

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_divisible_by(n: int, divisor: int) -> bool:
    """Check if a number is divisible by another number."""
    return n % divisor == 0