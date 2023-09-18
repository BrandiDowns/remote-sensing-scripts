# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 17:27:47 2022

@author: brand
"""

import pandas as pd
import matplotlib.pyplot as plt
from joypy import joyplot
from pandas.api.types import CategoricalDtype

s1 = pd.read_csv(r"C:\Users\brand\Documents\matlab\cygnss\s1_nanda_bet_poly1.csv")
s1['date'] = s1['date'].astype('string')

print(s1.date.unique())


s1_dates = ['03-Jan-2020', '15-Jan-2020', '27-Jan-2020', '08-Feb-2020', '20-Feb-2020',
            '03-Mar-2020', '15-Mar-2020', '27-Mar-2020', '08-Apr-2020', '20-Apr-2020',
            '02-May-2020', '14-May-2020', '26-May-2020', '07-Jun-2020', '19-Jun-2020',
            '01-Jul-2020', '13-Jul-2020', '25-Jul-2020', '06-Aug-2020', '18-Aug-2020',
            '30-Aug-2020', '11-Sep-2020', '23-Sep-2020', '05-Oct-2020', '17-Oct-2020',
            '29-Oct-2020', '10-Nov-2020', '22-Nov-2020', '04-Dec-2020', '16-Dec-2020',
            '28-Dec-2020']

cat_date = CategoricalDtype(s1_dates)

s1['date'] = s1['date'].astype(cat_date)

print(s1.info())

s1.dtypes


#%% joyplot v1

plt.figure()
joyplot(data=s1[['vv_db', 'date']], by='date', figsize=(12,8), colormap = plt.cm.viridis, linecolor='w', linewidth=0.5)
plt.title('Ridgeline Plot', fontsize=20)
plt.show()


#%% joyplot v2

plt.figure()
joyplot(data=s1[['vv_db', 'date']], by='date', figsize=(12,8), grid=True, fill=False,
        background='w', linecolor='w', linewidth=2, xrange=[-35,0])
plt.title('Ridgeline Plot', fontsize=20)
plt.show()






