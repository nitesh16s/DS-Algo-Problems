def towerOfHanoi(n, A, B, C):
    if n == 0:
        return
    towerOfHanoi(n-1, A, C, B)
    print(n, A + 'to' + B)
    towerOfHanoi(n-1, C, B, A)


A = 'A'
B = 'B'
C = 'C'
towerOfHanoi(4, A, B, C)