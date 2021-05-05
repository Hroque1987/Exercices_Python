import os

source = 'copy.txt'
destination = 'C:\\Users\\Helder Roque\\Desktop\\test.txt'

try:
    if os.path.exists(destination):
        print('There is alredy a file there')
    
    else:
        os.replace(source,destination)
        print(source+' was moved')

except FileNotFoundError:
    print(souce+' was not found')
    
# can be used to move directory
