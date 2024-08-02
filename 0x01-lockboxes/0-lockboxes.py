#!/usr/bin/python3
"""Solves the lock boxes puzzle """


def canUnlockAll(boxes):
    """
    Determine if all boxes can be opened given a set of keys.

    Parameters:
    boxes (list of list of int): A list where each element is a list of keys found in the corresponding box.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)  # Total number of boxes
    unlocked = set()  # Set to keep track of opened boxes
    unlocked.add(0)  # Start with box 0 unlocked
    keys = [0]  # List of keys to process, starting with box 0
    
    while keys:
        current_key = keys.pop()  # Get the next key to process
        for key in boxes[current_key]:  # Get the keys inside the current box
            if key not in unlocked:
                unlocked.add(key)  # Mark the box as unlocked
                keys.append(key)  # Add the key to the list for further processing
    
    return len(unlocked) == n  # Check if all boxes have been unlocked
