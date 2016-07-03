"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def find_pythagorean_triplet_summing_to(n):
    for i in range(1, n+1):
        for j in range(i, n+1):
            if i**2 + j**2 == (n - i - j)**2:
                return (i, j, (n - i - j))
    return None

def solution():
    return reduce(lambda x, y:x*y, find_pythagorean_triplet_summing_to(1000))
    pass

print solution()
