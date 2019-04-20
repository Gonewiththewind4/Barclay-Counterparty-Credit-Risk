# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 00:29:13 2019

@author: Gonewiththewind
"""

from SimulationMonteCarlo.code.FXForward import FXForward

FXForward._init_(FXForward,'GBP', 'GBP', 800, 800, '2014-10-24')
#FXForward._init_('GBP', 'GBP', 800, 800, '2014-10-24')
print(FXForward._repr_(FXForward))
print(FXForward.pricingTheTrade(FXForward,1))