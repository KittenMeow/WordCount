import re

fileWanted = input('Enter a file to browse > ')
try:
	opened = open(fileWanted, 'r')
except:
	raise Exception(f'{fileWanted} is an unknown file or directory.')
	opened.close()

	
toSee = input('Enter the word to count > ').lower()
splitted = opened.read().split()
print(f'The text has {len(splitted)} words.')
i = 0
while i < len(splitted):
	splitted[i] = splitted[i].lower()
	splitted[i] = re.sub("[^a-zA-Z]+", "", splitted[i])
	i += 1


wordcount = {}
for a in splitted:
	wordcount[a] = splitted.count(a)
try:
	del wordcount['']
except:
	pass
for key,value in sorted(wordcount.items()):
	print(f'{key}: {value}')
	



if toSee in splitted:
	if splitted.count(toSee) == 1:
		print(f'The word "{toSee}" appears {splitted.count(toSee)} time.')
	else:
		print(f'The word "{toSee}" appears {splitted.count(toSee)} times.')
else:
	print(f'No appearances of the word "{toSee}."')




opened.close()
