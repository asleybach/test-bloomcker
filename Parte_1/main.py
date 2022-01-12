#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
from repository.timebot import the_time as start
from repository.control_browser import TryMakeCheck
from repository.control_data import execute_jobs
from time import sleep
from tqdm import tqdm


print(f'''

test_part1 by asleybach@gmail.com

    execution time: {start()}	

'''
)

print(''' 
    Leyendo lista de cédulas 
''')

if not os.path.exists('files'):
    os.makedirs('files')

def parse_data(data):
    _clean = re.sub('[^0-9ÁÉÍÓÚáéíóúü ]+', '', data)
    return _clean

data_code = list()
data_collection = list()
answer=None

while answer != 'y':
    cod = input('cédula: ')
    data_code.append(parse_data(cod))
    answer = input('''
        ¿ejecutar la consulta y el reporte? 
            Responde s/n: ''')
    
    if answer == 's':
        if len(data_code) !=0:
            for item in tqdm(data_code):
                each=TryMakeCheck(item)
                data_collection.append(each)
            execute_jobs(data_collection)
            print('reporte generado... chequee la carpeta "files" por favor')
            break
        else:
            print('sin cédulas que consultar...')
print('Bye')
        