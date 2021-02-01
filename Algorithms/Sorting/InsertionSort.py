"""
Pseudo Code
arr(size=n)
for i=1 to n-1:
    j = i - 1
    current = arr[i]
    while j >= 0 and current < arr[j]:
        then increment arr[j] to arr[j+1]
        j = j - 1
    arr[j + 1] = current

"""

def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        current = arr[i]
        j = i - 1
        #increments all the elements > arr[i] by one index
        while j >= 0 and arr[j] > current:
            arr[j+1] = arr[j]
            j -= 1
        arr[j + 1] = current

    print(arr)


arr = [4,2,5,1,6,1]
arr2 = [1]
insertionSort(arr)
insertionSort(arr2)