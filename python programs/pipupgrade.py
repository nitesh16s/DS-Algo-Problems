import pkg_resources
from subprocess import call

packages = [dist.project_name for dist in pkg_resources.working_set]
try:
	call("pip3 install --upgrade " + ' '.join(packages), shell=True)
except Error:
	print('')
	print('Error')
	print('')