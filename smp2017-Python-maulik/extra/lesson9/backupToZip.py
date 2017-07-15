#! python3
#Copies an entire folder and its contnts into a ZIP file-
#whose filename increments

import zipfile,os

def backupToZip(folder):
    folder = os.path.abspath(folder)
    os.chdir(folder)
    
    number=1
    while True:
        zipFilename=os.path.basename(folder) + "_" + str(number) + ".zip"
        if not os.path.exists(zipFilename):
            break
        number += 1

    
    print("Creating %s...."%(zipFilename))
    backupZip=zipfile.ZipFile(zipFilename,"w")

    for foldername,subfolders,filenames in os.walk(folder):
        print("Adding files in %s...."%(foldername))
        backupZip.write(foldername)
        for filename in filenames:
            if filename.endswith(".zip"):
                continue
            newBase = os.path.basename(folder) + "_"
            if filename.startswith(newBase) and filename.endswith(".zip"):
                continue
            backupZip.write(os.path.join(foldername,filename))

    backupZip.close()
    print("Done.")

def main():
    print("Enter folder to backup :")
    folder=input()
    backupToZip(folder)

if __name__=="__main__":
    main()
        
    
