#!/usr/bin/python3
"""
A module for lockboxes.
"""


def canUnlockAll(boxes):
    """
    A method that determines if all boxes can be opened
    A key with the same number as a box opens that box
    All keys are assumed to be positive integers
    There can be keys that do not have boxes
    The first box is unlocked
    """
    n = len(boxes)
    unlocked_boxes = set([0])
    locked_boxes = set(boxes[0]).difference(set([0]))
    while len(locked_boxes) > 0:
        box_num = locked_boxes.pop()
        if not box_num or box_num < 0 or box_num >= n:
            continue
        if box_num not in unlocked_boxes:
            locked_boxes = locked_boxes.union(boxes[box_num])
            unlocked_boxes.add(box_num)
    return n == len(unlocked_boxes)
