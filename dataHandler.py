#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 21:52:07 2017

@author: garrettlee
"""
import api.kraken as kraken
import api.poloniex as poloniex
import api.cryptopia as cryptopia
import api.bitfinex as bitfinex
import api.bittrex as bittrex
import api.xbtce as xbtce
import api.hitbtc as hitbtc
import time
import datetime
import numpy as np
import pandas as pd
from twilio.rest import Client

#information for messaging
sid, auth = 'ACab5ed88cf08f4d2df63791bfe06c47c6', 'e5cf603faa88be60621654aaf8ce2e92'
cli = Client(sid,auth)
myTwilioNumber, myCellPhone = '+13178544873', '+13176905477'

#Dictionaries for exchanges
file = open('dictionaries.txt', 'r')
dicts = eval(file.read())
bitfinexPairs = dicts['bitfinex']
krakenPairs = dicts['kraken']
poloniexPairs = dicts['poloniex']
cryptopiaPairs = dicts['cryptopia']
bittrexPairs = dicts['bittrex']
xbtcePairs = dicts['xbtce']
hitbtcPairs = dicts['hitbtc']        

##Lists of coins to iterate through
moneyMakers = ['verium-bitcoin', 'bitcoindark-bitcoin', 'transfercoin-bitcoin', 'stratis-bitcoin', 'incent-bitcoin', 'litecoin-tether', 'evergreencoin-bitcoin', 'gamecredits-bitcoin', 'nautiluscoin-bitcoin', 'safeexchangecoin-bitcoin', 'lisk-bitcoin', 'monero-tether', 'dogecoin-bitcoin', 'golem-bitcoin', 'dash-tether', 'dnotes-bitcoin', 'nubits-bitcoin', 'navcoin-bitcoin', 'potcoin-bitcoin', 'nxt-bitcoin', 'primecoin-bitcoin', 'melon-bitcoin', 'magi-bitcoin', 'litecoin-bitcoin', 'waves-bitcoin', 'augur-bitcoin', 'zcoin-bitcoin', 'namecoin-bitcoin', 'pinkcoin-bitcoin', 'ark-bitcoin', 'goldcoin-bitcoin', 'pivx-bitcoin', 'bytecoin-bitcoin', 'neweconomymovement-bitcoin', 'pascalcoin-bitcoin', 'rubycoin-bitcoin', 'bata-bitcoin', 'vcash-bitcoin', 'viacoin-bitcoin', 'reddcoin-bitcoin', 'lbry credits-bitcoin', 'clams-bitcoin', 'influxcoin-bitcoin', 'augur-ethereum', 'musicoin-bitcoin', 'ethereum classic-tether', 'zcash-tether', 'radium-bitcoin', 'startcoin-bitcoin', 'ethereum-tether', 'ubiq-bitcoin', 'geocoin-bitcoin', 'verge-bitcoin', 'zcash-bitcoin', 'dash-bitcoin', 'zclassic-bitcoin', 'unbreakablecoin-bitcoin', 'peercoin-bitcoin', 'digibyte-bitcoin', 'burst-bitcoin', 'syndicate-bitcoin', 'ardor-bitcoin', 'counterparty-bitcoin', 'bitsend-bitcoin', 'unobtanium-bitcoin', 'emercoin-bitcoin', 'nexium-bitcoin', 'groestlcoin-bitcoin', 'ethereum classic-bitcoin', 'boolberry-bitcoin', 'blackcoin-bitcoin', 'cloakcoin-bitcoin', 'einsteinium-bitcoin', 'bitcoin-tether', 'expanse-bitcoin', 'ethereum classic-ethereum', 'factom-bitcoin', 'zcash-ethereum', 'okcash-bitcoin', 'bitshares-bitcoin', 'ripple-tether', 'bitbean-bitcoin', 'gnosis-bitcoin', 'cannabiscoin-bitcoin', 'maidsafecoin-bitcoin', 'decred-bitcoin', 'komodo-bitcoin', 'syscoin-bitcoin', 'vertcoin-bitcoin', 'auroracoin-bitcoin', 'nexus-bitcoin', 'gridcoin-bitcoin', 'bitcrystals-bitcoin', 'vericoin-bitcoin', 'ethereum-bitcoin', 'monero-bitcoin', 'byteball-bitcoin', 'golem-ethereum', 'steem-bitcoin', 'siacoin-bitcoin', 'ripple-bitcoin', 'feathercoin-bitcoin', 'gnosis-ethereum']
usePairs = [bitfinexPairs, krakenPairs, poloniexPairs, xbtcePairs, hitbtcPairs]
totalPairs = [hitbtcPairs, bitfinexPairs, krakenPairs, poloniexPairs, cryptopiaPairs, bittrexPairs, xbtcePairs]

#This function pulls information from all exchanges based on a given coin pair
def aggregateOrders(coinPair):
    asks, bids, exchanges = [], [], []
    try:
        pAsk, pBid = poloniex.topAskBid(poloniexPairs[coinPair])
        asks.append(pAsk)
        bids.append(pBid)
        exchanges.append('poloniex')
        print("Success: Poloniex - Ask:", pAsk, "Bid:",pBid)
    except:
        print("Failure: Poloniex")
        
    try:
        kAsk, kBid = kraken.topAskBid(krakenPairs[coinPair])
        asks.append(kAsk)
        bids.append(kBid)
        exchanges.append('kraken')
        print("Success: Kraken - Ask:", kAsk, "Bid:",kBid)
    except: 
        print("Failure: Kraken")
        
    try:
        cAsk, cBid = cryptopia.topAskBid(cryptopiaPairs[coinPair])
        asks.append(cAsk)
        bids.append(cBid)
        exchanges.append('cryptopia')
        print("Success: Cryptopia - Ask:", cAsk, "Bid:", cBid)
    except:
        print("Failure: Cryptopia")
        
    try:
        bAsk, bBid = bitfinex.topAskBid(bitfinexPairs[coinPair])
        asks.append(bAsk)
        bids.append(bBid)
        exchanges.append('bitfinex')
        print("Success: Bitfinex - Ask:", bAsk, "Bid:", bBid)
    except:
        print("Failure: Bitfinex")
        
    try:
        bAsk, bBid = bittrex.topAskBid(bittrexPairs[coinPair])
        asks.append(bAsk)
        bids.append(bBid)
        exchanges.append('bittrex')
        print("Success: Bittrex - Ask:", bAsk, "Bid:", bBid)
    except:
        print("Failure: Bittrex")
        
    try:
        bAsk, bBid = xbtce.topAskBid(xbtcePairs[coinPair])
        asks.append(bAsk)
        bids.append(bBid)
        exchanges.append('xbtce')
        print("Success: xBTCe - Ask:", bAsk, "Bid:", bBid)
    except:
        print("Failure: xBTCe")
    
    try:
        bAsk, bBid = hitbtc.topAskBid(hitbtcPairs[coinPair])
        asks.append(bAsk)
        bids.append(bBid)
        exchanges.append('hitbtc')
        print("Success: HitBTC - Ask:", bAsk, "Bid:", bBid)
    except:
        print("Failure: HitBTC")

    return asks, bids, exchanges

#This function checks to see if there's a discrepency
def checkForDifference(coin, percentThreshold = 0.5):
    asks, bids, exchanges = aggregateOrders(coin)
    try:
        #Get difference information
        avg = np.mean(asks+bids)
        maximum = max(bids)
        minimum = min(asks)
        diff = maximum-minimum
        pct = (diff/avg)*100

        #if the percentages is above the threshold, then report it
        if pct >= percentThreshold:
            print('Discrepency')
            cheap = exchanges[asks.index(minimum)]
            expensive = exchanges[bids.index(maximum)]
            return (coin, diff, pct, avg, cheap, expensive, minimum, maximum)
        #otherwise, just ignore
        else:
            print('No Discrepency')
    except:
        print('Error')

#writes a log of current state as the timestamp
def writeLog(log):
    toWrite = pd.DataFrame(log)
    toWrite.columns = ['Coin Pair', 'Price Difference', 'Percent Difference', 'Price Average', 'Cheap Exchange', 'Expensive Exchange', 'Min', 'Max']
    path = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H-%M-%S')
    toWrite.to_csv('logs/'+path+'.csv')
    return []

#continually checks for winning numbers
def makeMoney(listOfPairs, numWins=30, sleepTime=15, messaging = True, msgpct = 3):  
    winners = []
    while True:
        for group in listOfPairs:
            if len(winners) >= numWins: 
                winners = writeLog(winners)
                print('\nLog Written\n')
                
            for token in group.keys():
                winner = checkForDifference(token)
                if winner:
                    winners.append(winner)
                    if winner[2] > msgpct and messaging:
                        body = '\n' + winner[0]+' has discrepency of '+str(winner[1])+' which is '+str(winner[2])+' percent. It is cheap on '+winner[4]+' and expensive on '+winner[5]
                        message = cli.messages.create(body=body, from_=myTwilioNumber, to=myCellPhone)
                        print('\n-----MESSAGE SENT-----\n')
                time.sleep(sleepTime)
    return winners
