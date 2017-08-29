#!/usr/bin/env python

import sys

fh = sys.stdin

count = 0
for line in fh:
        if not line.startswith("@"):
            col_splt = line.split("\t")
            print col_splt[2]
            count += 1
            
        if count > 10:
            break
""""
cat ~/qbb2017-answers/day2-lunch/mappedreads.sam | ./04-question4.py  
2R
3R
3R
X
3L
2R
2L
*
2R
3L
3L
"""