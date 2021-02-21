def findPairs(x, y, z):
    if x+y == z:
        return 'YES'
    elif x+z == y:
        return 'YES'
    elif y+z == x:
        return 'YES'
    else:
        return 'NO'


t = int(input())
for i in range(t):
    x, y, z = map(int, input().split())
    print(findPairs(x, y, z))
