def oneCharacter(arr):
	if len(arr)<2:
		return False:
	else:
		count=0
		for i in range(len(arr)-1):
			a = list(arr[i])
			for j in range(i+1, len(arr)):
				b = list(arr[j])
				