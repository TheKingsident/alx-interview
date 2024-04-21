#!/usr/bin/env python3
"""
Module to find if all lockboxes can be opened
"""


def canUnlockAll(boxes):
    """
    Function that checks if all locked boxes can be opened
    """
    n = len(boxes)
    keys = set([0])
    boxesOpened = set()
    while keys:
        box = keys.pop()
        boxesOpened.add(box)
        keys.update(set(boxes[box]) - boxesOpened)
    return len(boxesOpened) == n
