"""
Hackerrank
Input: A single line containing the space-separated integers.
Output: First, print the array using the numpy.zeros tool and then print the array with the numpy.ones tool.

"""

import numpy

#arr = raw_input().strip().split(' ')

def zerones(arr):
    my_array = numpy.array(arr, int)
    array_zeros = numpy.zeros(my_array,int)
    print(array_zeros)
    array_ones = numpy.ones(my_array, int)
    print(array_ones)

arr = [3,3,3]

zerones(arr)
