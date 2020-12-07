def findGCD(a, b):
    # medified method 1 (no need of else)
    while (a < b):
        r = b % a
        if r == 0:
            return a
        b = a
        a = r

res1 = findGCD(36, 12624)
print(res1)