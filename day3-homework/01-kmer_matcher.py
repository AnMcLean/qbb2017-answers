#!/usr/bin/env python

"""
Matches k-mers between a single query sequence and a database of targets and outputs a file with target 
sequence name, target position, querey position, and k-mer sequence.

to run enter the following in the command line:
 ./01-kmer_matcher.py <target file> <query file> <k-mer length>
"""

import sys
import fasta_homework

tgt = open(sys.argv[1])
qry = open(sys.argv[2])
k = int(sys.argv[3])

index = {}


for ident, sequence in fasta_homework.FASTAReader(tgt):
    sequence = sequence.upper()
    for i in range(0,len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer not in index:
            index[kmer] = [(ident,i)]
        else:
            index[kmer].append((ident,i))
        
ident, sequence = fasta_homework.FASTAReader(qry).next()
sequence = sequence.upper()
count = 0 
for i in range(0,len(sequence) - k):
    count += 1
    if count > 1001:
        break
    else:
        kmer = sequence[i:i+k]
        if kmer in index:
            for x in index[kmer]:
                print str(x[0]) + "\t" + str(x[1]) + "\t"+ str(i) + "\t" + ident + "\t" + kmer
                