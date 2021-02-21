def printArrayReverseRecusively(arr, end):
    if end == -1:
        return
    print(arr[end])
    printArrayReverseRecusively(arr, end-1)

printArrayReverseRecusively([1,2,3,4,5,6,7], end=6)