#!/usr/local/bin/python3

import os
import sys

filename  = open("outputfile",'w+')
sys.stdout = filename
out = os.system("date")
print(out)
