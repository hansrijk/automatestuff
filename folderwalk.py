import os

for folderName, subfolders, filenames in os.walk('/home/hans/test'):
    print('de folder heet '+folderName)
    print('de subfolders in '+folderName +' zijn; '+str(subfolders))
    print('de filenames in '+folderName +' zijn; '+str(filenames))
    print()

       for subfolder in subfolders:
              if 'iets' in subfolder:
                # os.rmdir(subfolder)
                print('rmdir on ' + subfolder)

for file in filenames:
              if file.endswith('.py'):
                   shutil.copy(os.join(folderName, file), os.join(folderName, file + '.backup'))
