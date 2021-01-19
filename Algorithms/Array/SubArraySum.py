"""
input : array,size,sum
if array = [1,2,3,4,4,5]  size = 6    sum = 11
return [2,4] because 3+4+4 = 11
"""
def subArraySum(arr, n, s):
    # Your code here
    start = 0
    while start < n:
        end = start
        sum = 0
        if arr[start] == s:
            return [start, start]
        if arr[start] > s:
            start += 1
            continue
        for element in arr[start:n]:
            sum += element
            if sum == s:
                return [start, end]
            end += 1
        start += 1

    return [-1]

def main():
    array = [1, 2, 3, 4, 4, 5]
    size = 6
    sum = 11
    result = subArraySum(array,size,sum)
    print(result)

if __name__ == "__main__":
    main()