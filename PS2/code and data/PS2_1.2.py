# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:30:31 2021

@author: 92303
"""

import pandas as pd

df = pd.read_csv("Sig_Eqs.tsv",sep='\t')
df[df["Mag"]>6][["Year","Mag"]].groupby("Year")["Year"].count().plot()
