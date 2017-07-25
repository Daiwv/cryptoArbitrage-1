# cryptoArbitrage
Developing an arbitrage bot for cryptocurrencies in Python


## How to Use
After downloading the repo, open either dataHandler.py or tetherTester.py. 

NOTE: I've got my trial twilio account linked up to send me texts each time the discrepancy is above a certain percentage. You won't be able to do this unless you have an account of your own. 

### Data Handler
dataHandler.py looks at all possible combinations of coins listed on 7 of the top exchanges that are available in the United States. I suggest running the command 'makeMoney(usePairs)'. This will iterate continually through most pairs of tokens available on those exchanges. By default, it will save a (.csv) log for roughly every 50 price discrepancies found. It lists the coin pair, the price discrepancy, the percent discrepancy, the cheap exchange, the expensive exchange, and the average cost of the token over the 7 exchanges.

### Tether Tester
tetherTester.py is specific for Tether's 4 largest (non-USD) exchanges. It operates the same way as data handler, except it has no log writing features.
