def staircase(n):
    for i in range(n):
        for j in range(n-i-1):
            print(' ', end='')
        for k in range(i+1):
            print('#', end='')
        print(end='\n')


if __name__ == '__main__':
    n = int(input())
    staircase(n)
