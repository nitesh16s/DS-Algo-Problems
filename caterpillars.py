'''
Sieve of Erastothenses
'''


def remainingLeaves(n, jumps):

    leaves, remainLeaves = [True]*(n+1), n

    for jump in jumps:
        if jump <= n and leaves[jump]:
            for leave in range(jump, n+1, jump):
                if leaves[leave]:
                    leaves[leave] = False
                    remainLeaves -= 1

    return remainLeaves


t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    jumps = list(map(int, input().split()))
    print(remainingLeaves(n, jumps))
