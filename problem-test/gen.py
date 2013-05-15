import sys
import subprocess
import time
import math
import shutil
import os
import random

randint = lambda a,b:str(random.randint(a,b));

tasks = [
        ['1', 10],
        ['2', 20],
        ['3', 50],
        ['4', 100],
        ['5', 200],
        ['6', 400],
        ['7', 800],
        ['8', 1000],
        ['9', 10000],
        ['10', 20000],
        ]

def gen(opt, fd):
    fd.write(randint(1, opt[1]));
    fd.write(' ');
    fd.write(randint(1, opt[1]));

print 'Remove Last Generation'
subprocess.call('rm *.txt', shell = True)

print 'Generating...'
startTime = time.time()

for task in tasks:
    print task[0]
    fd = open('data/input' + task[0] + '.txt', 'wb');
    gen(task, fd);

stopTime = time.time()
print 'Generate Completed. %.3f second(s)' % (stopTime - startTime)
