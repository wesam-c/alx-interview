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

    num_operations = 0
    current = n

    # Iterate over possible divisors
    for i in range(2, int(n**0.5) + 1):
        while current % i == 0:
            num_operations += i
            current //= i

    # If there is any prime factor greater than sqrt(n)
    if current > 1:
        num_operations += current

    return num_operations
