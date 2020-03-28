
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:50:48 2020

"""

# Prediction Simulation
import time
import Neuronal_class as ne
import numpy as np

# base import
import matplotlib as matplot
import matplotlib.pyplot as plt



real_time = False
capital = 10
start_capital = 10
buy_invest = []
sell_invest = []
trade = []
trade_type = None
type_price = None
percentage = None
tab_capital = []
tab_capital.append((0, capital))

for i in range(0, len(ne.x_test)):
    tmp = np.array([ne.x_test[i]])
    prediction = ne.model.predict(tmp)
    if prediction[:, 0] == max(prediction[0]):
        if trade_type is None and capital > 0:
            buy_invest.append((i, ne.test_base["bid"].loc[i]))
            trade.append((i, ne.test_base["bid"].loc[i]))
            trade_type = True
            type_price = "buy"
    if prediction[:, 1] == max(prediction[0]):
        if trade_type == True:
            newCap = trade.pop()
            val = capital / newCap[1]
            newCap = val * ne.test_base["bid"].loc[i]
            capital = newCap
            sell_invest.append((i, ne.test_base["bid"].loc[i]))
            trade_type = None
            tab_capital.append((i, capital))
            type_price = "sell"
            
    if real_time == True:
        time.sleep(1)
        clear_output(wait=True)
        
        fig = plt.figure(figsize=(16,8))
        ne.test_base["bid"].loc[0:i].plot()
        buy_invest_tmp = np.array(buy_invest)
        sell_invest_tmp = np.array(sell_invest)
        print("Capital Start amount : ", start_capital)
        if type_price is not None:
            print("actual action : ", type_price)
        if len(buy_invest)  > 0:
            plt.plot(buy_invest_tmp[:,0], buy_invest_tmp[:,1], "ro", label="buy")
        if len(sell_invest)  > 0:
            plt.plot(sell_invest_tmp[:,0], sell_invest_tmp[:,1], "go", label="sell")
        print("capital : ", capital)
        plt.grid()
        plt.legend()
        plt.show()

        fig = plt.figure(figsize=(8,4))
        tab_tmp = np.array(tab_capital)
        plt.plot(tab_tmp[:,0],tab_tmp[:,1], "g", label="capital")
        plt.grid()
        plt.legend()
        plt.show()
        
        
clear_output(wait=True)

time.sleep(1)
fig = plt.figure(figsize=(16,8))
buy_invest_tmp = np.array(buy_invest)
sell_invest_tmp = np.array(sell_invest)

ne.test_base["bid"].loc[0:i].plot()
if len(buy_invest)  > 0:
    plt.plot(buy_invest_tmp[:,0], buy_invest_tmp[:,1], "ro", label="buy")
if len(sell_invest)  > 0:
    plt.plot(sell_invest_tmp[:,0], sell_invest_tmp[:,1], "go", label="sell")

print("Capital Start amount : ", start_capital)
if type_price is not None:
    print("actual action : ", type_price)
print("capital end : ", capital)

plt.grid()
plt.legend()
plt.show()
        
fig = plt.figure(figsize=(16,8))
tab_tmp = np.array(tab_capital)
plt.plot(tab_tmp[:,0],tab_tmp[:,1], "g", label="capital")
plt.grid()
plt.legend()
plt.show()  


returns=0   
mean_return=[]
for i in range (0,len(buy_invest)):
    returns+=buy_invest[i]-sell_invest[i]
    mean_return.append(buy_invest[i]-sell_invest[i])
    
print("Return for test period=")
print(returns/capital)
print("Mean return for test period by operation=")
print(np.mean(mean_return)/capital)

=======
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 11:50:48 2020

"""

# Prediction Simulation
import time
import Neuronal_class as ne
import numpy as np
# base import

import matplotlib as matplot
import matplotlib.pyplot as plt
from IPython.display import clear_output



real_time = False
capital = 10
start_capital = 10
buy_invest = []
sell_invest = []
trade = []
trade_type = None
type_price = None
percentage = None
tab_capital = []
tab_capital.append((0, capital))

for i in range(0, len(ne.x_test)):
    tmp = np.array([ne.x_test[i]])
    prediction = ne.model.predict(tmp)
    if prediction[:, 0] == max(prediction[0]):
        if trade_type is None and capital > 0:
            buy_invest.append((i, ne.test_base["bid"].loc[i]))
            trade.append((i, ne.test_base["bid"].loc[i]))
            trade_type = True
            type_price = "buy"
    if prediction[:, 1] == max(prediction[0]):
        if trade_type == True:
            newCap = trade.pop()
            val = capital / newCap[1]
            newCap = val * ne.test_base["bid"].loc[i]
            capital = newCap
            sell_invest.append((i, ne.test_base["bid"].loc[i]))
            trade_type = None
            tab_capital.append((i, capital))
            type_price = "sell"
            
    if real_time == True:
        time.sleep(1)
        clear_output(wait=True)
        
        fig = plt.figure(figsize=(16,8))
        ne.test_base["bid"].loc[0:i].plot()
        buy_invest_tmp = np.array(buy_invest)
        sell_invest_tmp = np.array(sell_invest)
        print("Capital Start amount : ", start_capital)
        if type_price is not None:
            print("actual action : ", type_price)
        if len(buy_invest)  > 0:
            plt.plot(buy_invest_tmp[:,0], buy_invest_tmp[:,1], "ro", label="buy")
        if len(sell_invest)  > 0:
            plt.plot(sell_invest_tmp[:,0], sell_invest_tmp[:,1], "go", label="sell")
        print("capital : ", capital)
        plt.grid()
        plt.legend()
        plt.show()

        fig = plt.figure(figsize=(8,4))
        tab_tmp = np.array(tab_capital)
        plt.plot(tab_tmp[:,0],tab_tmp[:,1], "g", label="capital")
        plt.grid()
        plt.legend()
        plt.show()
        
        
clear_output(wait=True)

time.sleep(1)
fig = plt.figure(figsize=(16,8))
buy_invest_tmp = np.array(buy_invest)
sell_invest_tmp = np.array(sell_invest)

ne.test_base["bid"].loc[0:i].plot()
if len(buy_invest)  > 0:
    plt.plot(buy_invest_tmp[:,0], buy_invest_tmp[:,1], "ro", label="buy")
if len(sell_invest)  > 0:
    plt.plot(sell_invest_tmp[:,0], sell_invest_tmp[:,1], "go", label="sell")

print("Capital Start amount : ", start_capital)
if type_price is not None:
    print("actual action : ", type_price)
print("capital end : ", capital)

plt.grid()
plt.legend()
plt.show()
        
fig = plt.figure(figsize=(16,8))
tab_tmp = np.array(tab_capital)
plt.plot(tab_tmp[:,0],tab_tmp[:,1], "g", label="capital")
plt.grid()
plt.legend()
plt.show() 

returns=0   
mean_return=[]
for i in range (0,len(buy_invest)):
    returns+=buy_invest[i]-sell_invest[i]
    mean_return.append(buy_invest[i]-sell_invest[i])
    
print("Return for test period=")
print(returns/capital)
print("Mean return for test period by operation=")
print(np.mean(mean_return)/capital)

