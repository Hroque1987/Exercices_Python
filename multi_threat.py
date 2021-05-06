# thread = a flow of execution. Like a separate order of instructions.
#           however each thread takes a turn running to achieve concurrency
#              GIL = (global interpreter lock)
#               allows only one thread to hold the control of the python interpreter at any one time


#cpu bund = programm/task spends most of it's time wating for internal events (CPU intensive)
#           use multiprocessing

# io bound = program/task spends most of it's time waiting for external events (user input, web scraping)
#            use multithreading

import threading
import time



def eat_breakfast():
    time.sleep(3)
    print('you eat breakfast')

def drink_coffe():
    time.sleep(4)
    print('you drank coffe')
    
def study():
    time.sleep(5)
    print('you have studied')

x = threading.Thread(target=eat_breakfast, args=())
x.start()

y = threading.Thread(target=drink_coffe, args=())
y.start()

z = threading.Thread(target=study, args=())
z.start()

x.join() # naw the main thread cant move on to the print instructions
y.join() # has to wait intil threads x,y,z finish
z.join()


#eat_breakfast()
#drink_coffe()
#study()

print(threading.activeCount())
print(threading.enumerate())
