"""
a = 2,4,5,7
b = 1,2, 3 , 6

"""

# def mergeSortedArrays(arr1,arr2):
#     for i in range(len(arr1)):
#         key = arr1[i]
#         j = len(arr2)-1
#         while j >= 0 and arr2[j] > key:
#             arr2[j+1] = arr2[j]
#             j -= 1
#         arr2[j] = key
#
#     print(arr2)

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


a = [2,4,4,5,7]
b = [1,3,6]
mergeSortedArrays(a,b)



