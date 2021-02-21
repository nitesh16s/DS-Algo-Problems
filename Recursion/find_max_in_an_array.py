def find_max_in_an_array(arr, idx):
    if idx == len(arr)-1:
        return arr[idx]
    misa = find_max_in_an_array(arr, idx+1)
    if misa > arr[idx]:
        return misa
    return arr[idx]


print(find_max_in_an_array([1, 2, 3, 4, 10, 3, 4, 2, 1], 0))
