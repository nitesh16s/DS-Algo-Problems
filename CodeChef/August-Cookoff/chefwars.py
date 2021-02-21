def chefWar(h,p):
	while not p <= 0 or not h <= 0:
		if p > 0 and h <= 0:
			return 1
		if p <= 0 and h > 0:
			return 0
		else:
			h -= p
			p /= 2
	return h,p

t = int(input())
for _ in range(t):
	h, p = map(int, input().split())
	print(chefWar(h,p))