#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:45:17 2017

@author: garrettlee
"""

import requests

def getOrders(pair):
    r = requests.get('https://poloniex.com/public?command=returnOrderBook&currencyPair='+pair)
    return r.json()

def topAskBid(pair):
    orders = getOrders(pair)
    ask = float(orders['asks'][0][0])
    bid = float(orders['bids'][0][0])
    return ask, bid