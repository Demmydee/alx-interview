#!/usr/bin/python3
"""Change making module.
"""

def makeChange(coins, total):
    result = 0
    coins.sort()
    coins.reverse()
    num = 0
    count = 0
    while result != total:
        if total == 0:
            return(0)
            break
        if result + coins[num] <= total:
            result += coins[num]
            count += 1
        elif result + coins[num] > total:
            if num < len(coins)-1:
                num += 1
            else:
                return(-1)
                break
        if result == total:
            return(count)
