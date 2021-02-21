def minOperations(nums):
    odds, evens = 0, 0
    for num in nums:
        if num % 2 == 0:
            evens += 1
        else:
            odds += 1

    return min(odds, evens)


t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    print(minOperations(arr))
