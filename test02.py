#!/usr/local/bin/python3

import os

df = os.system("`df -h |awk '{print $5}'`")
dfout = os.system("`dfout.` date +\"%Y%m%d\"``")


#out = os.system("df -h |awk '{print $5}' > dfout.` date +\"%Y%m%d\"`")

#os.system("df" > "dfout")

#out = os.system("df > dfout")

print('df')
