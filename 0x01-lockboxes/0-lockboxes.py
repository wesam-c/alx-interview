#!/usr/bin/python3
"""Solves the lock boxes puzzle """

def canUnlockAll(boxes):
    n = len(boxes)
    unlocked = set()
    unlocked.add(0)  # Start with box 0 unlocked
    keys = [0]  # List of keys to process, starting with box 0
    
    while keys:
        current_key = keys.pop()  # Get the next key to process
        for key in boxes[current_key]:  # Get the keys inside the current box
            if key not in unlocked:
                unlocked.add(key)
                keys.append(key)
    
    return len(unlocked) == n
