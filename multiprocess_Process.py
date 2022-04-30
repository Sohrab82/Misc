# #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:16:01 2020

@author: sohsaf
"""
'''
The multiprocessing Python module contains two classes capable of handling tasks. 
The Process class sends each task to a different processor, 
and the Pool class sends sets of tasks to different processors.
Pool is most useful for large amounts of processes where each process can execute quickly, 
while Process is most useful for a small number of processes where each process would 
take a longer time to execute.

The pool class works better when there are more processes and small IO wait. 
The Process class works better when processes are small in number and IO operations are long. 
'''

import time
import multiprocessing


def basic_func(x):
    if x == 0:
        return 'zero'
    elif x % 2 == 0:
        return 'even'
    else:
        return 'odd'


def multiprocessing_func(x):
    y = x * x
    time.sleep(5)
    print('{} squared results in a/an {} number'.format(x, basic_func(y)))


if __name__ == '__main__':
    starttime = time.time()
    processes = []
    for i in range(0, 10):
        p = multiprocessing.Process(target=multiprocessing_func, args=(i,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()

    print('That took {} seconds'.format(time.time() - starttime))
