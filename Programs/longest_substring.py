def longest(s):
    arr = []
    n = len(s)
    for i in range(n):
        fix = s[i]
        for j in range(i+1, n):
            print(fix, s[j])

print(longest('abcdef'))