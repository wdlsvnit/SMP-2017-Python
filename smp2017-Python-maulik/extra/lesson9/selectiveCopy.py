#! python3
#Program walks through a folder tree and searches for files with given extension-
#and copies them into a new folder

import os,shutil

def copyFile(file):
    shutil.copy(file,newFolder)
    
def searchFile(folder,extension):
    for foldername,subfolders,filenames in os.walk(folder):
        for file in filenames:
            if file.endswith(extension):
                print("copying %s to %s...."%(os.path.join(foldername,file),newFolder))
                #copyFile(os.path.join(foldername,file))


def main():
    print("Enter search folder path :")
    folder=input()
    print("enter extension of files :")
    extension = input()
    print("Enter path of new folder :")
    global newFolder
    newFolder = input()
    
    if not os.path.isdir(newFolder):
        os.makedirs(newFolder)
        
    searchFile(folder,extension)

if __name__=="__main__":
    main()
                      
    
