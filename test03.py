#!/usr/local/bin/python3

import os

out = os.system("df -h |awk '{print $5}' > dfout.` date +\"%Y%m%d\"`")

#with open('out', 'r') as f:
#   for line in f:
#      print(line)


big = os.system("grep -Eo '[0-9]+' dfout.` date +\"%Y%m%d\"`| sort -rn | head -n 1")
print(big)
