#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:49:02 2017

@author: garrettlee
"""

import requests

hitbtcPairs = {'bytecoin-bitcoin': 'BCNBTC', 'dash-bitcoin': 'DASHBTC', 'dogecoin-bitcoin': 'DOGEBTC', 'emercoin-bitcoin': 'EMCBTC', 'ethereum-bitcoin': 'ETHBTC', 'lisk-bitcoin': 'LSKBTC', 'litecoin-bitcoin': 'LTCBTC', 'nxt-bitcoin': 'NXTBTC', 'steem-bitcoin': 'STEEMBTC', 'nem-bitcoin': 'XEMBTC', 'monero-bitcoin': 'XMRBTC', 'ardor-bitcoin': 'ARDRBTC', 'zcash-bitcoin': 'ZECBTC', 'waves-bitcoin': 'WAVESBTC', 'iconomi-bitcoin': 'ICNBTC', 'gnosis-bitcoin': 'GNOBTC', 'monero-ethereum': 'XMRETH', 'ethereum classic-ethereum': 'ETCETH', 'dash-ethereum': 'DASHETH', 'zcash-ethereum': 'ZECETH', 'gnosis-ethereum': 'GNOETH', 'ripple-bitcoin': 'XRPBTC', 'strats-bitcoin': 'STRATBTC'}

def getOrders(pair):
    r = requests.get('https://api.hitbtc.com/api/1/public/'+pair+'/orderbook')
    return r.json()

def topAskBid(pair):
    orders = getOrders(pair)
    ask = float(orders['asks'][0][0])
    bid = float(orders['bids'][0][0])
    return ask, bid

a = requests.get('https://api.liqui.io/api/3/info').json()
for x in a['pairs']:
    if 'usdt' in x:
        print(x)