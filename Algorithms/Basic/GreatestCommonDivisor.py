def findGCD(a, b):
    print("inside GCD function")
    print("a: " + str(a) + " b: " + str(b))
    while (a < b):
        #print("a: " + str(a) + " b: " + str(b))
        r = b % a
        #print("r: " + str(r))
        if r == 0:
            return a
        else:
            b = a
            a = r



res1 = findGCD(36, 12624)
print(res1)