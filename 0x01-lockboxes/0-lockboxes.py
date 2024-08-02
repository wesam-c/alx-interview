#!/usr/bin/python3
"""Solves the lock boxes puzzle."""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be unlocked.

    Parameters:
    boxes (List[List[int]]): A list of lists, where each sublist contains keys.

    Returns:
    bool: True if all boxes can be unlocked, otherwise False.
    """
    total_boxes = len(boxes)
    set_of_keys = [0]
    counter = 0
    index = 0

    while index < len(set_of_keys):
        set_key = set_of_keys[index]
        for key in boxes[set_key]:
            if 0 < key < total_boxes and key not in set_of_keys:
                set_of_keys.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1
