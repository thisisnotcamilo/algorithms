#! /usr/bin/python3

# O(n)
def search(arr, n):
    for i in arr:
        if i == n:
            return print(True)
    return print(False)

a = [0,1,2,3,4,5,6,7]

search(a, 9)
