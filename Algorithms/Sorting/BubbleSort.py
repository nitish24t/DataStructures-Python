"""
Algorithm
BubbleSort A
for i in range(0,n)
    for j in range(0,n-1)
        if A[i+1] < A[i]
            swap(A[i+1],A[i])
"""

def bubbleSort(A):
    n = len(A)
    for i in range(0,n):
        for j in range(0,n-1):
            if A[j+1] < A[j]:
                A[j+1],A[j] = A[j],A[j+1]
    print(A)

bubbleSort([4,1,7,4,8,13,0])


