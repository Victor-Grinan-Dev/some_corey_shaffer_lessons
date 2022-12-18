"""Return count of bits does a binary representation of a numbers does"""


def countBits(n):
    n = str(bin(n))

    bits = 0
    for char in n:
        if char == "1":
            bits += 1
    return bits


"""The objective is to return all pairs of integers from a given array of integers that have a difference of 2.
The result array should be sorted in ascending order of values.
Assume there are no duplicate integers in the array. The order of the integers in the input array should not matter."""


def twos_difference(lst):
    pairs = len(lst)/2

    