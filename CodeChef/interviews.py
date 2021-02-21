import math


def interviews(nums, N, K):
    totalSolved, maxSecondsTaken = 0, 0

    for num in nums:
        maxSecondsTaken = max(maxSecondsTaken, num)
        if num >= 0:
            totalSolved += 1

    if totalSolved < math.ceil(N/2):
        return 'Rejected'

    elif maxSecondsTaken > K:
        return 'Too Slow'

    elif totalSolved == N and maxSecondsTaken == 1:
        return 'Bot'

    else:
        return 'Accepted'


t = int(input())
for _ in range(t):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    print(interviews(scores, N, K))
