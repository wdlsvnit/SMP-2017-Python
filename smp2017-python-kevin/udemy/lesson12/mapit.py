#! /usr/bin/python3

import webbrowser, sys , pyperclip

sys.argv # ['mapit.py','mangaf','block 3']

# checks if commmand line arguments were passed

if len(sys.argv)>1:
	address = ' '.join(sys.argv[1:])
else:
	address = pyperclip.paste()

# https://www.google.com/maps/place/<address>
webbrowser.open('https://www.google.com/maps/place/'+address)
