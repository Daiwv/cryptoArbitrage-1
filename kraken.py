#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:44:05 2017

@author: garrettlee
@documentation: https://www.kraken.com/en-us/help/api#general-usage
"""

import requests

coins = ['DASHEUR', 'DASHUSD', 'DASHXBT', 'EOSETH', 'EOSEUR', 
'EOSUSD', 'EOSXBT', 'GNOETH', 'GNOEUR', 'GNOUSD', 'GNOXBT', 'USDTZUSD', 
'XETCXETH', 'XETCXXBT', 'XETCZEUR', 'XETCZUSD', 'XETHXXBT', 'XETHXXBT.d', 
'XETHZCAD', 'XETHZCAD.d', 'XETHZEUR', 'XETHZEUR.d', 'XETHZGBP', 'XETHZGBP.d',
 'XETHZJPY', 'XETHZJPY.d', 'XETHZUSD', 'XETHZUSD.d', 'XICNXETH', 'XICNXXBT',
 'XLTCXXBT', 'XLTCZEUR', 'XLTCZUSD', 'XMLNXETH', 'XMLNXXBT', 'XREPXETH',
 'XREPXXBT', 'XREPZEUR', 'XREPZUSD', 'XXBTZCAD', 'XXBTZCAD.d', 'XXBTZEUR',
 'XXBTZEUR.d', 'XXBTZGBP', 'XXBTZGBP.d', 'XXBTZJPY', 'XXBTZJPY.d', 'XXBTZUSD',
 'XXBTZUSD.d', 'XXDGXXBT', 'XXLMXXBT', 'XXLMZEUR', 'XXLMZUSD', 'XXMRXXBT',
 'XXMRZEUR', 'XXMRZUSD', 'XXRPXXBT', 'XXRPZCAD', 'XXRPZEUR', 'XXRPZJPY',
 'XXRPZUSD', 'XZECXXBT', 'XZECZEUR', 'XZECZUSD']

def getOrders(pair, depth):
    url = 'https://api.kraken.com/0/public/Depth?pair='+pair+'&count='+depth
    r = requests.get(url)
    return r.json()
    
def topAskBid(pair):
    orders = getOrders(pair, '1')['result'][pair]
    ask = float(orders['asks'][0][0])
    bid = float(orders['bids'][0][0])
    return ask, bid
