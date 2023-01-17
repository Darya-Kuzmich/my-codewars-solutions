# DESCRIPTION
# Write a program that will calculate the number of trailing zeros in
# a factorial of a given number.
#
# N! = 1 * 2 * 3 *  ... * N
#
# Be careful 1000! has 2568 digits...
#
# For more info, see: http://mathworld.wolfram.com/Factorial.html
#
# Examples
# zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero
#
# zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
# Hint: You're not meant to calculate the factorial. Find another way
# to find the number of zeros.

from math import log, floor, pow


def zeros(n: int) -> int:
    if n == 0:
        return 0
    k_max = floor(log(n, 5))
    zeros_count = 0
    for k in range(1, k_max+1):
        zeros_count += floor(n / pow(5, k))
    return zeros_count


if __name__ == '__main__':
    print(zeros(0))
    print(zeros(6))
    print(zeros(12))
    print(zeros(30))
