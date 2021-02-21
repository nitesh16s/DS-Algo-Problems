def binary_search(arr, low, high, key):
    if high >= low:

        mid = low + (high-low)//2

        if arr[mid] == key:
            return mid

        elif key > arr[mid]:
            return binary_search(arr, mid+1, high, key)

        else:
            return binary_search(arr, low, mid-1, key)


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, high=10, key=5))
