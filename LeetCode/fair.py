def waysToMakeFair(nums):
    fair=0
    for i in range(len(nums)):
        even,odd=0,0
        arr = nums[:i] + nums[i+1:len(nums)]
        print(arr)
        for j in range(len(arr)):
            if j%2==0:
                even+=arr[j]
            if j%2!=0:
                odd+=arr[j]
        
        if even==odd:
            fair+=1
    return fair

print(waysToMakeFair([2,1,6,4]))