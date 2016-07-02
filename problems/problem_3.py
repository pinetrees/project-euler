"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from lib import get_prime_factors_of

def solution():
    prime_factors = get_prime_factors_of(600851475143)
    print prime_factors
    return max(prime_factors)

print solution()
