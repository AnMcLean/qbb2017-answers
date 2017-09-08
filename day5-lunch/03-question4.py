#!/usr/bin/env python

"""
usage: ./03-question4.py H3K4me3.bw ~/data/results/stringtie/SRR072893/t_data.ctab <.tab files>
"""

import sys
import pandas as pd
import statsmodels.api as sm
import numpy as np

fpkm_df = pd.read_csv(sys.argv[1], sep = "\t")
fpkm = fpkm_df['FPKM']

his_4 = pd.read_csv(sys.argv[2], sep = "\t", index_col=0)
his_4 = his_4.sort_index()
his_9 = pd.read_csv(sys.argv[3], sep = "\t", index_col=0)
his_9 = his_9.sort_index()
his_27 = pd.read_csv(sys.argv[4], sep = "\t", index_col=0)
his_27 = his_27.sort_index()
his_36 = pd.read_csv(sys.argv[5], sep = "\t", index_col=0)
his_36 = his_36.sort_index()

his_all = pd.concat([his_4[3], his_9[3], his_27[3], his_36[3]], axis = 1)

ind = [his_all]
dep = fpkm
    
model = sm.OLS(dep.values, ind.values).fit()
results = model.fit()

print(results.summary())
