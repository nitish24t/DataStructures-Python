
def merge(arr1,arr2,arr):
    l1 = len(arr1)
    l2 = len(arr2)
    n = len(arr)
    i = j = 0

    while i + j < n:
        if j == l2 or (i < l1 and arr1[i] < arr2[j]):
            arr[i+j] = arr1[i]
            i += 1
        else:
            arr[i+j] = arr2[j]
            j += 1
    print(arr)


def mergeSort(arr):
    n = len(arr)
    if n < 2:
        return
    m = n // 2
    S1 = arr[:m]
    S2 = arr[m:]
    print(S1)
    print(S2)
    mergeSort(S1)
    mergeSort(S2)
    merge(S1,S2,arr)


arr = [12, 11, 13, 5, 6, 7,5,23]

mergeSort(arr)

print(arr)
