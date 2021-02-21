def balloon(s):
	ans = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}

	for i in range(len(s)):
		if s[i] == 'b':
			ans[s[i]] += 1
		elif s[i] == 'a':
			ans[s[i]] += 1
		elif s[i] == 'l':
			ans[s[i]] += 1
		elif s[i] == 'o':
			ans[s[i]] += 1
		elif s[i] == 'n':
			ans[s[i]] += 1

	for key, value in ans.items():
		print(key,value)

print(balloon('balloonballoon'))