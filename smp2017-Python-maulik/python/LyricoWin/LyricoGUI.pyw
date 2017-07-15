import traceback
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *

import time
import os,requests,bs4,sys,re
import helpers

toGetSize = Tk()
toGetSize.withdraw()

w = 500 # width for the Tk
h = 300 # height for the Tk

# get screen width and height
ws = toGetSize.winfo_screenwidth() # width of the screen
hs = toGetSize.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk  window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

toGetSize.destroy()

def index():

#-------------------------GUI start------------------------#
   global ind,indExit
   ind = Tk()
   ind.title("Welcome to Lyrico")
   indExit = False

   ind.geometry('%dx%d+%d+%d' % (w, h, x, y))       #Set window to center
   ind.resizable(width=False,height=False)

   Label(ind,text="Lyrico",font=("times",30,"bold")).pack(pady=50)
   Label(ind,text="Add text files of your mp3 with lyrico").pack()
   Button(ind,text="Start",command = inputFile).pack(pady=30)
#-----------------------GUI end------------------------#
   ind.mainloop()


def inputFile():

   ind.destroy()     #Destroys existing windows to move on in gui
   indExit = True
   global folder,folderExit
#----------------------GUI start-------------------------#
   folder = Tk()
   folder.title("Choose Music Folder")
   folderExit = False

   folder.geometry('%dx%d+%d+%d' % (w, h, x, y))
   folder.resizable(width=False,height=False)
   Label(folder,text="Your Music Folder :",font=("times",26,"italic"),justify=CENTER).pack(pady=50)
   getFold = Button(folder,text="Browse",justify=CENTER,command=getFolder)
   getFold.pack()
#------------------------GUI end-------------------------#
   folder.mainloop()

def getFolder():

   global musicFolder
   musicFolder = filedialog.askdirectory()
   while musicFolder == "":    #checks if musicFolder is empty
      folder.mainloop()

   folder.destroy()
   folderExit = True
   instructUser()

def instructUser():

   global instructions,instructionsExit
#------------------------GUI start-------------------------#
   instructions = Tk()
   instructions.title("INSTRUCTIONS")
   instructionsExit = False

   instructions.geometry('%dx%d+%d+%d' % (w, h, x, y))
   instructions.resizable(width=False,height=False)
   Label(instructions,text="IMPORTANT:",justify=CENTER).pack(pady=10,fill=X)

   inst= "Proper detalis required to search\n\nFILL CAREFULLY"
   msg = Message(instructions, text = inst)
   msg.config(bg='gray', font=('times', 26, 'italic'))
   msg.pack(pady=15,fill=X)

   Button(instructions, text='OK',justify=CENTER,command=getInfo).pack()
#------------------------GUI end-----------------------------#
   instructions.mainloop()


def resetInfo():   #Resests Entries
   e1.delete(0,END)
   e2.delete(0,END)
   e3.set("")


def validateInfo():            #Validation Check
   if not e1.get() or not e2.get() or not e3.get():
      messagebox.showwarning("Field Empty","Please fill all the fields!")
      resetInfo()
      master.mainloop()
   else :
      subInfo()

def subInfo():

   i = []
   i.append(e1.get())
   i.append(e2.get())
   i.append(e3.get())
   i.append(filename)
   resetInfo()
   playlist.append(i)

   master.destroy()
   masterExit = True

def getInfo():

   global master,masterExit,win
   global e1,e2,e3
   global playlist,noOfFile,myLyricsFolder,filename
   global i
   i = []
# -----------------------------------------------------------#
   #from CLI

   playlist = []
   noOfFile=0

   myLyricsFolder = os.path.join(musicFolder,"MyLyrics")

   #make Mylyrics folder in the same folder, if not already present
   if not os.path.exists(myLyricsFolder):
      os.makedirs(myLyricsFolder)
   os.chdir(myLyricsFolder)

   '''GUI'''
   instructions.destroy()
   instructionsExit = True
