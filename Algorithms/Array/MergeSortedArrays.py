def mergeSortedArrays(arr1,arr2):
    len1,len2 = len(arr1), len(arr2)
    length = len1 + len2
    arr = [None]*length
    i=j=0
    counter = 0
    while counter < length:
        if i < len1 and j < len2:
            if arr1[i] > arr2[j]:
                arr[counter] = arr2[j]
                j += 1
            else:
                arr[counter] = arr1[i]
                i += 1
        elif i < len1:
            arr[counter] = arr1[i]
            i += 1
        elif j < len2:
            arr[counter] = arr2[j]
            j += 1
        counter += 1
    print(arr)

def mergeSortedArrays2(arr1,arr2):
    """with duplicates"""
    m,n = len(arr1),len(arr2)
    sortedMerge = []
    i = j = 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            sortedMerge.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            sortedMerge.append(arr2[j])
            j += 1
        elif arr1[i] == arr2[j]:
            sortedMerge.append(arr1[i])
            i += 1
    # Empty remaining elements
    while i < m:
        sortedMerge.append(arr1[i])
        i += 1
    while j < n:
        sortedMerge.append(arr2[j])
        j += 1
    print(sortedMerge)


def mergeSortedArrays3(arr1,arr2):
    """without duplicates"""
    m,n = len(arr1),len(arr2)
    sortedMerge = []
    i = j = 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            sortedMerge.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            sortedMerge.append(arr2[j])
            j += 1
        elif arr1[i] == arr2[j]:
            sortedMerge.append(arr1[i])
            i += 1
            j += 1
    # Empty remaining elements
    while i < m:
        sortedMerge.append(arr1[i])
        i += 1
    while j < n:
        sortedMerge.append(arr2[j])
        j += 1
    print(sortedMerge)


def mergeSortedArrays3(arr1,arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    n = l1 + l2
    A = [None]*n
    i = j = 0

    while i + j < n:
        if j == l2 or (i < l1 and arr1[i] < arr2[j]):
            A[i+j] = arr1[i]
            i += 1
        else:
            A[i+j] = arr2[j]
            j += 1

    print(A)


arr1 = [1, 2, 4, 5, 6]
arr2 = [2, 3, 5, 7]
mergeSortedArrays(arr1,arr2)
mergeSortedArrays2(arr1,arr2)
mergeSortedArrays3(arr1,arr2)



