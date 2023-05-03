# lower value is inclusive, higher value is exclusive: have that in mind to avoid offset:
#
# [lo,high)
import math

# this only works if the array is sorted, so keep that in mind
# O(logN)
def binary_search(arr, n):
    lo = 0
    hi = len(arr)
    while (lo < hi):
        m = math.floor(lo + (hi-lo)/2)
        j = arr[m]
        if j == n:
            return print("found!")
        elif (j > n):
            hi = m
        else:
            lo = m+1
    return print("not found!")

arr = [1,2,3,4,5,6,7,8]

binary_search(arr, 4)
