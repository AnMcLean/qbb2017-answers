#!/usr/bin/env python

"""
usage: ./01-question2.py ~/data/results/stringtie/SRR072893/t_data.ctab <output file name>
"""

import sys
import pandas as pd

df = pd.read_csv(sys.argv[1], sep = "\t")

forward = df["strand"] == "+"
reverse = df["strand"] == "-"

df_f = df[forward]
df_f["start."] = df_f["start"] - 500
df_f["end."] = df_f["start"] + 500

df_r = df[reverse]
df_r["start."] = df_r["end"] + 500
df_r["end."] = df_r["end"] - 500

df_all=pd.concat([df_r, df_f])

coi = [ "chr", "start.", "end.", "t_name" ]


df_all[coi].to_csv(sys.argv[2] + ".bed", sep = "\t", index=False)