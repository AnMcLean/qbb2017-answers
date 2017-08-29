#!/usr/bin/env python

import sys

fh = sys.stdin

total_mapq = 0

for line1 in fh:
    if not line1.startswith("@"):
        col_splt = line1.split("\t")
        total_mapq += float(col_splt[4])

line_total = 0

for line2 in fh:
    if not line2.startswith("@"):
        line_total += 1

ave_mapq = total_mapq/line_total
print ave_mapq
                