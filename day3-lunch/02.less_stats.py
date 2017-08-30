#!/usr/bin/env python

import sys

total span = 0
genecnt = 0

for line in sys.stdin:
    line = linerstrip()
    mylen = int(line)
    totalspan += mylen
    genecnt += 1
    
print "there are %d genes, with a total span of %d , average gene len is %f" % (genecnt, totalspan, float(totalspan)/genecnt)