"""
Move all negative numbers to beginning and positive to end with constant extra space - geeksforgeeks
Input: 12, 11, -13, -5, 6, -7, 5, -3, -6
Output: -13, -5, -7, -3, -6, 12, 5, 11, 6

"""

def moveElements(arr):
    n = len(arr)
    j = 0
    for i in range(0,n):
        if (arr[i] < 0):
            arr[i],arr[j] = arr[j],arr[i]
            j = j + 1
    print(arr)


arr = [12, 11, -13, -5, 6, -7, 5, -3, -6]
moveElements(arr)