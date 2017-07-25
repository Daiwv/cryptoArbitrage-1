#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 10:06:54 2017

@author: garrettlee
"""

import dataHandler as DH

##Initialize all needed information
pairs = DH.dicts
pBal, bBal, cBal, kBal = 0.05, 0.05, 0.05, 0.05
coinPairs = ['verium-bitcoin', 'bitcoindark-bitcoin', 'transfercoin-bitcoin', 'stratis-bitcoin', 'incent-bitcoin', 'litecoin-tether', 'evergreencoin-bitcoin', 'gamecredits-bitcoin', 'nautiluscoin-bitcoin', 'safeexchangecoin-bitcoin', 'lisk-bitcoin', 'monero-tether', 'dogecoin-bitcoin', 'golem-bitcoin', 'dash-tether', 'dnotes-bitcoin', 'nubits-bitcoin', 'navcoin-bitcoin', 'potcoin-bitcoin', 'nxt-bitcoin', 'primecoin-bitcoin', 'melon-bitcoin', 'magi-bitcoin', 'litecoin-bitcoin', 'waves-bitcoin', 'augur-bitcoin', 'zcoin-bitcoin', 'namecoin-bitcoin', 'pinkcoin-bitcoin', 'ark-bitcoin', 'goldcoin-bitcoin', 'pivx-bitcoin', 'bytecoin-bitcoin', 'neweconomymovement-bitcoin', 'pascalcoin-bitcoin', 'rubycoin-bitcoin', 'bata-bitcoin', 'vcash-bitcoin', 'viacoin-bitcoin', 'reddcoin-bitcoin', 'lbry credits-bitcoin', 'clams-bitcoin', 'influxcoin-bitcoin', 'augur-ethereum', 'musicoin-bitcoin', 'ethereum classic-tether', 'zcash-tether', 'radium-bitcoin', 'startcoin-bitcoin', 'ethereum-tether', 'ubiq-bitcoin', 'geocoin-bitcoin', 'verge-bitcoin', 'zcash-bitcoin', 'dash-bitcoin', 'zclassic-bitcoin', 'unbreakablecoin-bitcoin', 'peercoin-bitcoin', 'digibyte-bitcoin', 'burst-bitcoin', 'syndicate-bitcoin', 'ardor-bitcoin', 'counterparty-bitcoin', 'bitsend-bitcoin', 'unobtanium-bitcoin', 'emercoin-bitcoin', 'nexium-bitcoin', 'groestlcoin-bitcoin', 'ethereum classic-bitcoin', 'boolberry-bitcoin', 'blackcoin-bitcoin', 'cloakcoin-bitcoin', 'einsteinium-bitcoin', 'bitcoin-tether', 'expanse-bitcoin', 'ethereum classic-ethereum', 'factom-bitcoin', 'zcash-ethereum', 'okcash-bitcoin', 'bitshares-bitcoin', 'ripple-tether', 'bitbean-bitcoin', 'gnosis-bitcoin', 'cannabiscoin-bitcoin', 'maidsafecoin-bitcoin', 'decred-bitcoin', 'komodo-bitcoin', 'syscoin-bitcoin', 'vertcoin-bitcoin', 'auroracoin-bitcoin', 'nexus-bitcoin', 'gridcoin-bitcoin', 'bitcrystals-bitcoin', 'vericoin-bitcoin', 'ethereum-bitcoin', 'monero-bitcoin', 'byteball-bitcoin', 'golem-ethereum', 'steem-bitcoin', 'siacoin-bitcoin', 'ripple-bitcoin', 'feathercoin-bitcoin', 'gnosis-ethereum']



def calculateFees(buyExchange, sellExchange, coin, amount):
    tradeFee = .25
    #calcuate fee to shift funds from buy exchange to sell exchange
    if buyExchange == 'cryptopia':
        transferFee = 1
    elif buyExchange == 'poloniex':
        transferFee = 1
    elif buyExchange == 'bittrex':
        transferFee = bTx[coin]
    elif buyExchange == 'kraken':
        transferFee = 1
    
    #calculate the fee needed to get equal BTC on all exchanges
    if sellExchange == 'cryptopia':
        balanceFee = 1
    elif sellExchange == 'poloniex':
        balanceFee = 1
    elif sellExchange == 'bittrex':
        balanceFee = 0.001
    elif sellExchange == 'kraken':
        balanceFee = 1
    
    totalFee = balanceFee + transferFee + 2*tradeFee
    return 2.5