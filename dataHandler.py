#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:52:07 2017

@author: garrettlee
"""
import kraken
import poloniex
import cryptopia
import bitfinex

def aggregateOrders():
    pAsk, pBid = poloniex.topAskBid('BTC_ZEC')
    kAsk, kBid = kraken.topAskBid('XZECXXBT')
    cAsk, cBid = cryptopia.topAskBid('ZEC_BTC')
    bAsk, bBid = bitfinex.topAskBid('zecbtc')
    
    asks = [pAsk, kAsk, cAsk, bAsk]
    bids = [pBid, kBid, cBid, bBid]
    
    return asks, bids


a, b = aggregateOrders()

def check(asks,bids):
    if max(bids) > min(asks):
        print('YASSSSS')
        print(max(bids)-min(asks))
    else:
        print('no')

check(a,b)