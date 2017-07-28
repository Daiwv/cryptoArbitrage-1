#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 14:25:30 2017

@author: garrettlee
"""

#Import all teh goodies :)
import api.kraken as kraken
import api.poloniex as poloniex
import api.cryptopia as cryptopia
import api.bittrex as bittrex
import pandas as pd
import numpy as np
import time
from twilio.rest import Client

#information for messaging
sid, auth = 'ACab5ed88cf08f4d2df63791bfe06c47c6', 'e5cf603faa88be60621654aaf8ce2e92'
cli = Client(sid,auth)
myTwilioNumber, myCellPhone = '+13178544873', '+13176905477'

#import api dictionaries and pairs of coins that overlap :)
dicts = eval(open('dictionaries.txt', 'r').read())
krakenPairs, poloniexPairs, cryptopiaPairs, bittrexPairs = dicts['kraken'], dicts['poloniex'], dicts['cryptopia'], dicts['bittrex']
overlapPairs = ['verium-bitcoin', 'bitcoindark-bitcoin', 'transfercoin-bitcoin', 'stratis-bitcoin', 'incent-bitcoin', 'evergreencoin-bitcoin', 'gamecredits-bitcoin', 'nautiluscoin-bitcoin', 'safeexchangecoin-bitcoin', 'lisk-bitcoin', 'dogecoin-bitcoin', 'golem-bitcoin', 'dnotes-bitcoin', 'nubits-bitcoin', 'navcoin-bitcoin', 'potcoin-bitcoin', 'nxt-bitcoin', 'primecoin-bitcoin', 'melon-bitcoin', 'magi-bitcoin', 'litecoin-bitcoin', 'waves-bitcoin', 'augur-bitcoin', 'zcoin-bitcoin', 'namecoin-bitcoin', 'pinkcoin-bitcoin', 'ark-bitcoin', 'goldcoin-bitcoin', 'pivx-bitcoin', 'neweconomymovement-bitcoin', 'pascalcoin-bitcoin', 'rubycoin-bitcoin', 'bata-bitcoin', 'vcash-bitcoin', 'viacoin-bitcoin', 'reddcoin-bitcoin', 'lbry credits-bitcoin', 'clams-bitcoin', 'influxcoin-bitcoin', 'musicoin-bitcoin', 'zcash-tether', 'radium-bitcoin', 'startcoin-bitcoin', 'ubiq-bitcoin', 'geocoin-bitcoin', 'verge-bitcoin', 'zcash-bitcoin', 'dash-bitcoin', 'zclassic-bitcoin', 'unbreakablecoin-bitcoin', 'peercoin-bitcoin', 'digibyte-bitcoin', 'burst-bitcoin', 'syndicate-bitcoin', 'ardor-bitcoin', 'counterparty-bitcoin', 'bitsend-bitcoin', 'unobtanium-bitcoin', 'emercoin-bitcoin', 'nexium-bitcoin', 'groestlcoin-bitcoin', 'ethereum classic-bitcoin', 'boolberry-bitcoin', 'blackcoin-bitcoin', 'cloakcoin-bitcoin', 'einsteinium-bitcoin', 'bitcoin-tether', 'expanse-bitcoin', 'factom-bitcoin', 'okcash-bitcoin', 'bitshares-bitcoin', 'bitbean-bitcoin', 'gnosis-bitcoin', 'cannabiscoin-bitcoin', 'maidsafecoin-bitcoin', 'decred-bitcoin', 'komodo-bitcoin', 'syscoin-bitcoin', 'vertcoin-bitcoin', 'auroracoin-bitcoin', 'nexus-bitcoin', 'gridcoin-bitcoin', 'bitcrystals-bitcoin', 'vericoin-bitcoin', 'ethereum-bitcoin', 'monero-bitcoin', 'byteball-bitcoin', 'steem-bitcoin', 'siacoin-bitcoin', 'ripple-bitcoin', 'feathercoin-bitcoin']

#Pull in all information for a specific coin pair
def aggregate(coinPair):
    asks, bids = [], []
    print("-----Trying "+ coinPair[0:-8].capitalize()+"-----")
    try:
        pAsk, pBid = poloniex.top5(poloniexPairs[coinPair])
        asks += pAsk
        bids += pBid
        print("Success: Poloniex")
    except:
        print("Failure: Poloniex")
        
    try:
        kAsk, kBid = kraken.top5(krakenPairs[coinPair])
        asks += kAsk
        bids += kBid
        print("Success: Kraken")
    except: 
        print("Failure: Kraken")
        
    try:
        cAsk, cBid = cryptopia.top5(cryptopiaPairs[coinPair])
        asks += cAsk
        bids += cBid
        print("Success: Cryptopia")
    except:
        print("Failure: Cryptopia")
        
    try:
        bAsk, bBid = bittrex.top5(bittrexPairs[coinPair])
        asks += bAsk
        bids += bBid
        print("Success: Bittrex")
    except:
        print("Failure: Bittrex")
        
    
    try:
        asks, bids = pd.DataFrame(asks), pd.DataFrame(bids)
        asks.columns, bids.columns = ['Price', 'Quantity', 'Exchange'], ['Price', 'Quantity', 'Exchange']
    except:
        asks, bids = pd.DataFrame([]), pd.DataFrame([])
    return asks, bids

def checkForDifference(coin, percentThreshold = 5, volumeThreshold = 0.05):

    try:
        asks, bids = aggregate(coin)
        askPrices, bidPrices = asks['Price'], bids['Price']
        #Get difference information
        avg = np.mean(askPrices+bidPrices)/2
        maximum = bidPrices.idxmax()
        minimum = askPrices.idxmin()
        diff = bidPrices[maximum]-askPrices[minimum]
        pct = (diff/avg)*100
        
        #if the percentages is above the threshold, then report it
        if pct >= percentThreshold:
            print('Discrepency\nChecking volume...')

            cheap = asks['Exchange'][minimum]
            expensive = bids['Exchange'][maximum]
            
            #Check if the first transaction has sufficient volume            
            bidVolume = bidPrices[maximum]*bids['Quantity'][maximum]
            askVolume = askPrices[minimum]*asks['Quantity'][minimum]            
            if bidVolume >= 0.05 and askVolume >= 0.05:
                print('Volume Sufficient')
                print('Buying', coin[0:-8])
                return {'coin':coin, 'percent difference': pct, 'price sold':bidPrices[maximum], 'price paid':askPrices[minimum], 'cheap exchange':cheap, 'expensive exchange':expensive}
            else:
                print('Volume insufficient\nChecking other orders...')
                
                #Get the orders specific to the relevant exchanges
                exchangeBids = bids.loc[bids['Exchange'] == expensive]
                exchangeAsks = asks.loc[asks['Exchange'] == cheap]
                
                #get the bid volume and the prices
                maxBidVolume = np.sum(exchangeBids['Price']*exchangeBids['Quantity'])
                maxAskVolume = np.sum(exchangeAsks['Price']*exchangeAsks['Quantity'])
                avgBidPrice = maxBidVolume/np.sum(exchangeBids['Quantity'])
                avgAskPrice = maxAskVolume/np.sum(exchangeAsks['Quantity'])
                
                pctDifference = (avgBidPrice - avgAskPrice)/((avgBidPrice+avgAskPrice)/2)*100
                
                #if we can still get over the pct difference and volume, we buy sill
                if pctDifference > percentThreshold and maxBidVolume > 0.05 and maxAskVolume > 0.05:
                    print('Other orders still meet volume and price criteria')
                    print('Buying', coin[0:-8])
                    
                    return {'coin':coin, 'percent difference': pctDifference, 'price sold':avgBidPrice, 'price paid':avgAskPrice, 'cheap exchange':cheap, 'expensive exchange':expensive}
                print('Volume or percent low. Only bid:', maxBidVolume, '& ask:', maxAskVolume, 'worth at', pctDifference, 'percent.')
        #otherwise, just ignore
        else: 
            print('No Discrepency')
    except:
        print('Error')

def searchSpace(searchSpace = overlapPairs, sleepTime=30, messaging = True, pct=5, volume=0.05):  
    while True:                
        for pair in searchSpace:
            check = checkForDifference(pair, pct, volume)
            if check and messaging:
                    body = '\n' + check['coin'][0:-8]+' has a discrepency of '+str(check['percent difference'])+'%. It is cheap on '+check['cheap exchange']+' and expensive on '+check['expensive exchange']
                    cli.messages.create(body=body, from_=myTwilioNumber, to=myCellPhone)
                    print('\n-----MESSAGE SENT-----\n')
            print()
            time.sleep(sleepTime)
 
       
#searchSpace(pct=5, volume=.05, sleepTime=60)
#a,b = aggregate('ethereum-bitcoin')