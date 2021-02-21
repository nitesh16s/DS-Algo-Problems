def skmp(s,p):
	s = sorted(list(s))
	p = list(p)

	for i in range(len(p)):
		index = s.index(p[i])
		s.remove(s[index])

	index = 0

	for i in range(len(s)):
		if s[i] >= p[0]:
			index = i
			break

	s = s[0:index] + p + s[index:len(s)]

	return ''.join(s)

t = int(input())
for _ in range(t):
	s = str(input())
	p = str(input())
	print(skmp(s,p))