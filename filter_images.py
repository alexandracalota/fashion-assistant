import os
import random
import shutil
from global_vars import *

final_image_count = 35000

def remove_photo_dirs(path, remove = False):
	dirs = {}
	count = {}

	for c in categories:
		dirs[c] = []
		count[c] = 0
	
	total_count = 0
	
	for dir in os.listdir(path + '/img'):
		found = False
		for c in categories:
			if c in dir:
				dirs[c].append(dir)
				for _ in os.listdir(path + '/img/' + dir):
					count[c] += 1
					total_count += 1
				found = True
				break
		if not found and os.path.isdir(path + '/img/' + dir):
			shutil.rmtree(path + '/img/' + dir)
	
	print(count)
	print(total_count)

	percentage = {}
	for k, v in count.items():
		percentage[k] = 1.0 * v / total_count * 100

	print(percentage)

	if remove:
		for object_type, dir_list in dirs.items():
			f = count[object_type] / len(dir_list)
			print(object_type + " " + str(count[object_type]) + " " + str(len(dir_list)) + " " \
				+ str(percentage[object_type]) + " f " + str(f))

			to_eliminate = len(dir_list) - 1.0 * percentage[object_type] * final_image_count / 100 / f

			print(to_eliminate)
			for _ in range(int(to_eliminate)):
				img_dir = dir_list.pop(random.randrange(len(dir_list)))
				shutil.rmtree(path + '/img/' + img_dir)

	for c in categories:
		dirs[c] = []
	
	total_count = 0
	for dir in os.listdir(path + '/img/'):
		for c in categories:
			if c in dir:
				dirs[c].append(dir)
				for _ in os.listdir(path + '/img/' + dir):
					total_count += 1
				break

	print(total_count)

	return dirs

def update_file(dirs, path, filename):
	input_file = open(path + filename + '.txt', "r")
	i = 0
	final_lines = []
	final_lines.append(0)

	for line in input_file.readlines():
		if i == 1:
			final_lines.append(line)
		i += 1
		for _, value in dirs.items():
			ok = False
			for v in value:
				if ('/' + v + '/') in line:
					if filename == 'list_category_img':
						words = line.split()
						
						final_lines.append(words[0])
					else:
						final_lines.append(line)

					ok = True
					break
			if ok:
				break

	final_lines[0] = str(len(final_lines) - 2) + '\n'

	input_file.close()

	output_file = open(path + filename + '_new.txt', "w")
	value = 0

	if filename == 'list_category_img':
		output_file.write(final_lines[0])
		output_file.write(final_lines[1])

		class_idx = {}
		for cat in categories:
			class_idx[cat] = value
			value += 1

		for idx in range(2, len(final_lines)):
			for key, value in class_idx.items():
				if key in final_lines[idx]:
					output_file.write(str(final_lines[idx]) + '               ' + str(value) + '\n')
					break
	else:
		for line in final_lines:
			output_file.write(str(line))

	output_file.close()

def update_attributes():
	
	return

if __name__ == '__main__':
	dirs = remove_photo_dirs('./Resources', False)

	# for key, value in dirs.items():
	# 	print(key + " " + str(value))
			
	# update_file(dirs, './Resources/Anno/', 'list_category_img')
	# update_file(dirs, './Resources/Anno/', 'list_landmarks')
	# update_file(dirs, './Resources/Anno/', 'list_bbox')
	update_file(dirs, './Resources/Anno/', 'list_attr_img')
	# update_attributes('./Resources/Anno/', 'list_attr_img', 'list_attr_cloth')
