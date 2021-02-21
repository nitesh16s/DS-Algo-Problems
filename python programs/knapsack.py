n = int(input('Enter number of objects: '))
kanpsack = int(input('Enter weight of bag: '))

objects = []
profits = []
weights = []

best = []

for i in range(n):
	a = int(input('Enter profit of object ' + str(i+1) + ': '))
	b = int(input('Enter weight of object ' + str(i+1) + ': '))
	profits.append(a)
	weights.append(b)

print(profits, weights)


for i in range(n):
	for j in range(n):
		a = 