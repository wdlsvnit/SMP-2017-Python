#RetreiveLyrics
"""
A Python program to add lyrics of mp3 files in form of text file

macOS: Link Lyrics to iTunes (Given song should be present in iTunes)

"""
# Automated A Boring Task

# external module usage : requests,bs4

import os,requests,bs4,sys,re,time
import helpers


def musicFolder():  #Gets the path of folder containing music
    musicFolder = input("Enter abs path of music folder :")
    
    if not os.path.exists(musicFolder):
        print("Path doesnt exists")
        print("Try again.")
        sys.exit(1)                  #1 if path does not exits

    return musicFolder

def mp3Finder(musicFolder):
    playlist = []
    noOfFiles=0

    myLyricsFolder = os.path.join(musicFolder,"MyLyrics")
    
    #make Mylyrics folder in the same folder, if not already present
    if not os.path.exists(myLyricsFolder):
        os.makedirs(myLyricsFolder)          
    os.chdir(myLyricsFolder)
    
    for foldername,subfolder,filenames in os.walk(musicFolder):
        for filename in filenames:
            
            if not filename.endswith(".mp3"):
                continue
            
            #.txt file to add in MyLyrics        
            isPresent = os.path.join(myLyricsFolder , filename.rstrip(".mp3") + ".txt")  
            if os.path.exists(isPresent):
                continue
            
            noOfFiles += 1
            songInfo = []
            
            print("For %s ... "%(filename.rstrip(".mp3")))   #Because every filename is not meaningful (atleast mine)
            artist = input("Artist name :")                  #Chance that artist name or song name is missing
            songInfo.append(artist)                          #Most IMP info from user
            song = input("Song name :")
            songInfo.append(song)
            language = input("English or Hindi (E or H) :")  #Language beacuse Two different sites for each lingo
            print("\n")

            #Save info into list of list so that user can relax
            songInfo.append(filename)
            songInfo.append(language)
            playlist.append(songInfo)   

    print("Total songs(mp3) :" + str(noOfFiles))
    if noOfFiles == 0:    
        return None
    
    print("Processing .... sit back and relax")        
    print("\n\n\n")

    return playlist

def searchGoogle(playlist):

    for info in playlist:
        
        l = info[3]

        #Flow control acc to lingo of song
        if l == "e" or l == "E" or l == "English" or l == "english":
            lang = "azlyrics.com"

        elif l == "h" or l == "H" or l == "Hindi" or l == "hindi":
            lang = "lyricsmint.com"
            
        else :
            print("Can only handle english or hindi songs.")
            sys.exit(3)  #3 if other than e or h
        
        url = "https://www.google.com/search?q=" + info[0].strip() + "+" + info[1].strip() + "+lyrics+" + lang.rstrip(".com")
        goog = requests.get(url)
        goog.raise_for_status()

        #To get all searches from google        
        azSoup = bs4.BeautifulSoup(goog.text,"html.parser")
        linkElems = azSoup.select(".r a")                      

        #filter href of required site
        az = re.compile(lang)               
        for links in linkElems:
            if az.search(links.get("href")) != None:
                lyricsUrl = "https://www.google.com" + links.get("href")
                break

        #Flow control acc to lingo of song
        if lang == "azlyrics.com":
            lyrics = helpers.EgetLyrics(lyricsUrl)            
        else :
            lyrics = helpers.HgetLyrics(lyricsUrl)

        lyTxt = info[2].rstrip(".mp3") + ".txt"

        #Add lyrics in a simple text file
        lyFile = open(os.path.join(".",lyTxt),"w")
        
        lyFile.write(info[0] + " -- " + info[1])
        lyFile.close()

        lyFile = open(os.path.join(".",lyTxt),"a",encoding = "utf-8")
        lyFile.write(lyrics)
        lyFile.close()

        print(info[2] + "..... Lyrics written...")
        

def main():
    try:
        music = musicFolder()
        print("")
        print("For the following songs you have to enter artist name,song name and language of song.")  #TODO : add delay
        print("IMPORTANT : proper details required to link lyrics with iTunes")
        print("FILL CAREFULLY")
        
        time.sleep(7)      #Smooth transition and reading time
        
        playlist = mp3Finder(music)

        if playlist == None:
                print("No mp3 file found or all mp3s have lyrics")
                print("Exiting.")
                sys.exit(2)  #2 if file not found

        searchGoogle(playlist)

        print("\nDONE!")
    except Exception as exc:
        print("There was a problem:" + str(exc))

if __name__ == "__main__":
    main()
