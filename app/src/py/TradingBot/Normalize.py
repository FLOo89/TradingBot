# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:25:31 2020


"""

# base import
import pandas as pd
import matplotlib as matplot

import numpy as np
import sklearn as sk

import sys

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer

from IPython.display import clear_output

#normalize class
class Normalisation():
    def __init__(self, data):
        self.__marketList = [e["name"] for e in data]
        self.__data = [e["data"] for e in data]
        self.__format = False
        
        
    def __norme_MinMax(self, target, numerical_markets):
        scaler = MinMaxScaler()
        normalized_markets = []
        if target == "all":
            for market in numerical_markets:
                columns_name= market.columns
                market[columns_name] = scaler.fit_transform(market[columns_name])
                normalized_markets.append(market.reset_index())
            self.__normalizeData = normalized_markets
        else:
            for marketName, market in zip(self.__marketList, numerical_markets):
                if marketName in target:
                    columns_name= market.columns
                    market[columns_name] = scaler.fit_transform(market[columns_name])
                    normalized_markets.append(market.reset_index())
            self.__normalizeData = normalized_markets
    
    def __norme_StandarScaler(self, target, numerical_markets):
        scaler = StandardScaler()
        normalized_markets = []
        if target == "all":
            for market in numerical_markets:
                columns_name= market.columns
                market[columns_name] = scaler.fit_transform(market[columns_name])
                normalized_markets.append(market.reset_index())
            self.__normalizeData = normalized_markets
        else:
            for marketName, market in zip(self.__marketList, numerical_markets):
                if marketName in target:
                    columns_name= market.columns
                    market[columns_name] = scaler.fit_transform(market[columns_name])
                    normalized_markets.append(market.reset_index())
            self.__normalizeData = normalized_markets
    
    def __norme_Normalizer_l(self, target, numerical_markets, norme):
        scaler = Normalizer(norme)
        normalized_markets = []
        if target == "all":
            for market in numerical_markets:
                columns_name= market.columns
                market[columns_name] = scaler.fit_transform(market[columns_name])
                normalized_markets.append(market)
            self.__normalizeData = normalized_markets
        else:
            for marketName, market in zip(self.__marketList, numerical_markets):
                if marketName in target:
                    columns_name= market.columns
                    market[columns_name] = scaler.fit_transform(market[columns_name])
                    normalized_markets.append(market.reset_index())
            self.__normalizeData = normalized_markets
            
    def fit(self, normeType, featuresList, target="all"):
        numerical_markets = []
        for market in self.__data:
            numerical_markets.append(market[featuresList]._get_numeric_data())
        if normeType == "MinMax":
            print("MinMax Normalization.")
            self.__norme_MinMax(target, numerical_markets)
            
        elif normeType == "StandarScale":
            print("StandarScale Normalization.")
            self.__norme_StandarScaler(target, numerical_markets)
        
        elif normeType == "Normalizer_l1":
            print("Normalizer_l1 Normalization.")
            self.__norme_Normalizer_l(target, numerical_markets, "l1")
        
        elif normeType == "Normalizer_l2":
            print("Normalizer_l2 Normalization.")
            self.__norme_Normalizer_l(target, numerical_markets, "l2")
    
    #return the data normalize
    def get_normalize_data(self, idx):
        return self.__normalizeData[idx]
