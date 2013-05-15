import sys
import subprocess
import time
import math
import shutil
import os
import random

randint = lambda a,b:str(random.randint(a,b));

tasks = [
        ['1', 2, 1, 2],
        ['2', 10, 4, 7],
        ['3', 50, 13, 14],
        ['4', 100, 1, 100],
        ['5', 500, 314, 413],
        ['6', 1000, 1, 2],
        ['7', 5000, 4999, 5000],
        ['8', 8000, 3514, 5137],
        ['9', 10000, 9999, 10000],
        ['10', 10000, 172, 9981],
        ]

def gen(opt, fd):
    size, b0, b1 = opt[1], opt[2], opt[3]
    fd.write(str(size)+'\n')
    l = range(1, size+1)
    del l[b1-1]
    del l[b0-1]
    random.shuffle(l)
    for x in l:
        fd.write(str(x)+' ')
    fd.write('\n')

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
