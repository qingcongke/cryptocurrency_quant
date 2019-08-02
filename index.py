import pandas as np
import ccxt

binance = ccxt.binance()

markets = binance.loadMarkets()

for i in markets:
    print(i)

print(binance.symbols)
