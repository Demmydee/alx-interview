#!/usr/bin/python3
"""
    Minimum operations task
"""


def minOperations(n):
    if n <= 1:
        return(0)
    copy = 1
    x = 1
    op_count = 0
    while x < n:
        x += copy
        op_count += 1
        if n % copy == 0:
            copy = x
            op_count += 1

    return(op_count)
