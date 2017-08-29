#!/usr/bin/env python

import sys

fh = sys.stdin

total_maps_to_one = 0

for line in fh:
    if 'NH:i:1' in line:
        total_maps_to_one += 1
print total_maps_to_one

# cat ~/qbb2017-answers/day2-lunch/mappedreads.sam | ./03-question3.py
# 16602832