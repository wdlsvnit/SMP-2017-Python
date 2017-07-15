#! python3
#To delete files in a folder tree with size more than 100MB

import os

def delFiles(folder):
    for foldernames,subfolders,filenames in os.walk(folder):
        for file in filenames:
            file = os.path.join(foldernames,file)
            if os.path.getsize(file) > 10**8: #greater than 100MB == 10^8
                print("deleting file %s ...."%(file))
                #os.unlink(file)

def main():
    print("To delete files in a folder tree with size more than 100MB,")
    print("Enter folder name :")
    folder = input()
    delFiles(folder)

if __name__ == "__main__":
    main()
