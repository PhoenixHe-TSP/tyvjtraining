import sys
import subprocess
import glob
import time
import math
import shutil
import os

si = sys.stdin
so = sys.stdout
se = sys.stderr

solver = 'main.cpp'
compiler = "g++ "
options = "-o main -std=c++0x "

compileCommand = compiler + options + solver
runner = "./main"
runCommand = [runner]

devnull = open(os.devnull, 'w')

print 'Step 1: Compile Solver %s' % solver
startTime = time.time()
retCode = subprocess.call(compileCommand, shell = True)
stopTime = time.time()
if retCode:
	print 'Compiler exited with Code %d, compile error.' % retCode
	sys.exit(1)
print 'Compile Success! Compiled in %.3f second(s)' % (stopTime - startTime)

print 'Step 2: Get Input File List'

tasks = []

for inputFile in glob.glob("data/input*.txt"):
	print 'Found Input File: %s' % inputFile
	tail = inputFile[10:]
	outputFile = 'data/output' + tail
	tasks.append((inputFile, outputFile))

print '%d Input File(s) found!' % len(tasks)

print 'Step 3: Generate the Output File'
runTime = 0.0
for task in tasks:
	so.write('Running for Input File: %s, Output File %s ... ' % task)
	inputfd = open(task[0], 'rb')
	outputfd = open(task[1], 'wb')
	startTime = time.time()
	retCode = subprocess.call(runCommand, stdin = inputfd, stdout = outputfd)
	stopTime = time.time()
	if retCode:
		print 'Failed!'
		print 'Solver exit with Code %d' % retCode
		sys.exit(1)
	print 'OK'
	curRunTime = stopTime - startTime
	if runTime < curRunTime:
		runTime = curRunTime
	print 'Generated in %.3f second(s)' % curRunTime

print '-----------------------------------------------'
print 'Generation Finished.'
print 'Longest Execution Time: %.3f second(s)' % runTime
print 'Suggest Time Limit: %d second(s)' % int(math.ceil(runTime * 3) + 0.5)
print '-----------------------------------------------'

print 'Step 4: Cleanup the workspace'
print 'All OK. Will now exit.'
