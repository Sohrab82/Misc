
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 11:20:35 2020

@author: sohsaf
"""

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
    time.sleep(2)
    print('{} squared results in a/an {} number'.format(x, basic_func(y)))


if __name__ == '__main__':

    starttime = time.time()
    pool = multiprocessing.Pool()
    pool.map(multiprocessing_func, range(0, 10))
    pool.close()
    print('That took {} seconds'.format(time.time() - starttime))
