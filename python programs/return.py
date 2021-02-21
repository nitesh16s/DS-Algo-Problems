arr = [1,2,3,4,5,6,7,8]

n = len(arr)

count = 0

for i in range(1, n):
	start = i
	end = n

	summ = arr[i] + arr[n-i-2]
	print(summ)

	print('before: ', start, end)

	while start<end:

		if summ == arr[n-i]:
			count+=1
			print('count: ', count)
			start+=1
			end-=1


		if summ < arr[n-i]:
			start+=start

		if summ > arr[n-i]:
			end -= 1

		start+=1
		end-=1

		print('after: ', start, end)