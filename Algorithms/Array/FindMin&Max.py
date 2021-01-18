def findMinMax(arr):
    n = len(arr)
    min = max = arr[0]
    for i in range(0,n):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]

    return (min,max)


arr = [12,3,5,6,78,56]
result = findMinMax(arr)
print(result)