#------------------from CLI -------------------------------#
   for foldername,subfolder,filenames in os.walk(musicFolder):

      for filename in filenames:
         if not filename.endswith(".mp3"):
            continue

         #.txt file to add in MyLyrics
         isPresent = os.path.join(myLyricsFolder , filename.rstrip(".mp3") + ".txt")
         if os.path.exists(isPresent):
            continue

         noOfFile += 1
     #----GUI start----------#
         master = Tk()
         master.title("Fill Info")
         masterExit = False

         master.geometry('+%d+%d'% (x, y))        #Variable Dimension window
         master.resizable(width=False,height=False)
         master.protocol('WM_DELETE_WINDOW',dontAllow)

         Label(master,text = filename.rstrip(".mp3"),font=("times",24)).grid(row=0,column=0,columnspan=3,pady=15,sticky = W+E)
         Label(master, text="Artist").grid(row=1,column=0,sticky = W+E)
         Label(master, text="Song Name").grid(row=2,column=0,sticky=W+E)

         e1 = Entry(master)
         e2 = Entry(master)

         e1.grid(row=1,column=1,sticky=W+E)
         e2.grid(row=2,column=1,sticky=W+E)

         e3 = StringVar()
         #e3.set("English")

         Label(master,
            text="Language",
            justify = LEFT,
            padx = 20).grid(row=3,column=0,sticky=W+E)
         Radiobutton(master,
                  text="English",
                  padx = 20,justify = LEFT,
                  variable=e3,
                  value="English").grid(row=3,column=1,pady=4,sticky=W+E)
         Radiobutton(master,
                  text="Hindi",
                  padx = 20,justify = LEFT,
                  variable=e3,
                  value="Hindi").grid(row=4,column=1,pady=4,sticky=W+E)

         submit = Button(master, text='Submit',justify=RIGHT, command=validateInfo).grid(row=5,column=0, pady=4)
         reset = Button(master, text='Reset',justify=LEFT, command=resetInfo).grid(row=5,column=2, pady=4)
    #-----------GUI end---------------

         master.mainloop()

    #Window for sake of animation
   win = Tk()
   win.title("Processing...")
   win.after(5,searchGoogle)            #To retain window then start searching
   win.geometry('%dx%d+%d+%d'% (w, h, x, y))
   win.resizable(width=False,height=False)
   win.protocol('WM_DELETE_WINDOW',dontAllow)   #Dont allow user to exit at the time of processing

def totSongDetails():
#------------------------GUI start--------------------------------#
   global totSong,totSongExit
   totSong = Tk()
   totSong.title("Total Songs")
   totSongExit = False

   totSong.geometry('%dx%d+%d+%d' % (w, h, x, y))
   totSong.resizable(width=False,height=False)
   Label(totSong,text = "Total songs(mp3) :%s"%(noOfFile)).pack(pady=30)
   Label(totSong,text = "Total songs(mp3) Written :%s"%(filesWritten)).pack(pady=30)
   if noOfFile == 0:
      Label(totSong, text = "No new songs").pack()
      Button(totSong,text = "Restart",command=restart).pack()
      Button(totSong,text = "Quit",command=totSong.destroy).pack()
      totSong.quit()
   else:
      Label(totSong,text="DONE",justify = CENTER).pack(pady=30)
      Button(totSong,text="Files Added",command=showProcess).pack(pady = 5)
#------------------------GUI end----------------------------#
   totSong.mainloop()

def dontAllow():
   messagebox.showwarning("Bad Request","Cant quit in middle of process!")

def restart():
   global totSong
   totSong.destroy()
   totSongExit = True
   main()

def Restart():
    global SP
    SP.destroy()
    main()

# ---- ----- CLI -----------#

def searchGoogle():

