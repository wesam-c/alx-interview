#!/usr/bin/python3

"""
Module to calculate the fewest number of operations needed to achieve exactly n 'H' characters.

Functions:
    minOperations(n): Returns the minimum number of operations required.
"""

def minOperations(n):
    """
    Calculate the fewest number of operations needed to achieve exactly n 'H' characters.

    The function uses the factorization of n to determine the minimum number of operations
    needed to generate exactly n 'H' characters in the text editor. The operations available 
    are 'Copy All' and 'Paste'. 

    Parameters:
    n (int): The number of 'H' characters to be achieved.

    Returns:
    int: The minimum number of operations needed, or 0 if n is impossible to achieve.

    Example:
    >>> minOperations(9)
    6
    >>> minOperations(12)
    7
    """
    if n <= 1:
        return 0
    
    operations = 0
    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1
    
    return operations
