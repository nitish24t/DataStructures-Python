"""
K’th Smallest/Largest Element in Unsorted Array
"""

def findMin_and_Max(arr,k):
    n = len(arr)
    for i in range(k):
        min_index = i
        for j in range(i,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index],arr[i] = arr[i],arr[min_index]

    for i in range(k):
        max_index = i
        for j in range(i,n):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[max_index],arr[i] = arr[i],arr[max_index]

    print(arr)

    return (arr[k-1],arr[-k])




arr = [1,30,2,41,5,9,60]
result = findMin_and_Max(arr,2)

print(result)
