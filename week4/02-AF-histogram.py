#!/usr/bin/env python

"""
Usage: ./02-AF-histogram.py plink.frq
"""

import sys
import matplotlib.pyplot as plt

df = open(sys.argv[1])

allele_freq = []

for line in df:
    if line.startswith(" C"):
        continue
    else:
        a_freq = line.split()[-2]
        allele_freq.append(float(a_freq))

plt.figure()
plt.hist(allele_freq, bins=30)
plt.xlabel("Allele Frequency")
plt.ylabel("Count")
plt.savefig("allele_freq_histogram.png")
plt.close()