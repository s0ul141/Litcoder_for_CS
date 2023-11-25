# -*- coding: utf-8 -*-
"""Cookies

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b3bN-V-Vfhn0q4t72EeU4SVjzU5IcxUL
"""

import heapq

def minSteps(target, candies):


    heap = candies[:]
    heapq.heapify(heap)
    target = int(target)


    steps = 0


    while heap[0] < target:
        # Get the two least sweet candies
        leastSweet = heapq.heappop(heap)
        secondLeastSweet = heapq.heappop(heap)


        newSweetness = leastSweet + 2 * secondLeastSweet


        heapq.heappush(heap, newSweetness)

        steps += 1

    return steps


inputVal1 = input()
inputVal2 = input()

array1 = inputVal2.split()
array1 = [int(x) for x in array1]
array1.sort()
outputVal = minSteps(inputVal1, array1)
print(outputVal)