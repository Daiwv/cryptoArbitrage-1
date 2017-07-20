#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 19:49:02 2017

@author: garrettlee
"""

import requests

def getOrders(pair):
    r = requests.get('https://api.bitfinex.com/v1/book/'+pair)
    return r.json()

def topAskBid(pair):
    orders = getOrders(pair)
    ask = float(orders['asks'][0]['price'])
    bid = float(orders['bids'][0]['price'])
    return ask, bid

def importDicts(file):
    dicts_from_file = []
    with open('bitfinex.txt','r') as inf:
        for line in inf:
            dicts_from_file.append(eval(line)) 
    return dicts_from_file


bf = {"bitfinex": {"Litecoin-Bitcoin":"ltcbtc", "Ethereum-Bitcoin":"ethbtc", "Ethereum Classic-Bitcoin": "etcbtc", "ZCash-Bitcoin": "zecbtc", "Monero-Bitcoin":"xmrbtc", "Dash-Bitcoin":"dshbtc", "BitConnect-Bitcoin":"bccbtc", "Ripple-Bitcoin":"xrpbtc", "IOTA-Bitcoin":"iotbtc","IOTA-Ethereum":"ioteth","EOS-Bitcoin":"eosbtc", "EOS-Ethereum":"eoseth"}} 
kr = {"kraken": {"Dash-Bitcoin":"DASHXBT", "EOS-Ethereum":"EOSETH", "EOS-Bitcoin":"EOSXBT", "Gnosis-Ethereum":"GNOETH", "Gnosis-Bitcoin":"GNOXBT","Ethereum Classic-Ethereum":"XETCXETH","Ethereum Classic-Bitcoin":"XETCXXBT","Ethereum-Bitcoin":"XETHXXBT","Iconomi-Ethereum":"XICNXETH","Iconomi-Bitcoin":"XICNXXBT","Litecoin-Bitcoin":"XLTCXXBT","Melon-Ethereum":"XMLNXETH","Melon-Bitcoin":"XMLNXXBT","Augur-Ethereum":"XREPXETH","Augur-Bitcoin":"XREPXXBT","Dogecoin-Bitcoin":"XXDGXXBT","Stellar Lumens-Bitcoin":"XXLMXXBT","Monero-Bitcoin":"XXMRXXBT","Ripple-Bitcoin":"XXRPXXBT","ZCash-Bitcoin":"XZECXXBT"}}
po = {'poloniex': {'Belacoin-Bitcoin': 'BTC_BELA', 'Bitcoin Dark-Bitcoin': 'BTC_BTCD', 'Bitmark-Bitcoin': 'BTC_BTM', 'Bitshares-Bitcoin': 'BTC_BTS', 'Blackcoin-Bitcoin': 'BTC_BLK', 'Burst-Bitcoin': 'BTC_BURST', 'Bytecoin-Bitcoin': 'BTC_BCN', 'Clams-Bitcoin': 'BTC_CLAM', 'Dash-Bitcoin': 'BTC_DASH', 'Digibyte-Bitcoin': 'BTC_DGB', 'Dogecoin-Bitcoin': 'BTC_DOGE', 'Einsteinium': 'BTC_EMC2', 'Floodingcoin-Bitcoin': 'BTC_FLDC', 'Florincoin-Bitcoin': 'BTC_FLO', 'Gamecredits-Bitcoin': 'BTC_GAME', 'Gridcoin-bitcoin': 'BTC_GRC', 'Zcash-bitcoin': 'BTC_ZEC', 'ardor-bitcoin': 'BTC_ARDR', 'augur-bitcoin': 'BTC_REP', 'augur-ethereum': 'ETH_REP', 'augur-tether': 'USDT_REP', 'bitcoin plus-bitcoin': 'BTC_XBC', 'bitcrystals-bitcoin': 'BTC_BCY', 'counterparty-bitcoin': 'BTC_XCP', 'dash-tether': 'USDT_DASH', 'decred-bitcoin': 'BTC_DCR', 'dnotes-bitcoin': 'BTC_NOTE', 'ethereum classic-bitcoin': 'BTC_ETC', 'ethereum classic-ethereum': 'ETH_ETC', 'ethereum classic-tether': 'USDT_ETC', 'ethereum-bitcoin': 'BTC_ETH', 'ethereum-steem': 'ETH_STEEM', 'ethereum-tether': 'USDT_ETH', 'expanse-bitcoin': 'BTC_EXP', 'factom-bitcoin': 'BTC_FCT', 'gnosis-bitcoin': 'BTC_GNO', 'gnosis-ethereum': 'ETH_GNO', 'golem-bitcoin': 'BTC_GNT', 'golem-ethereum': 'ETH_GNT', 'huntercoin-bitcoin': 'BTC_HUC', 'lisk-bitcoin': 'BTC_LSK', 'list-ethereum': 'ETH_LSK', 'litecoin-bitcoin': 'BTC_LTC', 'litecoin-tether': 'USDT_LTC', 'maidsafecoin-bitcoin': 'BTC_MAID', 'monero-bitcoin': 'BTC_XMR', 'monero-tether': 'USDT_XMR', 'monero-zcash': 'XMR_ZEC', 'namecoin-bitcoin': 'BTC_NMC', 'nautiluscoin-bitcoin': 'BTC_NAUT', 'navcoin-bitcoin': 'BTC_NAV', 'nem-bitcoin': 'BTC_XEM', 'neoscoin': 'BTC_NEOS', 'nexium-bitcoin': 'BTC_NXC', 'nxt-bitcoin': 'BTC_NXT', 'nxt-tether': 'USDT_NXT', 'omni-bitcoin': 'BTC_OMNI', 'pascalcoin-bitcoin': 'BTC_PASC', 'peercoin-bitcoin': 'BTC_PPC', 'pinkcoin-bitcoin': 'BTC_PINK', 'potcoin-bitcoin': 'BTC_POT', 'primecoin-bitcoin': 'BTC_XPM', 'radium-bitcoin': 'BTC_RADS', 'riecoin-bitcoin': 'BTC_RIC', 'ripple-bitcoin': 'BTC_XRP', 'ripple-tether': 'USDT_XRP', 'siacoin-bitcoin': 'BTC_SC', 'steem-bitcoin': 'BTC_STEEM', 'storjcoin x-bitcoin': 'BTC_SJCX', 'stratus-bitcoin': 'BTC_STRAT', 'synereo-bitcoin': 'BTC_AMP', 'syscoin-bitcoin': 'BTC_SYS', 'tether-bitcoin': 'USDT_BTC', 'vcash-bitcoin': 'BTC_XVC', 'vericoin-bitcoin': 'BTC_VRC', 'vertcoin-bitcoin': 'BTC_VTC', 'viacoin-bitcoin': 'BTC_VIA', 'zcash-ethereum': 'ETH_ZEC', 'zcash-tether': 'USDT_ZEC'}}