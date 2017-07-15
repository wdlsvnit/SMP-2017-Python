#! python3
#Add lyrics directly to mp3 files in iTunes
#Works only for macOS
#Uses AppleScript

'''
Combines usage of AppleScript and Python
to add lyrics to the song in iTunes

Module used: osascript
'''

from osascript import osascript

def addToITunes(song,artist,lyrics):  #to search song with name and its author similar to regex pattern

    #pass AppleScript to addlyrics to variable cmd
    #Limitation : artist name should be same as entered
    cmd = '''
global f,ly,a

set a to "%s"
set f to "%s"
set ly to "%s"

tell application "iTunes"
	set res to (every file track whose name contains f and artist is a)
    if res is in {{}, {""}, ""} then set lyrics to ly
		repeat with t in res
                        if lyrics of t is in {{}, {""}, ""} then set lyrics of t to ly
		end repeat
end tell

'''%(artist,song,lyrics.lstrip("\n"))


    returncode,stdout,stderr = osascript(cmd)
    #if return code is not zero then error can be debugged by studying stderr

    if returncode != 0 :
        return False
    else:
        return True
