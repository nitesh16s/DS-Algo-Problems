from itertools import combinations


def teamNames(words, N):
    names = set()
    for i in range(N):
        for j in range(i+1, N):
            i_name, j_name = list(words[i]), list(words[j])
            names.add(''.join(i_name))
            names.add(''.join(j_name))

            # swap
            i_name[0], j_name[0] = j_name[0], i_name[0]
            names.add(''.join(i_name))
            names.add(''.join(j_name))

    names = combinations(names.difference(set(words)), 2)
    ans = 0
    for _ in names:
        ans += 1
    return 2*ans


t = int(input())
for _ in range(t):
    N = int(input())
    arr = list(map(str, input().split()))
    print(teamNames(arr, N))
