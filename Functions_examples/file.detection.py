import os

path = 'C:\\Users\\Helder Roque\\Desktop\\test.txt'

if os.path.exists(path):
    print('That location exists')
    if os.path.isfile(path):
        print('That is a file.')
else:
    print('That location doesn´t exist') 


path_folder = 'C:\\Users\\Helder Roque\\Desktop\\folder'

if os.path.exists(path_folder):
    print('That location exists')
    if os.path.isfile(path_folder):
        print('That is a file.')
    elif os.path.isdir(path_folder):
        print('That is a directory')
else:
    print('That location doesn´t exist')