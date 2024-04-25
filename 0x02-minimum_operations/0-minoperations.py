#!/usr/bin/python3
""" Module for the 0. Minimum Operations task """


def minOperations(n):
    """ Function definition """
    prime_factors = []
    divisor = 2

    while divisor <= n:
        if n % divisor == 0:
            prime_factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    return sum(prime_factors)
