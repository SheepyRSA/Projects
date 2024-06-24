# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 21:24:03 2024

@author: Wentz
"""
#Question 1 Python Project for ITSCA2-12
#Class constructor method to initialise portfolio collection with 10000 balance available
class MoneyAvailable:
    def __init__(self, balance):
        self.balance = 10000.00
    
monBalance = MoneyAvailable(1)
guestAns = 1
portCat = {}
portCount = 0

def addStockFunc (dict1, count, name):
    stockCat = {}   
    addStock = int(input("How many stocks do you have? Please enter a number \n"))
    
    for i in range(addStock):
        key = input("Stock name: \n")
        value = input("Amount of shares: \n")
        value1 = value.replace(" ", "")
        value = float(value1)
        stockCat[key] = value
    print(stockCat)

    for i in range(count):
        key = name
        value = stockCat
        dict1[key] = value
    print(dict1)

print("*******************************************************")
print(str.upper("Welcome to your portfolio manager!"))
print("as a default 10 000.00 has been added to the account please remove this via the withdraw function if needed.")

while guestAns != 0:
    print("******************************************************* \n \n")
    print("(1)Would you like to create a portfolio? \n")
    print("(2)Would you like to buy shares? \n")
    print("(3)Would you like to sell shares? \n")
    print("(4)Would you like to deposit money? \n")
    print("(5)Would you like to withdraw money? \n")
    print("(6)View all portfolios \n")
    print("(7)View a specific portfolios \n")
    print("(8)Display balance \n")
    print("(0)Exit \n")
    
    choice = int(input("Which option would you want? please add the number as seen above \n"))
    if choice == 1:
        #New Portfolio and add to catalogue
        portF = input("Add new portfolio: \n")
        
        while bool(portF) == False:
            portF = input("Porfolio name not added, add portfolio name: \n") 
        else:
            print("Thank you for entering portfolio: " + portF)
            portCount += 1
            addStock = input("Would you like to add Stock? Y/N \n")
            
            if addStock == "Y" or addStock == "y":
                addStockFunc(portCat, portCount, portF)
            else:
                print("The porfolio will not be saved due to missing stock \n \n")
                continue
            
    elif choice == 2:
        customPort = input("for which portfolio would you like to add stock shares? \n")
        x = portCat[customPort]
        print(x)
        customStock = input("for which stock would you like to add shares? \n")
        y = x[customStock]
        print(y)
        buyShares = input("How many shares do you want to buy? \n")
        if monBalance.balance >= y:
            y = y + buyShares
            portCat[customPort][customStock] = y
            monBalance.balance = monBalance.balance - y
        else:
            print("*********** \n")
            print("Your current balance is: " + str(monBalance.balance) + " there is not enough to buy shares \n")
        continue   
             
    elif choice == 3:
        customPort = input("for which portfolio would you like to add stock shares? \n")
        a = portCat[customPort]
        print(a)
        customStock = input("for which stock would you like to add shares? \n")
        b = a[customStock]
        print(b)
        sellShares = input("How many shares do you want to sell? \n")
        if monBalance.balance >= b and b >= sellShares:
            b = b - sellShares
            portCat[customPort][customStock] = b
            monBalance.balance = monBalance.balance + b
        else:
            print("*********** \n")
            print("Your current balance is: " + str(monBalance.balance) + " there is not enough to shares to sell \n")
        continue
    
    elif choice == 4:
        addMon = float(input("Insert the amount you would like to deposit to the balance? \n"))
        monBalance.balance += addMon
        print("*********** \n")
        print("Your current balance is:" + str(monBalance.balance) + " \n")
        continue
    
    elif choice == 5:
        removeMon = float(input("Insert the amount you would like to withdraw to the balance? \n"))
        if monBalance.balance >= removeMon:
            monBalance.balance = monBalance.balance - removeMon
        else:
            print("*********** \n")
            print("Your current balance is: " + str(monBalance.balance) + " there is not enough to withdraw \n")
        continue
    
    elif choice == 6:
        #Display all portfolios
        print(" \n \n")
        print("*********** \n")
        print("Porfolio names:")
        print(*portCat.keys(), sep=", ")
        continue
    
    elif choice == 7:
        #Display spesific portfolio
        customPort3 = input("Which portfolio are you looking for? \n")
        x = portCat[customPort3]
        print("*********** \n")
        print(customPort3)
        print(x)
        continue
    
    elif choice == 8:
        #Display balance
        print("*********** \n")
        print(monBalance.balance)
        continue
    
    elif choice == 0:
        guestAns = 0
    else: 
        print("Not one of the advised numbers were selected. \n")
        continue

#Resources:
#https://www.copahost.com/blog/input-python/#:~:text=Input%20validation%20using%20the%20module,print("Entry%20is%20valid! Accessed online 05/03/2024
#https://www.youtube.com/watch?v=yYALsys-P_w Accessed online 05/03/2024
#https://www.youtube.com/watch?v=Jk31MDmtuU4 Accessed online 05/03/2024
#https://stackoverflow.com/questions/14147369/make-a-dictionary-in-python-from-input-values Accessed online 06/03/2024
#https://bobbyhadz.com/blog/python-add-user-input-to-dictionary Accessed online 06/03/2024
#https://www.scaler.com/topics/list-of-dictionaries-in-python/ Accessed online 06/03/2024
#https://www.w3schools.com/python/python_dictionaries_nested.asp Accessed online 07/03/2024
#https://blog.finxter.com/python-print-dictionary-keys-without-dict_keys/#:~:text=An%20easy%20and%20Pythonic%20way,single%20whitespace%20character%20per%20default. Accessed online 07/03/2024
#https://www.w3schools.com/python/python_classes.asp Accessed online 08/03/2024

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1,2,3,4,5])
A = np.array([])

#Question 2
#2.1
df_books = pd.read_csv("Books_Data.csv",sep=";")
df_fixed = df_books.copy()
first15= df_fixed.head(15)
print(first15)
#df_books.describe() # - mean, median etc.
#2.2
df_fixed.rename(columns={'index' : 'Index', 'Publishing Year' : 'publishingYear', 'Book Name' : 'bookName', 
                         'Author' : 'Author', 'language_code' : 'languageCode', 'Author_Rating' : 'authorRating',
                         'Book_average_rating' : 'bookAverageRating', 'Book_ratings_count' : 'bookRatingsCount',
                         'genre' : 'theGenre', 'gross sales' : 'grossSales', 'publisher revenue' : 'publisherRevenue',
                         'sale price' : 'salePrice', 'sales rank' : 'salesRank',  'Publisher ' : 'publisherName',
                         'units sold' : 'unitsSold'}, inplace=True)
print(df_fixed)
#2.3
missingNaN = df_fixed.isnull().sum(axis=1)
print("Total missing lines which was removed: " + str(missingNaN.sum())+"\n")
df_fixed.dropna(subset=['bookName'], inplace = True)
df_fixed.dropna(subset=['unitsSold'], inplace = True)
df_fixed.dropna(subset=['publisherName'], inplace = True)

#2.4
df_fixed['authorRating'].replace('Novice', 'Beginner', inplace=True)
df_fixed['authorRating'].replace('Intermediate', 'Intermediate', inplace=True)
df_fixed['authorRating'].replace('Famous', 'Expert', inplace=True)
df_fixed['authorRating'].replace('Excellent', 'Expert', inplace=True)

df_fixed['theGenre'].replace('children', 'Children', inplace=True)
df_fixed['theGenre'].replace('fiction', 'Fiction', inplace=True)
df_fixed['theGenre'].replace('genre fiction', 'Fiction', inplace=True)
df_fixed['theGenre'].replace('nonfiction', 'Non-Fiction', inplace=True)

#2.5
df_betterBooks = df_fixed.query('bookAverageRating >= 4')
df_betterBooks = df_betterBooks.sort_values(by='bookAverageRating', ascending=False)
df_betterBooks = df_betterBooks[['bookName', 'bookAverageRating']]
top10 = df_betterBooks.head(10)
print("The top 10 highest rating books are: \n")
print(top10)
print("\n")

#2.6
df_fixed["operatingCost"] = df_fixed['grossSales'] - df_fixed['publisherRevenue']
df_fixed.drop(['salesRank'], inplace=True, axis=1)
print(df_fixed)

#was used to test the above and to see if it worked:
#print(df_fixed['salesRank'].to_string(index=False)) - gave me an error because it was deleted.

#2.7
averageRating = pd.pivot_table(df_fixed, values='bookAverageRating', index='publisherName')
print(averageRating)
print('\n')

#2.8
meanSales = df_fixed["grossSales"].mean().round(2)
medianSales = df_fixed["grossSales"].median()
stdSales = df_fixed["grossSales"].std()
print("Mean Gross Sales:" + str(meanSales))
print("Median Gross Sales:" + str(medianSales))
print("Standard Deviantion Gross Sales:" + str(stdSales))

#2.9
df_fixed['publishingYear'] = df_fixed['publishingYear'].astype(str).str.replace('.0', ' ')
df_fixed = df_fixed.drop(df_fixed[df_fixed['publishingYear'].astype(int) < 1500].index)
print(df_fixed)

#Question 3

#3.a
df_highest = df_fixed[df_fixed['bookAverageRating'] >= 4]
df_highest = df_highest.sort_values(by=['bookAverageRating'], ascending=False)
df_highest = df_highest[['bookName', 'bookAverageRating']]
topTen = df_highest.head(10)
print("The top 10 highest rating books are: \n")
print(topTen)
print("\n")

#3.b
df_fixed.plot(kind = 'scatter', x = 'theGenre', y = 'grossSales')
plt.title("Sales across Genres")
plt.show()

#3.c
df_GenYear = df_fixed.copy()
df_GenYear = df_GenYear[df_GenYear['theGenre'] == "Fiction"]
df_GenYear = df_GenYear[['theGenre', 'publishingYear']]
df_GenYear['publishingYear'] = df_GenYear['publishingYear'].astype(int)
df_GenYear.plot(kind='hist') 
plt.title("Fiction across Years")
plt.xlabel("Years")
plt.legend('', frameon=False)
plt.show()

#3.d
countPub = pd.pivot_table(df_fixed, values='grossSales', index='publisherName', aggfunc="sum")
countPub.plot(kind='pie', subplots=True, figsize=(10, 10), autopct='%1.0f%%', startangle=60)
plt.legend('', frameon=False)
print("Publisher Total Sales")
print(countPub)
print("\n")

#3.e
df_HighPub = df_fixed.copy()
df_HighPub = df_HighPub[df_HighPub['publisherName'] == "Amazon Digital Services,  Inc."]
df_HighPub = df_HighPub[['theGenre', 'grossSales']]
highPub = pd.pivot_table(df_HighPub, values='grossSales', index='theGenre', aggfunc="sum")
print("Sales across Amazon Digital Services,  Inc. per Genre")
print(highPub)
print("\n")
highPub.plot(kind='pie', subplots=True, figsize=(10, 10), autopct='%1.0f%%', startangle=60) 


df_GenPub = df_fixed.copy()
df_GenPub = df_GenPub[['theGenre', 'grossSales']]
genPub = pd.pivot_table(df_GenPub, values='grossSales', index='theGenre', aggfunc="sum")
print("Sales across Genre")
print(genPub)
print("\n")
genPub.plot(kind='pie', subplots=True, figsize=(10, 10), autopct='%1.0f%%', startangle=60) 

print("There seems to be some correlation between the highest selling Publisher and the overall distribution of Genres. \n")

#3.f
ratingVsSales = pd.pivot_table(df_fixed, values='bookAverageRating', index='grossSales')
ratingVsSales.plot(kind='hist')
plt.xlabel("Book Rating")

print("The book rating does have a impact on gross sales but majority of the sales are made with a rating around 4.0. \n")

#3.g
ratingVsAuth = pd.pivot_table(df_fixed, values='bookAverageRating', index='authorRating')
plt.xlabel("Author Rating")
ratingVsAuth.plot(kind='line')
print(ratingVsAuth)

print("The book rating does seem to help the author rating. \n")

#https://www.w3schools.com/python/pandas/pandas_analyzing.asp Accessed Online: 10/03/2024
#https://www.w3schools.com/python/pandas/pandas_cleaning_empty_cells.asp Accessed Online: 10/03/2024
#https://saturncloud.io/blog/how-to-count-the-number-of-missingnan-values-in-each-row-in-python-pandas/ Accessed Online: 10/03/2024
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html Accessed Online: 11/03/2024
#https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html Accessed Online: 11/03/2024
#https://www.w3schools.com/python/pandas/pandas_plotting.asp Accessed Online: 11/03/2024
#https://pandas.pydata.org/docs/user_guide/reshaping.html Accessed Online: 12/03/2024
#https://www.statology.org/remove-legend-matplotlib/ Accessed Online: 12/03/2024