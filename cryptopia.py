#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 18:51:47 2017

@author: garrettlee
"""

import requests

def getTicker():
    r = requests.get('https://www.cryptopia.co.nz/api/GetTradePairs')
    return r.json()

def getOrders(pair, depth='1'):
    r = requests.get('https://www.cryptopia.co.nz/api/GetMarketOrders/'+pair+'/'+depth)
    return r.json()

def topAskBid(pair):
    orders = getOrders(pair)['Data']
    ask = orders['Sell'][0]['Price']
    bid = orders['Buy'][0]['Price']
    return ask, bid

x = getTicker()
cryptopiaPairs = {}
for info in x['Data']:
    name = info['Currency'].lower()+'-'+info['BaseCurrency'].lower()
    if 'bitcoin' in name or 'ethereum' in name or 'tether' in name:
        cryptopiaPairs[name] = info['Label'].replace('/', '_')

