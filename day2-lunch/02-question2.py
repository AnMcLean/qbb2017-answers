#!/usr/bin/env python

import sys

fh = sys.stdin

align_matches = 0

for line in fh:
    if 'NM:i:0' in line:
        align_matches += 1
print align_matches
    
# cat ~/qbb2017-answers/day2-lunch/mappedreads.sam | ./02-question2.py
# 14589427