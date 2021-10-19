# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv("Sig_Eqs.tsv",sep='\t')
df1 = pd.DataFrame(df, columns=("Country","Deaths"))
df2 = df1.groupby("Country").sum()
df3 = df2.sort_values(by="Deaths",ascending = False).head(10)
print(df3)