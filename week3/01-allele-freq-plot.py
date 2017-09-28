#!/usr/bin/env python

"""
Usage: ./01-allele-freq-plot.py <input .vcf file>
"""

import sys
import matplotlib.pyplot as plt

df = open(sys.argv[1])

allele_freq = []

for line in df:
    if line.startswith("#"):
        continue
    else:
        info = line.split()[7]
        al_freq = ((info.split(";")[3]).strip("AF=")).split(",")
        for i in al_freq:
            allele_freq.append(float(i))

plt.figure()
plt.hist(allele_freq, bins=50)
plt.xlabel("Allele Frequency")
plt.ylabel("Number of Alleles")
plt.savefig("allele_freq_histogram.png")
plt.close()