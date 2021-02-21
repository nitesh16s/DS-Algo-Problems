original = open('myfile.txt')

stack = []

for line in original:
	stack.append(line.rstrip('\n'))
original.close()


output = open('myfile.txt', 'w')

while len(stack)!=0:
	output.write(stack.pop()+'\n')

output.close()