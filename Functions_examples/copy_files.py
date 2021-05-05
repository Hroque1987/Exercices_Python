#copyfile() = copies contents
#copy() = copyfile() + permission mode + destination can be directory
#copy2() = copy() + copies metadata (file creation and modification time)

import shutil

shutil.copyfile('test.txt', 'C:\\Users\\Helder Roque\\Desktop\\copy.txt')