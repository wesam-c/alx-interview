#!/usr/bin/python3
"""Writing a function for Pascal's Triangle"""

def pascal_triangle(n):
    """
    returns a lists of integers
    representing the Pascal’s triangle
    """
    if n <= 0:
        return[]
    
    traingle = []

    for i in range(n):
        row = [0] * (i + 1)

        #set the first and last elements in the row to 1
        row[0] = row[-1] = 1

        # the interior elements
        for j in range (1, len(row) -1):
            row[j] = traingle[i - 1][j - 1] + traingle[i - 1][j]

        # Add the row to the triangle
        traingle.append(row)

    # Return the completed triangle
    return traingle
