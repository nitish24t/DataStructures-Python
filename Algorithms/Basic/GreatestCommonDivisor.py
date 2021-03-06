def findGCD(a, b):
    # method 2
    while b != 0:   # run till remainder is not zero
        t = a
        a = b
        b = t % b
        print(f"a={a}, b={b}, t={t}")
    return a        # return the divisor
res1 = findGCD(24, 248)
print(res1)


res2 = findGCD(248, 24)
print(res2)


# GCD (20,8)
# a   |   b   |   r
# 20      8       4
# 8       4       0
