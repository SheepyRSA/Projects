from datetime import datetime
import time
import sys
import MetaTrader5 as mt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import mplfinance as mpf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

mt.initialize()

login = 25121304
password = '@G<E!#*oV4/M'
server = 'Tickmill-Demo'

mt.login(login, password, server)

if not mt.initialize():
    print("initialize() failed, error code =",mt.last_error())
    sys.exit()
    
#'XAUUSD'
prices = {}
date_from = datetime(2014,1,10)

print('Insert your symbol')
symbol = input()
print('\n')

print('Which time basis would you like?')
print('1 = 1 minute intervals')
print('2 = 5 minute intervals')
print('3 = 30 minute intervals')
timechosen = int(input())

if timechosen != 0 and timechosen == 1:
    timeframe = mt.TIMEFRAME_M1
    interval = 60
    
elif timechosen == 2:
     timeframe = mt.TIMEFRAME_M5
     interval = 300
     
elif timechosen == 3:
     timeframe = mt.TIMEFRAME_M30
     interval = 1800
else:
    print('Invalid Number')
   
print('\n')
print(interval)
print(timeframe)

for i in range(1000000):
    rates = pd.DataFrame(mt.copy_rates_range(symbol, mt.TIMEFRAME_M1, date_from, datetime.now()))
    rates['time'] = pd.to_datetime(rates['time'], unit = 's')
    print(rates)
    #rates.to_csv('Gold_Stock.csv', sep=';', encoding='utf-8', index=False)
    
    print(rates[-1:])
    rates = pd.DataFrame(mt.copy_rates_from_pos(symbol, timeframe, 0, 15))
    rates['time'] = pd.to_datetime(rates['time'], unit = 's')
    print(rates)
    
    last10 = rates[-10:]
    last10 = last10.set_index("time")
    last10 = last10.drop(['spread', 'real_volume'], axis=1)
    last10.rename(columns={'tick_volume': 'volume'}, inplace=True)
    print(last10)
    filename = f'{symbol}.png'
    apdict = mpf.make_addplot(last10['low'])
    mc = mpf.make_marketcolors(up='g',down='r',
                           edge='inherit',
                           wick='black',
                           volume='in',
                           ohlc='i')
    s  = mpf.make_mpf_style(marketcolors=mc)

    # Plot each chunk separately
    mpf.plot(last10, mav=2, type='candle', style=s, volume=True, savefig=filename)
    mpf.plot(last10, mav=2, type='candle', style=s, volume=True)
    

    # Function to load and preprocess an image
    def load_and_preprocess_image(img_path, target_size=(224, 224)):
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to fit model input requirements
        img_array /= 255.0  # Normalize pixel values
        return img_array

    # Load the saved model
    saved_model = load_model('my_cnn_model.keras')

    # Path to new image for prediction
    img_path = f'F:\\ml_prototype\\{symbol}.png'

    # Load and preprocess the image
    img = load_and_preprocess_image(img_path)

    # Make predictions
    predictions = saved_model.predict(img)

    # Assuming it's a classification task with classes ['class1', 'class2', ...]
    # Example: Print predicted class probabilities
    print(predictions)

    # Get the predicted class label
    predicted_class = (predictions > 0.5).astype("int32")[0][0]  # Assuming threshold of 0.5 for binary classification
    print(f"Predicted class: {'up' if predicted_class == 1 else 'down'}")

    def interpret_trend(prediction):
        if prediction == 0:
            return "*******\nDownwards trend\n*******"
        elif prediction == 1:
            return "*******\nUpwards trend\n*******"
        else:
            return "*******\nUnknown trend\n*******"

    # Interpret the predicted class
    predicted_trend = interpret_trend(predicted_class)

    # Print the interpreted trend
    print("Predicted trend:\n", predicted_trend)
    time.sleep(interval)

