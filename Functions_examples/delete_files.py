import os

path = 'test.txt'

try:
    os.remove(path) # use to remove a file
    #os.rmdir(path) use to remove a empty folder

except FileNotFoundError:
    print(path+' not found')

# to delete a folder with files

import shutil

shutil.rmtree(path)
