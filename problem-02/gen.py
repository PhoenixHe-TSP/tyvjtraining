import sys
import subprocess
import time
import math
import shutil
import os
import random

randint = lambda a,b:str(random.randint(a,b));

tasks = [
        ['1', 0, 2, 4, 'LFRCTFCYFCVFCJF'],
        ['2', 0, 4, 2, 'Cz'+'F'*9998],
        ['3', 0, 1, 1, ''],
        ['4', 0, 1, 1, 'FLFLFLFLFCRRFRFRFRF'],
        ['5', 100, 10, 10, ''],
        ['6', 1000, 1, 100, ''],
        ['7', 0, 1, 100, 'RC2'+'F'*9997],
        ['8', 9999, 100, 1, ''],
        ['9', 9999, 100, 100, ''],
        ['10', 9999, 100, 100, ''],
        ]

def gen(opt, fd):
    a, n, m, s = opt[1], opt[2], opt[3], opt[4]
    fd.write(str(n)+' '+str(m)+'\n')
    if a is 0:
        fd.write(s+'\n')
    else:
        while (a>=0):
            rnd = random.randint(0, 3)
            a-=1
            if rnd is 0:
                fd.write('F')
            elif rnd is 1:
                fd.write('L')
            elif rnd is 2:
                fd.write('R')
            else:
                --a
                fd.write('C')
                fd.write(random.choice(\
                        '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-*/'"~!@#$%^&()`\|[]{}<>?.,:;=_''')) 
        fd.write('\n');


print 'Remove Last Generation'
subprocess.call('rm data/*.txt', shell = True)

print 'Generating...'
startTime = time.time()

for task in tasks:
    print task[0]
    fd = open('data/input' + task[0] + '.txt', 'wb');
    gen(task, fd);

stopTime = time.time()
print 'Generate Completed. %.3f second(s)' % (stopTime - startTime)
