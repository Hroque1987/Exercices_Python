# daemon threads = a thread that runs in the background, not impoertand for program to run
#                   your program will not wait for daemon to complete before exiting
#                   non-daemon threads cannot normaly be killed, stay alive until task is complete
#


import threading
import time

def timer():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print ('logged in for: ',count, 'seconds')

x = threading.Thread(target=timer,daemon=True)
x.start()

answer = input('Do you wish to exit?')


