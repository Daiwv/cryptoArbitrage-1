#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:52:07 2017

@author: garrettlee
"""
#Import everything
import poloniex
import cryptopia
import bittrex
import liqui
import time
import numpy as np
from twilio.rest import Client

#information for messaging
sid, auth = 'ACab5ed88cf08f4d2df63791bfe06c47c6', 'e5cf603faa88be60621654aaf8ce2e92'
cli = Client(sid,auth)
myTwilioNumber, myCellPhone = '+13178544873', '+13176905477'

#exchange API dictionaries & best keys to use
poloniexPairs = {'augur-tether': 'USDT_REP', 'dash-tether': 'USDT_DASH', 'ethereum classic-tether': 'USDT_ETC', 'ethereum-tether': 'USDT_ETH', 'litecoin-tether': 'USDT_LTC', 'monero-tether': 'USDT_XMR', 'nxt-tether': 'USDT_NXT', 'ripple-tether': 'USDT_XRP', 'bitcoin-tether': 'USDT_BTC', 'zcash-tether': 'USDT_ZEC'}
cryptopiaPairs = {'ark-tether': 'ARK_USDT', 'bitcoin-tether': 'BTC_USDT', 'bitsend-tether': 'BSD_USDT', 'chaincoin-tether': 'CHC_USDT', 'dash-tether': 'DASH_USDT', 'decred-tether': 'DCR_USDT', 'dogecoin-tether': 'DOGE_USDT', 'dotcoin-tether': 'DOT_USDT', 'ethereum classic-tether': 'ETC_USDT', 'ethereum-tether': 'ETH_USDT', 'hush-tether': 'HUSH_USDT', 'inpay-tether': 'INPAY_USDT', 'litecoin-tether': 'LTC_USDT', 'monero-tether': 'XMR_USDT', 'navcoin-tether': 'NAV_USDT', 'nzed-tether': 'NZDT_USDT', 'pivx-tether': 'PIVX_USDT', 'skycoin-tether': 'SKY_USDT', 'unobtanium-tether': 'UNO_USDT', 'waves-tether': 'WAVES_USDT', 'zcash-tether': 'ZEC_USDT'}
bittrexPairs = {'bitcoin-tether': 'USDT-BTC', 'ethereum classic-tether': 'USDT-ETC', 'ethereum-tether': 'USDT-ETH', 'litecoin-tether': 'USDT-LTC', 'ripple-tether': 'USDT-XRP', 'zcash-tether': 'USDT-ZEC'}
liquiPairs = {'litecoin-tether': 'ltc_usdt', 'bitcoin-tether': 'btc_usdt', 'dash-tether': 'dash_usdt', 'ethereum-tether': 'eth_usdt', 'iconomi-tether': 'icn_usdt', 'golem-tether': 'gnt_usdt', 'waves-tether': 'waves_usdt', 'gnosis-tether': 'gno_usdt'}
keys = ['litecoin-tether', 'bitcoin-tether', 'ethereum-tether','dash-tether', 'monero-tether', 'ripple-tether', 'zcash-tether']

#This function pulls information from all exchanges based on a given coin pair
def aggregateOrders(coinPair):
    asks, bids = [], []
    try:
        pAsk, pBid = poloniex.topAskBid(poloniexPairs[coinPair])
        asks.append(pAsk)
        bids.append(pBid)
        print("Success: Poloniex - Ask:", pAsk, "Bid:",pBid)
    except:
        print("Failure: Poloniex")
        
    try:
        cAsk, cBid = cryptopia.topAskBid(cryptopiaPairs[coinPair])
        asks.append(cAsk)
        bids.append(cBid)
        print("Success: Cryptopia - Ask:", cAsk, "Bid:", cBid)
    except:
        print("Failure: Cryptopia")
        
    try:
        bAsk, bBid = bittrex.topAskBid(bittrexPairs[coinPair])
        asks.append(bAsk)
        bids.append(bBid)
        print("Success: Bittrex - Ask:", bAsk, "Bid:", bBid)
    except:
        print("Failure: Bittrex")
        
    try:
        lAsk, lBid = liqui.topAskBid(liquiPairs[coinPair])
        asks.append(lAsk)
        bids.append(lBid)
        print("Success: Liqui - Ask:", lAsk, "Bid:", lBid)
    except:
        print("Failure: Bittrex")

    return asks, bids

#This function checks to see if there's a discrepency
def checkForDifference(coin):
    asks, bids = aggregateOrders(coin)
    avg = np.mean(asks+bids)
    try:
        diff = max(bids)-min(asks)
        if diff >= .001:
            pct = diff/avg
            print(coin,'has discrepency of',diff,'which is',pct*100,'percent')
            return (coin, diff, pct)
        else:
            print('No Discrepency')
    except:
        print('Error')


def makeMoney(listOfPairs):
    winners = []
    while True:
        for token in listOfPairs:
            winner = checkForDifference(token)
            if winner:
                winners.append(winner)
                if winner[2] > .01:
                    body = winner[0]+' has discrepency of '+str(winner[1])+' which is '+str(winner[2]*100)+' percent'
                    message = cli.messages.create(body=body, from_=myTwilioNumber, to=myCellPhone)
                    print('\n-----MESSAGE SENT-----\n')
            time.sleep(15)
    return winners
