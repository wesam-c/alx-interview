#!/usr/bin/python3

def min_operations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n
    'H' characters in a text file using a text editor that supports only two
    operations: Copy All and Paste.

    Parameters:
    n (int): The desired number of 'H' characters.

    Returns:
    int: The fewest number of operations needed. Returns 0 if n is less than 2.
    """
    if n < 2:
        return 0

    current_num_of_h = 1
    copied = 0
    num_of_operations = 0

    while current_num_of_h < n:
        if n % current_num_of_h == 0:
            copied = current_num_of_h
            num_of_operations += 1

        current_num_of_h += copied
        num_of_operations += 1

    return num_of_operations
