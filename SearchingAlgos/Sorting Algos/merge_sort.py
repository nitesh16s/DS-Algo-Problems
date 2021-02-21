'''
Merge Sort:
    Divide and Conquer Algorithm
'''

def mergeSort(arr):
    if len(arr) > 1:

        # find the mid of the array
        mid = len(arr)//2

        # dividing the arr