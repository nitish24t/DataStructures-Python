"""
GEEKS FOR GEEKS
Check if a key is present in every segment of size k in an array

arr[] = { 3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3}
key = 3
segment = 3
Output : Yes
There are 4 non-overlapping segments of size segment in the array, {3, 5, 2}, {4, 9, 3}, {1, 7, 3} and {11, 12, 3}. 3 is present all segments.
"""

def checkKeyAvailability(arr,key,segment):
    index = 0
    length = len(arr)
    while index < length:
        if key not in arr[index:index+segment]:
            return "NO"
        index += segment
    return "YES"


arr = [3, 5, 2, 4, 9, 3, 1, 7, 3, 11, 12, 3]
key = 3
segment = 3

result = checkKeyAvailability(arr,key,segment)

print(result)