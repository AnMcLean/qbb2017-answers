#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"""

./02-heatmap_maker.py abundance_table.tab

"""   

df = pd.read_csv(sys.argv[1],sep='\t',index_col=0)

samples = ['SRR492183', 'SRR492186', 'SRR492188', 'SRR492189', 'SRR492190', 'SRR492193', 'SRR492194', 'SRR492197']

df_samples = df[samples]


labels = {"bin.1":'Staphylococcus haemolyticus',"bin.2":'Leuconostoc citreum',"bin.3":'Staphylococcus lugdunensis',"bin.4":'Enterococcus faecalis',"bin.5":'Cutibacterium avidum',"bin.6":'Staphylococcus epidermidis',"bin.7":'Staphylococcus aureus',"bin.8":"Anaerococcus prevotii"}

bins = []

for i in df_samples.index.tolist():
    bins.append(labels[i])

plt.figure()
plt.imshow(df_samples, aspect='auto', interpolation='nearest')
plt.title("Bacterial Abundance in Infant Gut Microbiome")
plt.xlabel("Sample")
plt.xticks(range(len(df_samples.columns)), df_samples.columns, rotation='vertical')
plt.ylabel("Species")
plt.yticks([x for x in range(len(bins))], bins)
plt.colorbar(label='Abundance')
plt.tight_layout()
plt.savefig("Heatmap.png")
plt.close()
