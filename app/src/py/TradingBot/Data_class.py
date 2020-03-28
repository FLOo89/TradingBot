# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:37:15 2020

"""
import numpy as np
import Strategy_class as st
# Format Data functions
def generate_data(dataset, timestep, xcols, ycols):
    dx, dy = [], []
    for i in range(len(dataset) - timestep):
        a = dataset.iloc[i : i + timestep][xcols]
        dx.append(np.array(a))
        dy.append(dataset.iloc[i + timestep  - 1][ycols])
    return np.array(dx), np.array(dy)

def split_train(frame, train_per, test_per, timestep, xcols, ycols, balance=False):
    x_tmp, y_tmp = generate_data(frame, timestep, xcols, ycols)
    if balance is True:
        x_tmp, y_tmp =  st.balancelabelisation(x_tmp, y_tmp)
    train_size = int(x_tmp.shape[0] * train_per)
    test_size = int(x_tmp.shape[0] * test_per) + train_size

    x_train = x_tmp[: train_size]
    y_train = y_tmp[: train_size]
    x_test = x_tmp[train_size : test_size]
    y_test = y_tmp[train_size : test_size]
    return x_train, y_train, x_test, y_test