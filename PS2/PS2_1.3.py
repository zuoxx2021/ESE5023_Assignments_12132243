# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 10:09:42 2021

@author: 92303
"""

import pandas as pd

df = pd.read_csv("Sig_Eqs.tsv",sep='\t')

countrylist = df['Country'].unique()
result = df[['Country','Mag','Year','Mo','Dy']].head(0)

def CountEq_LargestEq(a):
    df1 = df[df['Country'] == str(a)]
    df2 = df1[df1['Mag']==df1['Mag'].max()][['Country','Mag','Year','Mo','Dy']] 
    df2['total_number'] = df[df['Country'] == str(a)]['Country'].count()
    global result
    result = result.append(df2)
    

for i in countrylist:
    CountEq_LargestEq(i)
    
result = result.sort_values('total_number',ascending=False,ignore_index=True)