#!/usr/bin/python3
"""Solves the lock boxes puzzle """

def canUnlockAll(boxes):
    """
    take boxes
        created set of keys
            go to box0
                get all keys and add them setofkeys
            start opening boxes from setofkeys
                got to first key we have in setofkeys
                    go to the box coresponding to that key
                        and take the keys from it and add them to the setofkeys
                    keep looping through all setofkeys
            ignore keys that are more than number of boxes

            track opening of boxes by counter, if at end it = to length off boxes, it mean all boxes unlock
    
    """
    total_boxes = len(boxes)
    setofkeys = [0]
    counter = 0
    index = 0

    while index < len(setofkeys):
        setkey = setofkeys[index]
        for key in boxes[setkey]:
            if 0 < key < total_boxes and key not in setofkeys:
                setofkeys.append(key)
                counter += 1
        index += 1

    return counter == total_boxes - 1
