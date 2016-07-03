"""
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(start, end):
    return sum(map(lambda x: x**2, range(start, end+1)))

def square_of_sum(start, end):
    return sum(range(start, end+1))**2

def solution():
    return square_of_sum(1, 100) - sum_of_squares(1, 100)

print solution()
