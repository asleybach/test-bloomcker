#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from repository.timebot import the_time as start
from repository.control_data import execute_jobs
from time import sleep

print(f'''
test_part2 by asleybach@gmail.com

    execution time: {start()}	
'''
)

if not os.path.exists('files'):
    os.makedirs('files')

job = lambda : execute_jobs()

sleep(3)
print('Ready...')
sleep(2)
print("check csv file into 'files' folder")
sleep(1)
print("bye")

if __name__ == '__main__':
    job()