#!/usr/bin/env python

"""
Usage: ./03-Manhattan-plot.py <gwas output file>
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

df = open(sys.argv[1])
df_name = sys.argv[1]

sig_p = []
n_sig_p = []

count = 0
x_sig =[]
x_n_sig =[]

for line in df:
    if "CHR" in line or "NA" in line:
        continue
    else:
        splt = line.split()
        x = -np.log10(float(splt[8]))
        count += 1
        if float(splt[8]) <= 10e-5:
            sig_p.append(x)
            x_sig.append(count)
        else:
           n_sig_p.append(x)
           x_n_sig.append(count)

x = range(len(sig_p))

plt.figure()
plt.scatter(x_sig, sig_p, alpha = 0.4, c="red")
plt.scatter(x_n_sig, n_sig_p, alpha = 0.4, c="blue")
plt.xlabel("Gene Position")
plt.ylabel(r"$-log_{10}$(P)")
plt.title(str(df_name[12:-13]))
plt.savefig(str(df_name[12:-13] + "_man_plot.png"))
plt.close()