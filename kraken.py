#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 15 15:44:05 2017

@author: garrettlee
@documentation: https://www.kraken.com/en-us/help/api#general-usage
"""

import pprint
import requests



def getInformation():
    r = requests.get('https://api.kraken.com/0/public/AssetPairs')
    return r.json()

def getOrders(pair, depth):
    url = 'https://api.kraken.com/0/public/Depth?pair='+pair+'&count='+depth
    r = requests.get(url)
    return r.json()
    

    

#effectively just going to get this JSON information
#https://api.kraken.com/0/public/Depth?pair=XXBTZUSD&count=5
getOrders('XXBTZUSD', '5')

#getting the exchange's information
#info = getExchangeInformation()
#pprint.pprint(info)
#pairs = list(info['result'].keys())
