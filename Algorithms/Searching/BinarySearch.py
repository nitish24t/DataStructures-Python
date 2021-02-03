"""
Binary search is suitable to search a sorted array by repetedly dividing the array by half.
"""

def BinarySearchIterative(A, key):
    n = len(A)
    low = 0
    high = n - 1

    while low <= high:
        mid = low + (high - low) // 2
        if key == A[mid]:
            return mid
        elif key < A[mid]:
            high = mid - 1
        elif key > A[mid]:
            low = mid + 1
    return -1


def BinarySearchRecursive(A, key, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        # print(mid,end=" ,")
        if A[mid] == key:
            return mid
        elif A[mid] < key:
            return BinarySearchRecursive(A, key, mid+1, high)
        elif A[mid] > key:
            return BinarySearchIterative(A, key, low, mid-1)
    else:
        return -1

#A = [1,4,5,7,9,12,14,16,19,22,41,43,48,51]
A = [1, 4, 5, 7, 9, 12]
finder = 9
index = BinarySearchIterative(A, finder)
index2 = BinarySearchRecursive(A,finder, 0, len(A)-1)
if index2 is not -1:
    print(index2)
else:
    print("Value not found in array")