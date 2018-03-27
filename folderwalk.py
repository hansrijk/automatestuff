import os

for folderName, subfolders, filenames in os.walk('/home/hans/Desktop/Automate the Boring Stuff with Python Programming'):
	print('de folder is '+folderName)
	print('de subfolders in '+folderName +' zijn; '+str(subfolders))
	print('de filenames in '+folderName +' zijn; '+str(filenames))
	print()
