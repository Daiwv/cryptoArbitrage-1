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

x = getTicker()
pairs = {}
for info in x['Data']:
    name = info['Currency']+'-'+info['BaseCurrency']
    if 'Bitcoin' in name or 'Ethereum' in name:
        pairs[name] = info['Label'].replace('/', '_')


#a = getOrders(pairs['Dash-Bitcoin'], '1')

def topAskBid(pair):
    orders = getOrders(pair)['Data']
    ask = orders['Sell'][0]['Price']
    bid = orders['Buy'][0]['Price']
    return ask, bid

