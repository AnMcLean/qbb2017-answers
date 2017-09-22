#!/usr/bin/env python

"""
Usage ./02-codontable.py realigned.fa

"""

import sys
import fasta3
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import itertools

input_file = open(sys.argv[1])

amino_dictionary = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }

dN = []
dS = []

for i in range(0,4871):
    dN.append(0)
    dS.append(0)
    
nuc_seq = []
for ident, seqs in fasta3.FASTAReader( input_file ):
    nuc_seq.append(seqs)
    
query_seq = nuc_seq[:1]
target_seq = nuc_seq[1:]

for n in range(len(target_seq)):
    count = 0
    prot_count = 0
    while count < 14614:
        target = target_seq[n][count:count+3]
        query = query_seq[0][count:count+3]
        if "-" in target_seq[n][count:count+3]:
            count += 3
            prot_count += 1
        elif "-" in query_seq[0][count:count+3]:
            count += 3
            prot_count += 1
        elif target_seq[n][count:count+3] == query_seq[0][count:count+3]:
            count += 3
            prot_count += 1
        elif target not in amino_dictionary:
            count += 3
        elif query not in amino_dictionary:
            count += 3
        elif amino_dictionary[target] != amino_dictionary[query]:
            dN[prot_count] = dN[prot_count] + 1
            count += 3
            prot_count += 1
        elif amino_dictionary[target] == amino_dictionary[query]:
            dS[prot_count] = dS[prot_count] + 1
            count += 3
            prot_count += 1

diffs = [int(n) - int(s) for n,s in zip (dN, dS)]

diffs_mean = np.mean(diffs)
diffs_std = np.std(diffs)
diffs_SE = (diffs_std)/(math.sqrt(len(diffs)))
z_score = (diffs_mean)/(diffs_std)

print("mean dN - dS: %d" % diffs_mean)
print("dN - dS standard deviation: %d" % diffs_std)
print("dN - dS standard error: %d" % diffs_SE)
print("z score: %d" % z_score)

plt.figure()
plt.plot(diffs)
plt.xlabel("Position")
plt.ylabel("dN - dS")
#plt.yscale('log')
#plt.ylim((1,1000))
plt.savefig("week_1_plot" + ".png")
plt.close()
