#一些辅助操作
#文件的存储和读取

# NEED HELP: https://docs.python.org/3/tutorial/inputoutput.html
import os

#创建文件夹
def create_project_dir(directory):
	if not os.path.exists(directory):
		os.makedirs(directory)
#我们用两个文件夹
#一个queue.txt 用来记录等待被爬的网址
#一个crawled.txt 记录爬过了的网址
# TODO: 创建crawled.txt

def create_data_files(project_name,base_url):
	queue = os.path.join(project_name,'queue.txt')
	if not os.path.isfile(queue):
		write_file(queue,base_url)

	# Code in here

# 写入文件

def write_file(path,data):
	with open(path,'w') as f:
		f.write(data)

# TODO: txt文件中“添加”新的内容
def append_to_file(path,data):
	# Code in here and delete the "pass"
	pass


def delete_file_contents(path):
	open(path,'w').close()

# 读取文件内容
# 我们将url 存储为 set 类型（快速）
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