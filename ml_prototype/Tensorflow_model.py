# import pandas as pd
# import numpy as np
# import matplotlib as plt
# import tensorflow as tf
# import mplfinance as mpf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import SimpleRNN, Dense, Dropout, LSTM, GRU
# from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten

from PIL import Image
import os
import numpy as np
import seaborn as sns
from tensorflow.keras.models import Sequential, save_model
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def load_images_from_folder(folder, label):
    images = []
    try:
        for filename in os.listdir(folder):
            img_path = os.path.join(folder, filename)
            if os.path.isfile(img_path):
                with Image.open(img_path) as img:
                    img = img.resize((224, 224))  # Resize images to a fixed size
                    img = np.array(img)
                    if img.shape[2] == 4:
                        img = img[:, :, :3]  # Drop alpha channel if exists
                    images.append(img)
    except PermissionError as e:
        print(f"PermissionError: {e}")
        return None
    except Exception as e:
        print(f"Error loading images: {e}")
        return None
    
    print(f"Loaded {len(images)} images from '{label}' folder.")
    return np.array(images)

# Define your dataset directory
dataset_dir = 'F:\\ml_prototype\\GoldStockPhotos'

# Load images from 'up' and 'down' folders
up_folder = os.path.join(dataset_dir, 'up')
down_folder = os.path.join(dataset_dir, 'down')

images_up = load_images_from_folder(up_folder, 'up')
images_down = load_images_from_folder(down_folder, 'down')

# Concatenate images from both 'up' and 'down' folders
X = np.concatenate([images_up, images_down], axis=0)
y = np.concatenate([np.ones(len(images_up)), np.zeros(len(images_down))], axis=0)  # Assuming binary classification

# Ensure images have 3 channels (RGB)
assert X.shape[3] == 3, "Input images should have 3 channels (RGB)"

# Normalize pixel values to [0, 1]
X = X.astype('float32') / 255.0

X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Define your CNN model
model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1, activation='sigmoid')  # Example output layer for binary classification
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Print model summary
model.summary()

# Example: Fit the model (you need to split your data into train and validation sets)
model.fit(X_train, y_train, epochs=50, validation_data=(X_val, y_val), batch_size= 16)

# Save the model
model.save('my_cnn_model(1).keras')

"""
# To Save the model: (old way)
model.save('my_cnn_model.h5')

# new way to save: (End of CNN)
model.save('my_cnn_model.keras')

# RNN NETWORK
"physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    tf.config.experimental.set_memory_growth(physical_devices[0], True)
print("Num GPUs Available:", len(tf.config.experimental.list_physical_devices('GPU')))

# SORTING AND CHANGING DATA: Load and preprocess data
columns = ['time', 'open', 'high', 'low', 'close']
df = pd.read_csv("Gold_Stock.csv", sep=";", usecols=columns, parse_dates=["time"])
df = df[columns].set_index("time")
#df = df.drop(['tick_volume','spread', 'real_volume'], axis=1)
print(df)

chunk_size = 6

for i in range(0, len(df), chunk_size):
    chunk = df.iloc[i:i+chunk_size]
    
    # Check if it's the 6th chunk and determine color
    if len(chunk) >= 6:
        close_5th = chunk.iloc[4]['close']
        close_6th = chunk.iloc[5]['close']
        
        if close_6th < close_5th:
            filename = f"DOWN_{i}.png"
        else:
            filename = f"UP_{i}.png"
    else:
        continue
    
    mpf.plot(chunk, type="candle", style="yahoo", savefig=filename)

df['time'] = pd.to_datetime(df['time'], format='%Y/%m/%d %H:%M')
df['timestamp'] = df['time'].astype(np.int64) // 10**9  # Convert to Unix timestamp in seconds

# Extract date components
df['year'] = pd.to_datetime(df['time']).dt.year
df['month'] = pd.to_datetime(df['time']).dt.month
df['day'] = pd.to_datetime(df['time']).dt.day
df['hour'] = pd.to_datetime(df['time']).dt.hour


# Function to determine trend
def high_low(row):
    if row['open'] > row['close']: 
         return 0  # Downward
    elif row['open'] < row['close']:
         return 1  # Upward
    else:
         return 0  # No change (you can adjust this based on your needs)

# Apply function to create 'trend' column
df['trend'] = df.apply(high_low, axis=1)


# Add tick volume (tick rate) as a new feature
# Assuming 'tick_volume' is a column in your original CSV
df['tick_volume'] = df['tick_volume']  # Adjust this to your actual tick volume data

# Prepare X and Y
X = df[['open', 'high', 'low', 'tick_volume']].values 
Y = df['trend'].values

# Set a random seed for reproducibility
np.random.seed(42)

# Define the number of time steps
n_steps = 10
n_features = 4  

# Reshape X to [samples, timesteps, features]
num_samples = len(X) - n_steps + 1
X_reshaped = np.zeros((num_samples, n_steps, n_features))

for i in range(num_samples):
    X_reshaped[i] = X[i:i+n_steps]

with tf.device('/GPU:0'):
    # Build the RNN model
    model = Sequential()
    model.add(GRU(32, activation='relu', input_shape=(n_steps, n_features)))
    model.add(Dense(64, activation='relu', input_shape=(10,)))  # Adjust input_shape as per your data
    model.add(Dense(256, activation='softmax'))  # Adjust number of neurons
    # model.add(Dense(512, activation='leaky_relu'))  # Adjust number of neurons
    # model.add(Dense(256, activation='softmax'))  # Adjust number of neurons
    # model.add(Dense(128, activation='elu'))  # Adjust number of neurons
    # model.add(Dense(64, activation='exponential'))  # Adjust number of neurons
    model.add(Dense(1, activation='sigmoid'))  # Output layer for binary classification
    
    # Compile the model
    model.compile(optimizer='adam', loss='mean_absolute_error', metrics=['accuracy'])

# Print model summary
model.summary()

# Train the model
model.fit(X_reshaped, Y[n_steps-1:], epochs=1000, verbose=1, batch_size= 2048)

# Function to predict trend direction
def predict_trend(open_val, high_val, low_val, tick_volume_val):
    latest_sequence = X[-n_steps:].copy()  # Assuming X is your original data
    latest_sequence[-1] = [open_val, high_val, low_val, tick_volume_val]  # Update the last sequence with new values

    # Reshape for prediction
    latest_sequence_reshaped = latest_sequence.reshape((1, n_steps, n_features))

    # Predict the trend for the latest sequence
    predicted_trend = model.predict(latest_sequence_reshaped)[0][0]

    # Interpret the prediction
    if predicted_trend >= 0.5:
        return "Upward"
    else:
        return "Downward"
    
# Predicting with new values
latest_open = 2324.83
latest_high = 2327.55
latest_low = 2322.92
latest_tick_volume = 5294

predicted_direction = predict_trend(latest_open, latest_high, latest_low, latest_tick_volume)
print(f"Predicted trend direction: {predicted_direction}")
"""