def reverse(arr):
    print("Before Reverse" + str(arr))
    l = 0
    h = len(arr) - 1
    while(l < h):
        templow = arr[l]
        arr[l] = arr[h]
        arr[h] = templow
        l += 1
        h -= 1

    print("After Reverse" + str(arr))

arr = [1,2,3,-2,5]
reverse(arr)