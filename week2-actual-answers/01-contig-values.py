#!/usr/bin/env python

"""
Usage: ./01-contig-values.py <fasta contigs file>
"""

import sys
import fasta3 as fasta
import operator

contigs = open(sys.argv[1])

list_of_contigs = []
length_all = 0

for ident, seq in fasta.FASTAReader(contigs):
    if len(seq) == 0:
        continue
    list_of_contigs.append(seq)
    length_all += len(seq)
    
list_of_contigs = sorted(list_of_contigs, key=operator.itemgetter(2), reverse=True)

n_contigs = len(list_of_contigs)

min_contig = len(max(list_of_contigs))

max_contig = len(min(list_of_contigs))

total_nucs = 0

for i in list_of_contigs:
    total_nucs += len(i)

avg_contig_len = float(total_nucs) / float(len(list_of_contigs))

x = float(length_all)/2

count = 0
for contig in list_of_contigs:
    count += len(contig)
    if count >= x:
        n50 = contig
        break
    
print "Number of contigs: %d" % (n_contigs)
print "Minimum contig length: %d" % (min_contig)
print "Maximum contig length: %d" % (max_contig)
print "Average contig length: %f" % (avg_contig_len)
print "N50: %f" % (len(n50))


