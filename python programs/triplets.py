a = [1,2,3,4,5,6]
res = []
n = len(a)
count = 0

for i in range(0, n):
	for j in range(i, n):
		summ = a[i] + a[j]
		res.append(summ)
		if i==j:
			res.pop()


for i in range(0,n):
	for j in range(i,n):
		if res[i] == a[i]+a[j]:
			count+=1

print(count)