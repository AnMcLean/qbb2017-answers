#!/usr/bin/env python

"""
Usage: ./02_diff_expression.py hema_data.txt
"""

import sys
import pandas as pd
from scipy import stats

df = pd.read_csv( sys.argv[1], sep='\t' ).dropna()
early = [ 'CFU', 'mys', 'mid' ]
late = [ 'poly', 'unk', 'int' ]
df['mean_early'] = df[early].mean(axis=1)
df['mean_late'] = df[late].mean(axis=1)
t,p = stats.ttest_ind(df[early],df[late], axis=1)
df['p-value'] = p
df['ratio'] = df['mean_early'] / df['mean_late']
df = df.mask( df['p-value'] > 0.05 ).dropna()
down = df.mask( df['ratio'] > 0.5 ).dropna()
up = df.mask( df['ratio'] < 2.0 ).dropna()
new_df= pd.concat( [ down, up ] )[['gene','ratio','p-value']].sort_values('p-value')
print new_df.to_csv(index=False,sep='\t')

