# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 00:29:13 2019

@author: Gonewiththewind
"""
#import pandas as pa

class FXForward(object):
    '''
    we use this class to price a trade of forward contract
    
    '''
    def _init_(self, pay_ccy, rec_ccy, pay_amt, rec_amt, date ):
        self.pay_ccy = pay_ccy
        self.rec_ccy = rec_ccy
        self.pay_amt = pay_amt
        self.rec_amt = rec_amt
        self.date = date
        
    def _repr_(self):
        result = ''
        result += 'pay: '+ self.pay_ccy + ' ' + str(self.pay_amt) + '\n'
        result += 'receive: '+ self.rec_ccy + ' ' + str(self.rec_amt) + '\n'
        result += str(self.date) + '\n'
        return result
    
    def pricingTheTrade(self, exchange_rate):
        ''' Give the price of the trade,give the ecxchange rates
        between the two currency legs on the exchange dates as an input'''
        
        if self.pay_ccy == 'EUR':
            return self.rec_amt - self.pay_amt/exchange_rate
        elif self.pay_ccy == 'GBP':
            return self.rec_amt / exchange_rate - self.pay_amt
        #wait for adding another kinds of currency

        
    def pricingEURGBP(self):
        '''Take an input of EUR/GBP DataFrame and return a DataFrame of
        valuations for the trade'''
        
        return
    
if __name__ == '__main__':
    FXForward._init_(FXForward,'GBP', 'GBP', 800, 800, '2014-10-24')
    print(FXForward._repr_(FXForward))
    print(FXForward.pricingTheTrade(FXForward,1))