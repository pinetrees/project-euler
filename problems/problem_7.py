"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""
from lib import is_prime

def get_nth_prime(n):
    i = 0
    j = 1
    while i <= n:
        j += 1
        if is_prime(j):
            i += 1
    return j

def solution():
    return get_nth_prime(10000)

print solution()

