"""
Sort an array of 0s, 1s and 2s
"""

def sortArray(arr):
    low = mid = 0
    high = len(arr)-1
    while mid <= high:
        if arr[mid] == 2:
            arr[high],arr[mid] = arr[mid],arr[high]
            high -= 1
        if arr[mid] == 1:
            mid += 1
        if arr[mid] == 0:
            arr[mid],arr[low] = arr[low],arr[mid]
            mid += 1
            low += 1
    return arr





arr = [0,1,0,1,2,0,1,2,2]
result = sortArray(arr)
[print(f,end="  ") for f in result]