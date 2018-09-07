#!/usr/local/bin/python3
import sys
import os

empFile = (os.system('df -h')) 

with open('samplefile', 'a+') as f:
	for line in f:
		print(empFile)
