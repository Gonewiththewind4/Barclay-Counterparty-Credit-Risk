# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 00:29:13 2019

@author: Gonewiththewind
"""

class FXForward()：
    '''
    we use this class to price a trade of forward contract
    
    '''
    def _init_(self, currency, amount, date ):
        self.currency = currency
        self.amount = amount
        self.date = date
    
    def pricingTheTrade(self):
        ''' Give the price of the trade,give the ecxchange rates
        between the two currency legs on the exchange dates as an input'''
        return
        
    def pricingEURGBP(self):
        '''Take an input of EUR/GBP DataFrame and return a DataFrame of
        valuations for the trade'''
        
        return