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
	file = open(path,'w')
	file.write(data)
	file.close()

def append_to_file(path,data):
	file = open(path,'a')
	file.write(data + '\n')
	file = close()

def delete_file_contents(path):
	open(path,'w').close()

def file_to_set(file_name):
	result = set()
	file = open(file_name,'rt')
	for line in file:
		result.add(line.replace('\n',''))
	file.close()
	return result

def set_to_file(links,file_name):
	file = open(file_name,'w')
	for l in sorted(links):
		file.write(l+'\n')
	file.close()