#-----------------------from CLI------------------------------------#
    global filesAdded,filesWritten
    filesWritten = 0
    filesAdded = []
    for info in playlist:

        l = info[2]

        #Flow control acc to lingo of song
        if l == "English":
            site = "azlyrics.com"

        elif l == "Hindi":
            site = "lyricsmint.com"

        url = "https://www.google.com/search?q=" + info[0].strip() + "+" + info[1].strip() + "+lyrics+" + site.rstrip(".com")
        goog = requests.get(url)
        goog.raise_for_status()

        #To get all searches from google
        azSoup = bs4.BeautifulSoup(goog.text,"html.parser")
        linkElems = azSoup.select(".r a")

        lyricsUrl = ""
        #filter href of required site
        az = re.compile(site)
        for links in linkElems:
            if az.search(links.get("href")) != None:
                lyricsUrl = "https://www.google.com" + links.get("href")   #Can create Error
                break

        #Flow control acc to lingo of song
        if lyricsUrl == "":
            messagebox.showwarning("Lyrics not found",info[3] + " - Lyrics not found on site")
            continue
        #Possilbilty of NameError : lyricsUrl not defined
        if site == "azlyrics.com":
            lyrics = helpers.EgetLyrics(lyricsUrl)
        else :
            lyrics = helpers.HgetLyrics(lyricsUrl)

        if lyrics == "":
            messagebox.showwarning("Lyrics Not Found",info[3] + " - Lyrics not found")
            continue

        filesWritten += 1
        lyTxt = info[3].rstrip(".mp3") + ".txt"

        #Add lyrics in a simple text file
        lyFile = open(os.path.join(".",lyTxt),"w")

        lyFile.write(info[0] + " -- " + info[1])
        lyFile.close()

        lyFile = open(os.path.join(".",lyTxt),"a",encoding = "utf-8")
        lyFile.write(lyrics)
        lyFile.close()

        filesAdded.append(lyTxt)

    win.destroy()
    totSongDetails()
 ## -------------------------------------------------------##

def showProcess():

   totSong.destroy()
   totSongExit = True
   global SP,SPExit
#----------------------------GUI start---------------------------#
   GorW = 1 #First Gray
   SP = Tk()
   SP.title("Files Added")
   SPExit = False

   SP.geometry('%dx%d+%d+%d' % (w, h, x, y))
   SP.resizable(width=False,height=False)

   ybar = Scrollbar(SP)
   ybar.pack(side=RIGHT,fill=Y)

   sbar = Scrollbar(SP)
   sbar.pack(side=BOTTOM,fill=X)

   Label(SP,text="Lyrics Files:",font=("times",20,"bold")).pack(side=TOP)

   listbox = Listbox(SP)
   listbox.pack(side=TOP,fill=X)

   for file in filesAdded:
      if GorW%2 == 0:          #Alternate gray and white
         bg = "white"
      else:
         bg = "gray"
      listbox.insert(END,file)
      listbox.itemconfigure(END,bg=bg)
      GorW += 1

   Button(SP,text="Quit",command=SP.destroy).pack(side=TOP)
   Button(SP,text = "Restart",command=Restart).pack()

   SP.mainloop()

def main():
    index()

if __name__ == "__main__":
    # any name as accepted but not signature
    def report_callback_exception(self, exc, val, tb):
        messagebox.showerror("Error", message=str(exc) + str(val) + str(tb))
        messagebox.showwarning("Exit","Exiting App")
        global win
        win.destroy()

    Tk.report_callback_exception = report_callback_exception
    # now method is overridde"""
main()

'''except Exception as exc:
    exp = Tk()
    exp.title("Exception Found")
    #exp.eval('tk::PlaceWindow %s center'%(exp.winfo_pathname(exp.winfo_id())))
    exp.geometry('%dx%d+%d+%d' % (w, h, x, y))
    Label(exp,text ="Exception:\n" + str(exc)).pack()
    Button(exp,text = "Quit",command=exp.destroy).pack()'''
