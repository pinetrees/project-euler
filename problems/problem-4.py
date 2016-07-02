"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindromic(number):
    snumber = str(number)
    half_size = len(snumber) / 2
    first_half = snumber[0:half_size]
    second_half = snumber[-1*half_size:]
    return first_half == second_half[::-1]

def solution():
    palindromes = []
    for i in range(100, 999):
        for j in range(100, 999):
            product = i * j
            if is_palindromic(product):
                palindromes.append(product)
    return max(palindromes)

print solution()
