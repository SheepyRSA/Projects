# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 10:04:29 2024

@author: Wentz
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_prices = pd.read_csv("petrolprices.csv",sep=";")
df = df_prices.copy()
first15= df.head()
print('Q1.A')
print(first15)
print('\n')

df2 = df.set_index(['Year','Month'])
print('Q1.B')
print(df2.head())
print('\n')
"""Indexing examples was accessed online 13/06/2024:
https://sparkbyexamples.com/pandas/pandas-set-index-explained-with-examples/#:~:text=By%20using%20set_index()%20method,index%20with%20default%20numeric%20values."""

def price_dif(row):
    answer = 0.0
    if row['Petrol'] > row['Diesel']: 
         answer += row['Petrol'] - row['Diesel']
    elif row['Diesel'] > row['Petrol']:
         answer += row['Diesel'] - row['Petrol'] 
    return answer

"df3 = df.apply(price_dif, axis=1)"
"print(df3)"
df2['Price Difference'] = df2.apply(price_dif, axis=1)
print('Q1.C')
print(df2.head())
print('\n')

print('Q1.D')
year2023 = df2.loc[[2023]]
print(year2023)
print('\n')
year2024 = df2.loc[[2024]]
print(year2024)
print('\n')

fig, axes = plt.subplots(figsize=(6,4))
dif23 = df[df['Year'] == 2023]
dif23 = pd.pivot_table(dif23, index="Month", columns=['Year'])
dif23 = dif23.reindex(['January', 'February', 'March', 'April', 'May', 'July', 'August', 'September', 'October', 'November', 'December'])
plt.title('2023 Year Petrol and Diesel prices')
dif23.plot(ax=axes)

fig, axes2 = plt.subplots(figsize=(6,4))
dif24 = df[df['Year'] == 2024]
dif24 = pd.pivot_table(dif24, index="Month", columns=['Year'])
dif24 = dif24.reindex(['January', 'February', 'March', 'April', 'May', 'July', 'August', 'September', 'October', 'November', 'December'])
plt.title('2024 Year Petrol and Diesel prices')
dif24.plot(ax=axes2)

fig, axes3 = plt.subplots(figsize=(6,4))
dif23 = pd.pivot_table(df, index="Month", columns=['Year'])
dif23 = dif23.reindex(['January', 'February', 'March', 'April', 'May', 'July', 'August', 'September', 'October', 'November', 'December'])
plt.title('2023/2024 Year Petrol and Diesel prices') 
dif23.plot(ax=axes3)

fig, axes3 = plt.subplots(figsize=(6,4))
priceDif = pd.pivot_table(df2, values ='Price Difference', index="Month", columns=['Year'])
priceDif = priceDif.reindex(['January', 'February', 'March', 'April', 'May', 'July', 'August', 'September', 'October', 'November', 'December'])
plt.title('Price differences between Petrol and Diesel in 2023/2024')
priceDif.plot(ax=axes3)

"""Pivot tables accessed online 13/06/2024:
https://www.geeksforgeeks.org/python-pandas-pivot_table/"""
"""Subplot accessed online 13/06/2024
https://www.w3schools.com/python/matplotlib_subplot.asp"""