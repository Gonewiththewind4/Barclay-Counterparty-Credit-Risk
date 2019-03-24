# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 11:37:21 2019

@author: s1816623
"""

import pandas as pd
#import os
import numpy as np
#import scipy.stats as sp
#import matplotlib.pyplot as plt
#import matplotlib as mpl
class data():
    '''
    This class is used to prepared all the data we need for next analysis
    '''
    #load the whole data 
#    def _init_(self,dataBasic,index,startTime,endTime):
#        self.dataBasic = dataBasic
#        self.index = index
#        self.startTime = startTime
#        self.endTime = endTIme
    
    index = ["Date","EUR","JPY","USD","GBP","CHF","AUD","CAD"]
    dataBasic = pd.read_csv("./eurofxref-hist.csv")
    #get the EUR data with changed process with respect to GBP = 1
    dataEUR = dataBasic["GBP"]
    dataInUseForEUR = 1./dataEUR
 
    #form an in use dataframe
    
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
    
    def getLogReturn(logReturn):
        '''Return the  log returns'''
        return logReturn
    
    def getDataWithoutTime(dataWithoutTime):
        '''Return the dataWithoutTime'''
        return dataWithoutTime
    
    def getCorr(logReturn):
        '''Return the Correlation matrix of log returns'''
        Corr = logReturn.corr
        return Corr
        
    def getGeneratedPath(logReturn):
        '''Return the generated path DataFrame (261 * 1000)'''
        stdOfEUR = logReturn['EUR'].std()
        pathRandom = stdOfEUR * np.random.standard_normal(261)
        path = pathRandom
        for j in range(1,261):
            path[j] = path[j-1] + pathRandom[j]
        MonteCarloPath = pd.DataFrame(path)
        for i in range(999):
            pathRandom = stdOfEUR * np.random.standard_normal(261)
            path = pathRandom
            for j in range(1,261):
                path[j] = path[j-1] + pathRandom[j]
            MonteCarloPath.insert(0,str(i+1),path)
        return MonteCarloPath
        
    
if __name__ == '__main__':
    print(data.logReturn)