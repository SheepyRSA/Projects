# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 17:48:25 2024

@author: Wentz
"""
import pandas as pd
import mplfinance as mpf

# Parameters
columns = ['time', 'open', 'high', 'low', 'close', 'tick_volume']
file_path = "Gold_Stock.csv"
output_folder_up = "F:\\ml_prototype\\GoldStockPhotos\\up\\"
output_folder_down = "F:\\ml_prototype\\GoldStockPhotos\\down\\"
chunk_size = 6

# Read data in chunks with explicit date format
reader = pd.read_csv(file_path, sep=";", usecols=columns, parse_dates=["time"], date_format='%Y-%m-%d %H:%M:%S', chunksize=chunk_size)

chunk_size = 6  # Adjust this to the desired chunk size
entries_to_display = 5  # Number of entries to display per plot

for i, chunk in enumerate(reader):
    # Skip processing if chunk size is less than expected
    if len(chunk) < chunk_size:
        continue
    
    chunk.rename(columns={'tick_volume': 'volume'}, inplace=True)
    # Set index to DatetimeIndex
    chunk.set_index('time', inplace=True)
      
    # Determine filename based on close prices
    close_5th = chunk.iloc[4]['close']
    close_6th = chunk.iloc[5]['close']
    
    if close_6th < close_5th:
        filename = f"{output_folder_down}DOWN_{i}.png"
    else:
        filename = f"{output_folder_up}UP_{i}.png"
    
    # Plotting logic
    num_plots = len(chunk) // entries_to_display
    
    for plot_num in range(num_plots):
        start_idx = plot_num * entries_to_display
        end_idx = start_idx + entries_to_display
        
        # Adjust end index if it exceeds chunk length
        if end_idx > len(chunk):
            end_idx = len(chunk)
        
        # Extract subset of data for this plot
        plot_chunk = chunk.iloc[start_idx:end_idx]
        
        # Create additional plot with volume and low as an addplot
        apdict = mpf.make_addplot(plot_chunk['low'])
        "mc = mpf.make_marketcolors(up='g', down='r', edge='inherit', wick='black', volume='in', ohlc='i')"
        "s = mpf.make_mpf_style(marketcolors=mc)"
        
        # Plot each chunk separately
        mpf.plot(plot_chunk, mav=2, type='candle', volume=True, savefig=filename)

"""
for i, chunk in enumerate(reader):
    # Skip processing if chunk size is less than expected
    if len(chunk) < chunk_size:
        continue
    
    chunk.rename(columns={'tick_volume': 'volume'}, inplace=True)
    # Set index to DatetimeIndex
    chunk.set_index('time', inplace=True)
      
    # Determine filename based on close prices
    close_5th = chunk.iloc[4]['close']
    close_6th = chunk.iloc[5]['close']
    
    if close_6th < close_5th:
        filename = f"{output_folder_down}DOWN_{i}.png"
    else:
        filename = f"{output_folder_up}UP_{i}.png"
    
    # Create additional plot with volume and low as an addplot
    apdict = mpf.make_addplot(chunk['low'])
    mc = mpf.make_marketcolors(up='g',down='r',
                           edge='inherit',
                           wick='black',
                           volume='in',
                           ohlc='i')
    s  = mpf.make_mpf_style(marketcolors=mc)

    # Plot each chunk separately
    mpf.plot(chunk.iloc[:5], mav=2, type='candle', style=s, volume=True, savefig=filename)
"""    