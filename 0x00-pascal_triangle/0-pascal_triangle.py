#!/usr/bin/python3
"""Pascal's Triangle"""


def pascal_triangle(n):
    """
    A function that returns a list of lists of integers representing the
    Pascal's triangle of n
       . Returns an empty list if n <= 0
       . Assumes n will always be an integer
    """
    pasc_tri = []

    if n <= 0:
        return []

    for i in range(n):
        if (i == 0):
            pasc_tri.append([1])
        else:
            row = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    row.append(1)
                else:
                    row.append(pasc_tri[i - 1][j - 1] +
                                   pasc_tri[i - 1][j])

            pasc_tri.append(row)

    return (pasc_tri)
