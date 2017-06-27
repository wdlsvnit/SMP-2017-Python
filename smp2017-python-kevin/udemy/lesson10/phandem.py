import pyperclip, re



PhRegex = re.compile("""
# 415-555-0000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?	#first 3 digits
(-|\s)				
\d\d\d				#next 3 digits
-
\d\d\d\d			#last 4 digits
(((ext(\.)?\s)|x)\d+)?		#extension
)
""",re.VERBOSE)


EmRegex = re.compile("""
#lawf@lmf.com

[a-zA-Z0-9+.]+
@
[a-zA-Z0-9+.]+
""",re.VERBOSE)

text = pyperclip.paste()

phlist = PhRegex.findall(text)
emlist = EmRegex.findall(text)

print(phlist)
print(emlist)

phnoes = []

for i in phlist:
	phnoes.append(i[0])

results = '\n'.join(phnoes) + '\n' + '\n'.join(emlist)

pyperclip.copy(results)
















