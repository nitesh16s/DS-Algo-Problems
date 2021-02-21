def printArrayRecursively(arr, start):
    if start+1 > len(arr):
        return
    print(arr[start])
    printArrayRecursively(arr, start+1)

printArrayRecursively([1, 2, 3, 4, 5, 6], 0)
