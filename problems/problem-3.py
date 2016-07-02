"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def get_prime_factors_of(value):
    factors = []
    i = 2
    while i <= value:
        if value % i == 0:
            factors.append(i)
            value = value / i
        else:
            i += 1
    return factors

def solution():
    prime_factors = get_prime_factors_of(600851475143)
    print prime_factors
    return max(prime_factors)

print solution()
