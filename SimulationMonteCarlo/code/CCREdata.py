# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:37:21 2019

@author: s1816623
"""

import pandas as pd
import os
import numpy as np
import scipy.stats as sp

def data():

 #load the whole data 
    dataBasic = pd.read_csv("./eurofxref-hist.csv")
 
 #get the EUR data with changed process with respect to GBP = 1
    dataEUR = dataBasic["GBP"]
    dataInUseForEUR = 1./dataEUR
 
 #form an in use dataframe
    index = ["Date","EUR","JPY","USD","GBP","CHF","AUD","CAD"]
    dataInUseTemp = dataBasic[["Date","JPY","USD","GBP","CHF","AUD","CAD"]]
 
    temp = 1/dataBasic["GBP"]
    dataForOtherTemp = dataBasic[["JPY","USD","GBP","CHF","AUD","CAD"]]
    dataForOtherTemp = dataForOtherTemp.mul(temp,axis = 0)
    dataForOtherTemp.insert(0,'EUR',dataInUseForEUR)
    dataForOtherTemp.insert(0,'Date',dataBasic['Date'])
    dataInTime = dataForOtherTemp
     
    dataInTime = dataInTime[dataInTime['Date'] < '2016-01-01']
    dataInTime = dataInTime[dataInTime['Date'] > '2012-12-31']
    dataWithoutTime = dataInTime[["EUR","JPY","USD","GBP","CHF","AUD","CAD"]]
    temp1 = dataWithoutTime
 #log returns 
    for i in range(len(index)-1):
        temp1[index[i+1]] = dataWithoutTime[index[i+1]]/dataWithoutTime[index[i+1]].shift(-1)
        temp1[index[i+1]] = np.log(temp1[index[i+1]])
    logReturn = temp1
    
    Corr = logReturn.corr
    stdOfEUR = sp.norm.std(logReturn['EUR'])
    
    
    
if __name__ == '__main__':
    data()