# multiprocessing = running tasks in parallel on different cpu cores, bypass GIL used for Trheading
#                   multiprocessing = better for cpu bound tasks
#                   multithreading  = better for io bound tasks

from multiprocessing import Process, cpu_count
import time




def counter(num):
    count = 0
    while count < num:
        count += 1



def main():
    
    print(cpu_count())

    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))
    a.start()
    b.start()
    
    a.join()
    b.join()


    print('finished in :', time.perf_counter(),'seconds')



if  __name__ =='__main__': # to prevent the child process from create another child process
    main()

