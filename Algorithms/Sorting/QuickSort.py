"""
+++---+++ Partition Algorithm +++-----***
partition(A,start,end)
pivot = A[end]
p_index = start
i = 0

for i in range(start,end-1):
    if A[i] < pivot:
        swap(A[i],A[p_index])
        p_index += 1

"""

def partition(A,start,end):
    pivot = A[end]
    p_index = start
    for i in range(start,end):
        if A[i] < pivot:
            A[i],A[p_index] = A[p_index],A[i]
            p_index += 1
    A[p_index],A[end] = A[end],A[p_index]
    return p_index


# A = [6,2,10,9,5,0,8]
# p = partition(A,0,6)
# print(A)
# print(p)


def QuickSort(A,start,end):
    if start > end:
        return
    p = partition(A,start,end)
    QuickSort(A,start,p-1)
    QuickSort(A,p+1,end)


A = [6,2,9,5,0,8,5]
QuickSort(A,0,len(A)-1)
print(A)

