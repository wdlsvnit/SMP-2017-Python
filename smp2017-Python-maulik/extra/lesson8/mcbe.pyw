#! python3
#This program extends mcb.pyw

# mcbe.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcbe.pyw save <keyword> - Saves clipboard to keyword.
#        py.exe mcbe.pyw <keyword> - Loads keyword to clipboard.
#        py.exe mcbe.pyw list - Loads all keywords to clipboard.
#        py.exe mcbe.pyw delete <keyword> - delete keyword from clipboard
#        py.exe mcbe.pyw delete - delete all keywords

import shelve,pyperclip,sys

mcbeShelf=shelve.open("mcbe")

#save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower()=="save":
        mcbeShelf[sys.argv[2]]=pyperclip.paste()
    elif sys.argv[1].lower()=="delete":
        if sys.argv[2] in mcbeShelf.keys():
            del mcbeShelf[sys.argv[2]]
    
#list,use,delete keyword
elif len(sys.argv)==2:
    if sys.argv[1].lower()=="list":
        pyperclip.copy(str(list(mcbeShelf.keys())))
        
    elif sys.argv[1] in mcbeShelf:
        pyperclip.copy(mcbeShelf[sys.argv[1]])

    elif sys.argv[1].lower()=="delete":
        for key in list(mcbeShelf.keys()):
            del mcbeShelf[key]
        
mcbeShelf.close()
    
