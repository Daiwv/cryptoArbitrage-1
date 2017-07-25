#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:06:54 2017

@author: garrettlee
"""

import dataHandler as DH
import requests

##Initialize all needed information
#pairs = DH.dicts
pBal, bBal, cBal = 0.1, 0.1, 0.1

def calculateFees(buyExchange, sellExchange, coin, amount):
    tradeFee = .25
    #calcuate fee to shift funds from buy exchange to sell exchange
    if buyExchange == 'cryptopia':
        transferFee = 1
    elif buyExchange == 'poloniex':
        transferFee = 1
    elif buyExchange == 'bittrex':
        transferFee = 1
    
    #calculate the fee needed to get equal BTC on all exchanges
    if sellExchange == 'cryptopia':
        balanceFee = 1
    elif sellExchange == 'poloniex':
        balanceFee = 1
    elif sellExchange == 'bittrex':
        balanceFee = 1
    
    totalFee = balanceFee + transferFee + 2*tradeFee
    return totalFee

x = requests.get('https://www.cryptopia.co.nz/api/GetCurrencies').json()
