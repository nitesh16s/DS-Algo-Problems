def highestDivisor(N):
    for i in range(10, 0, -1):
        if N%i==0:
            return i

N = int(input())
print(highestDivisor(N))