def maxfun(arr, N):
    maxm = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                summ = abs(arr[i] - arr[j]) + \
                    abs(arr[j] - arr[k]) + abs(arr[k] - arr[i])
                maxm = max(maxm, summ)
    return maxm


t = int(input())
for _ in range(t):
    N = int(input())
    arr = list(map(int, input().split()))
    print(maxfun(arr, N))
