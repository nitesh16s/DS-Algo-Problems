def birthday(s, d, m):
    # Base case
	if len(s) == 1 and m == 1 and d == s[0]:
		return 1
	else:
		counts = 0
		for i in range(len(s)-m+1):
			if sum(s[i:i+m]) == d:
				print(s[i:i+m])
				counts+=1
		return counts

print(birthday([2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1], 18, 7))