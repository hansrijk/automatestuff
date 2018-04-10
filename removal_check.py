import os

os.chdir('/home/hans/Desktop')

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)
        print(filename)
