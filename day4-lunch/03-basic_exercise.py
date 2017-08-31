#!/usr/bin/env python

"""
Usage: ./03-basic_exercise.py ~/data/results/stringtie/SRR072893/t_data.ctab ~/data/results/stringtie/SRR072915/t_data.ctab scat1
open scat1.png
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

first = pd.read_csv( sys.argv[1], sep="\t")
second = pd.read_csv( sys.argv[2], sep="\t")

dictionary = {}
t_name = first["t_name"]
fpkm1 = first["FPKM"]

for i in range(len(t_name)):
    t = t_name[i]
    f = fpkm1[i]
    dictionary[t] = f

t_name2 = first["t_name"]
fpkm2 = second["FPKM"]
all_f1 = []
all_f2 = []

for i in range(len(t_name)):
    t = t_name2[i]
    f = fpkm2[i]
    if t in dictionary:
        x = dictionary[t]
        y = f
        all_f1.append(x)
        all_f2.append(y)

plt.figure()
plt.scatter(all_f1, all_f2, alpha=0.3)
plt.xlim(.001,100000)
plt.ylim(.001,100000)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("SRR072893 log(FPKM) Values")
plt.ylabel("SRR072915 log(FPKM) Values")
plt.savefig(sys.argv[3] + ".png")

plt.close()