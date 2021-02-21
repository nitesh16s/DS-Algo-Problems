k = int(input())

m = int(input())

list1 = [2,5,4]
list2 = [3,7,8,9]
list3 = [5,5,7,8,9,10]

len_list = []
maxm = []

# len_list.append(len(list1))
# len_list.append(len(list2))

for i in range(len(list1)):
	for j in range(len(list2)):
		for k in range(len(list3)):
			x = int((list1[i]**2 + (list2[j])**2 + (list3[k])**2)%1000)
			maxm.append(x)

maxm.sort(reverse=True)
print(maxm[0])