# -*- coding: utf-8 -*-

# base import
# base import
import pandas as pd
import matplotlib as matplot
import matplotlib.pyplot as plt
import numpy as np
import sklearn as sk
import os
import sys
import keras
import json
import yaml

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer

from IPython.display import clear_output
from keras.models import Sequential
from keras.layers import GRU
from keras.layers import Embedding, LSTM, Flatten,Dense, Dropout, Activation
from keras.utils import to_categorical
from keras.optimizers import SGD
from keras.callbacks import LearningRateScheduler
from IPython.display import clear_output
import h5py


import Normalize as no
import Strategy_class as st
import Data_class as dt


# Neural functions

def lstmNeuronsNumber(frame, setting):
    Ni = len(setting["labelisation_features_name"])
    No = len(setting["labelisation_labels_name"])
    Ns = frame.shape[0]
    a = setting["delta_neurons_numbers"]
    return int(Ns / (a * (Ni + No)))

class PlotRealTime(keras.callbacks.Callback):
    
    def on_train_begin(self, logs={}):
        self.i = 0
        self.x = []
        self.losses = []
        self.val_losses = []
        self.acc = []
        self.val_acc = []
        self.fig = plt.figure()
        self.logs = []

    def on_epoch_end(self, epoch, logs={}):

        self.logs.append(logs)
        self.x.append(self.i)
        self.acc.append(logs.get('acc'))
        self.val_acc.append(logs.get('val_acc'))
        self.losses.append(logs.get('loss'))
        self.val_losses.append(logs.get('val_loss'))
        self.i += 1
        clear_output(wait=True)
        plt.plot(self.x, self.acc, 'g', label="accuracy")
        plt.plot(self.x, self.val_acc, 'r', label="validation accuracy")
        plt.legend()
        plt.title("Accuracy percentage")
        plt.grid()
        plt.show()
        
        plt.plot(self.x, self.losses, label="loss")
        plt.plot(self.x, self.val_losses, label="val_loss")
        plt.legend()
        plt.title("Losses percentage")
        plt.grid()
        plt.show()
        

# noramlize: MinMax | StandarScale | Normalizer_l1 | Normalizer_l2 
settings = dict({"ticker_file": "tickers.csv",
                 "markets_target": ["BTC-NEO"],
                 "normalisation_fit_type": "StandarScale",
                 "normalisation_fit_target": "all",
                 "normalisation_target": "bid",
                 "labelisation_disparity": 0.065,
                 "labelisation_features_name": ["ask", "bid", "high", "low", "moy_prev_day"],
                 "labelisation_labels_name": ["buy", "sell", "wait"],
                 "is_balance": True,
                 "split_train": 0.7,
                 "split_test": 0.3,
                 "nb_per_bloc": 50,
                 "delta_neurons_numbers": 2, # delta {2-10}
                 "model_optimizer": "adam",
                 "model_loss": "mse",
                 "model_epoch": 70,
                 "model_batch_size": 50,
                 "model_validation_split": 0.1,
                 "model_suffle": True,
                 "model_evaluate_batch_size": 100
                })

# GET DATA
#data = get_data(settings["ticker_file"], settings["markets_target"])
data_path = os.getcwd() + "\\app\\src\\data\\BTC_NEO_100.csv"
data = pd.read_csv(data_path, delimiter = ",")
data = data.drop('Unnamed: 0', axis=1)

# Display
fig = plt.figure(figsize=(21,7))
data[0]["data"]["bid"].plot(label="bid", title="Bid curve")
plt.grid()
plt.legend()
plt.show()

# NORMALIZATION OF THE DATA
norm = no.Normalisation(data)
all_normalize_data = norm.fit(settings["normalisation_fit_type"], 
                              settings["labelisation_features_name"],
                              settings["normalisation_fit_target"])
normalize_data = norm.get_normalize_data(0)

# PEAKS DETECTION
peaksmax, peaksmin = st.peakdet(normalize_data[settings["normalisation_target"]], 
                                            settings["labelisation_disparity"])

# Display peaks
fig = plt.figure(figsize=(21,7))
plt.plot(peaksmax[:,0], peaksmax[:, 1], 'ro', label="Max peaks")
plt.plot(peaksmin[:,0], peaksmin[:, 1], 'go', label="Minimum peaks")
plt.plot(normalize_data["bid"], label="Bid")
plt.grid()
plt.title("Peaks detection")
plt.legend()
plt.show()

# Frame labelization

# LABELIZATION WITH PEAKS
normalize_data_tmp = st.frame_labelization(normalize_data, peaksmax, peaksmin, data)

# FORMAT DATA FOR MODEL
x_train, y_train, x_test, y_test = dt.split_train(normalize_data_tmp,
                                               settings["split_train"],
                                               settings["split_test"],
                                               settings["nb_per_bloc"],
                                               settings["labelisation_features_name"],
                                               settings["labelisation_labels_name"],
                                               balance=settings["is_balance"])
                                                     
                                                     
                                                     
# Model declaration
 
# SET NUMBER OF NEURONS
settings["model_lstm_neural"] = lstmNeuronsNumber(x_train, settings)  

# MODEL
model = Sequential()

model.add(
    LSTM(
        settings["model_lstm_neural"],
        input_shape=(x_train.shape[1],
        x_train.shape[2]),
        activation='tanh',
        return_sequences=True
        )
    )
    
model.add(
    LSTM(
        settings["model_lstm_neural"],
        activation='tanh'
        )
    )
    
model.add(Dense(y_train.shape[1], activation='softmax'))

model.compile(optimizer = settings["model_optimizer"],
              loss      = settings["model_loss"],
              metrics=['accuracy'])

model.summary()                                                    

# Training

# Plot real-time
plotRT = PlotRealTime()

# Learning stats
def lr(epoch):
    if epoch < 15:
        return 0.010
    if epoch < 40:
        return 0.0095
    if epoch < 55:
        return 0.008
    if epoch < 60:
        return 0.007
    if epoch < 150:
        return 0.01
    return 0.01
# TRAINING
hist = model.fit(x_train,
                 y_train, 
                 epochs=settings["model_epoch"],
                 batch_size=settings["model_batch_size"],
                 validation_split=settings["model_validation_split"],
                 verbose=1,
                 shuffle=settings["model_suffle"],
                 callbacks=[plotRT, LearningRateScheduler(lr, verbose=1)])
# EVALUATE
score , acc = model.evaluate(x_test, 
                             y_test, 
                             batch_size=settings["model_evaluate_batch_size"], 
                             verbose=1)

print("score: {}".format(score))
print("acc: {}".format(acc))


def base_frame_test(frame, train_per, test_per,):
    train_size = int(frame.shape[0] * train_per)
    test_size = int(frame.shape[0] * test_per) + train_size
    return frame.loc[train_size : test_size].reset_index()

test_base = base_frame_test(normalize_data_tmp,
                         settings["split_train"],
                         settings["split_test"])
                         
