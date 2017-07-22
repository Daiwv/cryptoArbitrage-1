#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:52:07 2017

@author: garrettlee
"""
import poloniex
import cryptopia
import bittrex
import liqui

import time

poloniexPairs = {'augur-tether': 'USDT_REP', 'dash-tether': 'USDT_DASH', 'ethereum classic-tether': 'USDT_ETC', 'ethereum-tether': 'USDT_ETH', 'litecoin-tether': 'USDT_LTC', 'monero-tether': 'USDT_XMR', 'nxt-tether': 'USDT_NXT', 'ripple-tether': 'USDT_XRP', 'bitcoin-tether': 'USDT_BTC', 'zcash-tether': 'USDT_ZEC'}
cryptopiaPairs = {'ark-tether': 'ARK_USDT', 'bitcoin-tether': 'BTC_USDT', 'bitsend-tether': 'BSD_USDT', 'chaincoin-tether': 'CHC_USDT', 'dash-tether': 'DASH_USDT', 'decred-tether': 'DCR_USDT', 'dogecoin-tether': 'DOGE_USDT', 'dotcoin-tether': 'DOT_USDT', 'ethereum classic-tether': 'ETC_USDT', 'ethereum-tether': 'ETH_USDT', 'hush-tether': 'HUSH_USDT', 'inpay-tether': 'INPAY_USDT', 'litecoin-tether': 'LTC_USDT', 'monero-tether': 'XMR_USDT', 'navcoin-tether': 'NAV_USDT', 'nzed-tether': 'NZDT_USDT', 'pivx-tether': 'PIVX_USDT', 'skycoin-tether': 'SKY_USDT', 'unobtanium-tether': 'UNO_USDT', 'waves-tether': 'WAVES_USDT', 'zcash-tether': 'ZEC_USDT'}
bittrexPairs = {'bitcoin-tether': 'USDT-BTC', 'ethereum classic-tether': 'USDT-ETC', 'ethereum-tether': 'USDT-ETH', 'litecoin-tether': 'USDT-LTC', 'ripple-tether': 'USDT-XRP', 'zcash-tether': 'USDT-ZEC'}
liquiPairs = {'litecoin-tether': 'ltc_usdt', 'bitcoin-tether': 'btc_usdt', 'dash-tether': 'dash_usdt', 'ethereum-tether': 'eth_usdt', 'iconomi-tether': 'icn_usdt', 'golem-tether': 'gnt_usdt', 'waves-tether': 'waves_usdt', 'gnosis-tether': 'gno_usdt'}


usePairs = [liquiPairs, bittrexPairs, cryptopiaPairs, poloniexPairs]

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

def check(coin):
    asks, bids = aggregateOrders(coin)
    try:
        if max(bids) > min(asks) and max(bids)-min(asks) >= .001:
            print('YASSSSS')
            print(max(bids)-min(asks))
            return (coin,max(bids)-min(asks))
        else:
            print('no')
    except:
        print('Error')

def makeMoney(listOfPairs, times=5):
    winners = []
    for i in range(times):
        for group in listOfPairs:
            for token in group.keys():
                winner = check(token)
                if winner:
                    winners.append(winner)
                time.sleep(15)
    return winners
