import traceback

def pdi(n):
    print(traceback.format_stack())
    if n==0:
        return
    print(n)
    pdi(n-1)
    print(n)

pdi(5)