import os 
import shutil

for file in os.listdir('/home/nitesh2/recovered_pictures'):

	name = os.path.join('/home/nitesh2/recovered_pictures', file)

	if 5242880 < os.path.getsize(name):
		shutil.move(name, '/home/nitesh2/Pictures/5above')

	elif os.path.getsize(name) <=102400:
		shutil.move(name, '/home/nitesh2/Pictures/0to100kb')

	elif 1048576 < os.path.getsize(name) <= 2097152:
		shutil.move(name, '/home/nitesh2/Pictures/1to2')

	elif 1048576*2 < os.path.getsize(name) <= 1048576*3:
		shutil.move(name, '/home/nitesh2/Pictures/2to3')

	elif 1048576*3 < os.path.getsize(name) <= 1048576*5:
		shutil.move(name, '/home/nitesh2/Pictures/3to5')

	elif 102400 < os.path.getsize(name) <= 102400*2:
		shutil.move(name, '/home/nitesh2/Pictures/100to200kb')

	elif 102400*2 < os.path.getsize(name) <= 102400*5:
		shutil.move(name, '/home/nitesh2/Pictures/200to500kb')

	elif 512000 < os.path.getsize(name) <= 1024000:
		shutil.move(name, '/home/nitesh2/Pictures/500to1MB')