def amount(a, b):
    if a%5 != 0:
        return f'{b:.2f}'
    if b-(a+0.5) < 0:
        return f'{b:.2f}'
    else:
        return f'{b-(a+0.5):.2f}'

withdraw, available = map(float, input().split())
print(amount(withdraw, available))