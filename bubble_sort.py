#! /bin/python3

# O(n^2)
def bubble_sort(arr):
    for j in range(0, len(arr)):
        for i in range(0, len(arr)-1):
            if arr[i] > arr[j]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

arr = [1,3,2,5,7,6,10, 4]

print(bubble_sort(arr))
