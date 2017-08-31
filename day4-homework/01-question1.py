#!/usr/bin/env python

"""
Usage: ./01-timecourse.py <samples.csv> <ctab_dir> <replicates.csv> <ctab_dir>
       open question_1_figure.png
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt

transcript = "FBtr0331261"

df_samples = pd.read_csv(sys.argv[1])
soi = df_samples["sex"] == "female"

ef_samples = pd.read_csv(sys.argv[3])
sof = ef_samples["sex"] == "female"

fpkms1 = []
for sample in df_samples["sample"][soi]:
    # Build complete file path
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    # Read current sample
    df = pd.read_csv(fname, sep="\t")
    # Subset just Sxl rows
    roi = df["t_name"] == transcript
    # save FPKM value to data frame
    fpkms1.append(df[roi]["FPKM"])

fpkms3 = [None,None,None,None]
for sample in ef_samples["sample"][sof]:
    ename = os.path.join(sys.argv[2], sample, "t_data.ctab")
    ef = pd.read_csv(ename, sep="\t")
    roi = ef["t_name"] == transcript
    fpkms3.append(ef[roi]["FPKM"].values[0])

df_samples = pd.read_csv(sys.argv[1])
soi = df_samples["sex"] == "male"

ef_samples = pd.read_csv(sys.argv[3])
sof = ef_samples["sex"] == "male"

fpkms2 = []
for sample in df_samples["sample"][soi]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab")
    df = pd.read_csv(fname, sep="\t")
    roi = df["t_name"] == transcript
    fpkms2.append(df[roi]["FPKM"])
    
fpkms4 = [None,None,None,None]
for sample in ef_samples["sample"][sof]:
    ename = os.path.join(sys.argv[2], sample, "t_data.ctab")
    ef = pd.read_csv(ename, sep="\t")
    roi = ef["t_name"] == transcript
    fpkms3.append(ef[roi]["FPKM"].values[0])

plt.figure()
plt.plot(fpkms1, color="r", label="Female")
plt.plot(fpkms3, color="r")
plt.plot(fpkms2, color="b", label="Male")
plt.plot(fpkms4, color="b")
plt.legend(loc='upper center')
plt.ylabel("mRNA abundance log(FPKM)")
plt.xlabel('developmental stage')
plt.title('Sxl mRNA abundance during developement')
plt.xlim(0,7)
plt.xticks([0, 1, 2, 3, 4, 5, 6, 7], ['10', '11', '12', '13', '14A', '14B', '14C', '14D'])
plt.subplots_adjust(bottom=0.2)
plt.savefig("question_1_figure.png")
plt.close()