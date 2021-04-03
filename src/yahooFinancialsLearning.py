#https://github.com/ranaroussi/yfinance
import yfinance as YahooFundamentals
# https://github.com/JECSand/yahoofinancials
from yahoofinancials import YahooFinancials 
import json
from pprint import pprint
cryptocurrencies = ['BTC-USD', 'ETH-USD', 'XRP-USD']
yahoo_financials_cryptocurrencies = YahooFinancials(cryptocurrencies)
daily_crypto_prices = yahoo_financials_cryptocurrencies.get_historical_price_data('2008-09-15', '2018-09-15', 'daily')

# need a  refresher in JSON and nested dict
# https://www.learnbyexample.org/python-nested-dictionary/
pprint(daily_crypto_prices.keys())
pprint(daily_crypto_prices['BTC-USD'].keys())
#pprint(daily_crypto_prices['BTC-USD'])
for k,v in daily_crypto_prices["BTC-USD"].items():
    print(k,v)
    break
#pprint(json.dumps(daily_crypto_prices["BTC-USD"]))
