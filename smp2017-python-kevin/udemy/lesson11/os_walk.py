import os
import shutil

initialdir = '/home/fullbuster/'
print('initial directory is: '+initialdir)

print('Enter directory path')

finaldir = input()

directory = initialdir + finaldir

ch = 'n'

print('Wanna backup files?(y/n)')

ch = input()

print('\n')

for Foldername, Subfolders, Files in os.walk(directory):
	print('Folder is '+ Foldername)
	print('Sub folders in '+Foldername+' are: '+str(Subfolders))
	print('Files in '+Foldername+' are: '+str(Files) +'\n')
	if(ch.lower()=='y'):
		for File in Files:
			if(File.endswith('.py')):
				shutil.copy((os.path.join(Foldername,File)),(os.path.join(Foldername,File+'.back')))
