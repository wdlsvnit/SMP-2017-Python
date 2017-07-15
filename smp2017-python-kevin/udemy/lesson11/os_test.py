import os

print('Enter directory path')

directory = input()

os.chdir(directory)

for File in os.listdir():
	if File.endswith('.mkv'):
		os.unlink(File)
