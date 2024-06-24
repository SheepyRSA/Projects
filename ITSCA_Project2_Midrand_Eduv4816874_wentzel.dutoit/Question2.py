# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 14:13:32 2024

@author: Wentz
"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from textblob import TextBlob

df = pd.read_csv("music_album_reviews.csv",sep=";")
review = df['Review']
ratingVis = pd.pivot_table(df, values='Rating', index='Rating', aggfunc='count')
ratingVis.plot(kind='pie', subplots=True, figsize=(10, 10), autopct='%1.0f%%', startangle=60)
plt.legend('', frameon=False)
plt.show()
print ('The amount of simular ratings:')
print(ratingVis)
print ('\n')


text_review = df['Review'][75454]
print(text_review)

text_blob_object = TextBlob(df['Review'][75454]) 
print(text_blob_object.polarity)
"Textblob and polarity: https://textblob.readthedocs.io/en/dev/api_reference.html"

def sent_pol(row):
    if isinstance(row['Review'], str): 
        text_blob_object = TextBlob(row['Review']) 
        polarity = text_blob_object.polarity
        "polarity = str(polarity)"
        return polarity
    else:
        return None
    
"Check if zero or not accessed online 14/06/2024: https://stackoverflow.com/questions/28210060/check-if-value-is-zero-or-not-null-in-python"

df3 = df.apply(sent_pol, axis=1)
print(df3.head())

df['Polarity'] = df.apply(sent_pol, axis=1)

def pos_neg(row):
    answer = ""
    if row['Polarity'] > 0: 
         answer = "Positive"
    elif row['Polarity'] < 0:
         answer = "Negative"
    return answer

df4 = df.apply(pos_neg, axis=1)
print(df4.head())

df['Status'] = df.apply(pos_neg, axis=1)

print(df.head(15))

sns.countplot(x='Status', data=df)
plt.title('Polarity distribution')
plt.show()