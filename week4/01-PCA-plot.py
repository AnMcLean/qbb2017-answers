#!/usr/bin/env python

"""
Usage: ./01-PCA-plot.py <plink.eigenvec>
"""

import sys
import matplotlib.pyplot as plt

pc1 = []
pc2 = []

for i in open(sys.argv[1]):
    pcs = i.split()
    pc1.append(pcs[-2])
    pc2.append(pcs[-1])
    
plt.figure()
plt.scatter(pc1, pc2)
plt.xlabel('First Principal Component')
plt.ylabel('Second Principal Component')
plt.savefig('PCA')
plt.close()

