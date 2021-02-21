def zigzag(n):
    if n == 0:
        return
    print('pre', n)
    zigzag(n-1)
    print('in', n)
    zigzag(n-1)
    print('post', n)


print(zigzag(3))
