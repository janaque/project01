#!/usr/local/bin/python3

import os


out = os.system("df -h |awk '{print $5}' > dfout.` date +\"%Y%m%d\"`")

