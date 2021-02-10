def rotLeft(a, d):

    n = len(a)

    times = d % n

    for j in range(times):
        start = a[0]
        for i in range(1, n):
            a[i], a[i - 1] = a[i - 1], a[i]
        a[n - 1] = start

    return a

a = [1,2,3,4,5]

res = rotLeft(a,3)

print(res)