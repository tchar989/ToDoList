import os
import platform
import getpass

#if platform.system() == 'Darwin':
#	path = '/Users/' + getuser()
#else if platform.System() == 'nt':
#	path = 

def initializeFile(path):
	toDoFile = open(path,"w+")
	toDoFile.write('Mon\nTue\nWed\nThu\nFri\nSat\nSun')
	return

def addTask(day,task,time='NaN'):
	toDoFile = open(path,"w+")
	if time != 'NaN':

filepath = "/Users/" + getpass.getuser() + "/Desktop/hello.txt"
try:
	open(filepath,"r")
except IOError:
	print "Creating file..."
	initializeFile(filepath)


