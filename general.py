import os

def create_project_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)

def create_data_files(project_name,base_url):
	def initfile(name, init_context=''):
		file = os.path.join(project_name,name)
		if not os.path.isfile(file):
			write_file(file,init_context)

	initfile('queue.txt',base_url)
	initfile('crawled.txt')
	initfile('finish.txt')


def write_file(path,data):
	with open(path,'w') as f:
		f.write(data)

def append_to_file(path,data):
	with open(path,'a') as file:
		file.write(data + '\n')

def delete_file_contents(path):
	open(path,'w').close()

def file_to_set(file_name):
	result = set()
	with open(file_name,'rt') as f:
		for line in f:
			result.add(line.replace('\n',''))
	return result

def set_to_file(links,file_name):
	with open(file_name,'w') as f:
		for l in sorted(links):
			f.write(l+'\n')