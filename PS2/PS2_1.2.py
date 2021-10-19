# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:30:31 2021

@author: 92303
"""

import pandas as pd

df = pd.read_csv("Sig_Eqs.tsv",sep='\t')
df1 = pd.DataFrame(df, columns=("Year","Mag"))
df2 = df1.loc[df1["Mag"] > 6]
df2.groupby(["Year"]).count()
print(df2)