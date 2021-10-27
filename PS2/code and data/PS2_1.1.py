# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd

df = pd.read_csv("Sig_Eqs.tsv",sep='\t')
print(df[["Country","Deaths"]].groupby("Country").sum().sort_values(by="Deaths",ascending=False).head(10))