import os
import shutil
from time import sleep

my_file = open('python1.txt', 'a+')
i=0

for file in os.listdir('/home/nitesh2/recovered_py'):

	print(i)
	i+=1

	name = os.path.join('/home/nitesh2/recovered_py', file)

	file_name = open(name, 'rb')

	lines = file_name.readlines()

	for line in lines:
		line = str(line)
		# line = str(line)
		# print(line)
		# sleep(0.1)
		if 'CASCADE' in line:
			print(line)
			# sleep(0.25)
			my_file.write(line)
			my_file.write('\r\n')



	# print('Number of lines in the file' + str(file_name) + 'is :', x)

	# print(lines)

	# # for line in lines:
	# # 	print(file_name)
	# 	# if 'import django' in line:
	# 		# print('True')