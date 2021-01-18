def selectionSort(arr):
    """
    Selects the maximum element and swaps it with the iteration index
    """
    n = len(arr)
    for i in range(n):
        max = (arr[i],i)
        for j in range(i,n):
            if arr[j] > max[0]:
                max = (arr[j],j)
        #swap the max index with iteration index
        temp = arr[i]
        arr[i] = max[0]
        arr[max[1]] = temp

    print(str(arr))



arr = [2,5,-4,10,9]
selectionSort(arr)