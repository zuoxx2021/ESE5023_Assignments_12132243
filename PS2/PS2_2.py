# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 21:40:39 2021

@author: 92303
"""

import pandas as pd

noaa = pd.read_csv('2281305.csv')
wind = noaa.loc[:,('DATE','WND')]
wind[['DA','DQC','TC','SR','SQC']] = wind['WND'].str.split(',',5,expand = True)

paqccwind = wind[wind["SQC"].astype('int') == 1]
paqccwind['DATE'] = pd.to_datetime(paqccwind['DATE'])
paqccwind['SR1'] = paqccwind['SR'].astype('int')
paqccwind.groupby([paqccwind['DATE'].dt.year,paqccwind['DATE'].dt.month])['SR1'].mean().plot()