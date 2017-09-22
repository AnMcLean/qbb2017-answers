#!/usr/bin/env python

"""
Usage: ./02-dotplot.py <lastz file> <plot name>
"""

import fasta3 as fasta
import matplotlib.pyplot as plt
import sys

df = open(sys.argv[1])

plt.figure()

count = 0

for x in df:
    if "start1" in x:
            continue
    else:
        field = x.split("\t")
        plt.plot([count, count + int(field[1])], [int(field[1]),int(field[0])])
        count += int(field[1])
        
plt.ylim((0,100000))
plt.xlim((0,50000))
plt.xlabel("Reference Position")
plt.ylabel("Contig") 
plt.savefig( sys.argv[2] + ".png")
plt.close()