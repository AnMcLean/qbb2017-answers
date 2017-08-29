#!/usr/bin/env python

import sys

fh = sys.stdin

align_total = 0

for line in fh:
    if line.startswith("@"):
        continue
    align_total += 1
print align_total

# cat ~/qbb2017-answers/day2-lunch/mappedreads.sam | ./01-question1.py 
# 22145900