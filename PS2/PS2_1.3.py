# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:09:42 2021

@author: 92303
"""

import pandas as pd

df = pd.read_csv("Sig_Eqs.tsv",sep='\t')
c='CHINA'
maxmag = df[df["Country"] == c]["Mag"].max()
print(maxmag)
df[(df["Mag"] == maxmag) & (df["Country"] == c)]["Year","Mo"]

def Count_LargestEq(c):
    
    num = df[df["Country"] == c]["Country"].value_counts()
    
    maxmag = df[df["Country"] == c]["Mag"].max()
    dat = df[df["Mag"] == maxmag & df["Country"] == c]["Mag","Year","Mo","Dy","Hr","Mn","Sec"]
    
    print(num)
    print(dat)
    
for i in df["Country"]:
    Count_LargestEq(i)