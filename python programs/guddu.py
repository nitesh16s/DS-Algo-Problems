def gudduDate(n):
	if n <= 0:
		return False
	else:
		arr = []
		i=1
		while len(arr)!=n:
			a = [int(x) for x in str(i)]
			b = sum(a)
			i+=1
			if b%10==0:
				arr.append(a)

		ans = ''.join(map(str, arr[n-1]))

		return ans

t = int(input())
for _ in range(t):
	n = int(input())
	print(gudduDate(n))