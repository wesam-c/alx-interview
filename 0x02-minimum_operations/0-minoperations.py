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
    min_operations = 0
    char_length = 1
    clipboard = 0

    if n <= 1:
        return 0

    while char_length < n:
        if n % char_length == 0:
            clipboard = char_length
            min_operations += 1

        char_length += clipboard
        min_operations += 1
    
    return min_operations
