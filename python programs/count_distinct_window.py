def myfunc(arr, k):
	ans = []
	for i in range(len(arr)-k+1):
		window = arr[i:i+k]
		distinct = set()
		for num in window:
			distinct.add(num)
		ans.append(len(distinct))
	return ans

print(myfunc([1,2,1,3,4,2,3], 4))
print(myfunc([1,2,4,4],2))