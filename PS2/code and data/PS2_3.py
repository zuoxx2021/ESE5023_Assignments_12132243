# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 17:20:10 2021

@author: 92303
"""

import pandas as pd

#loadfile
dam = pd.read_excel('GRanD_dams_v1_3.xlsx')

#clean data
dam1 = dam[dam['YEAR']>1900]
dam1

#Plot the time series of a certain variable.---------------------------------------------
#the number of dams built since 1900
dam1.groupby(dam['YEAR'])['YEAR'].count().plot()

#5 simple statistical check---------------------------------------------------------------
#Top 10 countries with the most DAMS
dam.groupby(dam['COUNTRY'])['COUNTRY'].count().sort_values(ascending=False).head(10)

#The name and country of the longest dam
dam[dam['DAM_LEN_M'] == dam['DAM_LEN_M'].max()][['COUNTRY','DAM_NAME','DAM_LEN_M']]

#The name and country of the deepest dam
dam[dam['DEPTH_M'] == dam['DEPTH_M'].max()][['COUNTRY','DAM_NAME','DEPTH_M']]

#The main use of these dams
dam.groupby(dam['MAIN_USE'])['MAIN_USE'].count().sort_values(ascending=False).head(10)

#The highest dam
dam[dam['ELEV_MASL'] == dam['ELEV_MASL'].max()][['COUNTRY','DAM_NAME','ELEV_MASL']]