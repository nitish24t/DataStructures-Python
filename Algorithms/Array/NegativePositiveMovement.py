"""
Move all negative numbers to beginning and positive to end with constant extra space - geeksforgeeks
Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -12 -13 -5 -7 -3 -6 11 6 5
"""

def moveElements(arr):
    n = len(arr)
    j = 0
    for i in range(n,0):
        if (arr[i] > 0):
            arr[i],arr[j] = arr[j],arr[i]
            j = j + 1
    print(arr)


arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
moveElements(arr)