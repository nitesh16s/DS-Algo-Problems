from itertools import permutations


def teamNames(words, n):
    words = set(words)
    firstLetters = set()
    names = set()

    for word in words:
        firstLetters.add(word[0])

    if len(firstLetters) == 1:
        return 0

    for word in words:
        for first in firstLetters:
            name = list(word)
            name[0] = first
            name = ''.join(name)
            if name not in words:
                names.add(name)

    ans = 0
    names = permutations(names, 2)
    seen = {}
    
    for name in names:
        if name not in seen:
            name1, name2 = list(name[0]), list(name[1])
            name1[0], name2[0] = name2[0], name1[0]
            if ''.join(name1) in words and ''.join(name2) in words:
                ans += 1

    return ans


t = int(input())
for _ in range(t):
    N = int(input())
    arr = list(map(str, input().split()))
    print(teamNames(arr, N))
