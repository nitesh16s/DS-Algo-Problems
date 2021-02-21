import time

start = time.time()

array = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57, 60, 63, 66]

products = []

for index in range(0, len(array)):
	for jindx in range(index+1, len(array)):
		for kindex in range(jindx+1, len(array)):
			product = array[index]*array[jindx]*array[kindex]
			products.append(product)

print(max(products))

end = time.time()

print(end-start)