def isAnagram(a, b):
    countA, countB = {}, {}

    for s in a:
        try:
            countA[s] += 1
        except:
            countA[s] = 1

    for s in b:
        try:
            countB[s] += 1
        except:
            countB[s] = 1

    print(countA, countB)

    return 'YES' if countA == countB else 'NO'

 
print(isAnagram(a='b', b='d'))
