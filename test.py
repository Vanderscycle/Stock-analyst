
import pandas as pd
import numpy as np
import os
from os.path import join, dirname
from dotenv import load_dotenv
import requests

import sys
import json
dotenv_path = sys.path.insert(0,os.path.abspath('../.env'))
load_dotenv(dotenv_path)

MARKETSTACK_API_KEY = os.environ.get("MARKETSTACK_API_KEY")

#https://marketstack.com/documentation
#https://www.nylas.com/blog/use-python-requests-module-rest-apis/
baseUrl = 'http://api.marketstack.com/v1/'
method = ['eod','intraday']
# /Intraday Data API Endpoint
ticker = 'AAPL'
# http://api.marketstack.com/v1/intraday
mainParameters = [f'?access_key={MARKETSTACK_API_KEY}',
    f'&symbols={ticker}']
    
#  optional parameters: 

optionalParameters = [
    "&interval=1h",
    "&sort=DESC",
    "&date_from=2021-03-08",
    "&date_to=2021-03-12",
    "&limit=10",
    "&offset=0"
    ]
urlRequest = baseUrl+method[0]+''.join(mainParameters)#+''.join(optionalParameters)
response = requests.get(urlRequest)
print(response)    

from itertools import islice

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

jsonData = json.loads(response.text)

#https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
print(json.dumps(jsonData['data'][:2], indent=4, sort_keys=True))

# !pip3 install quandl
import quandl
quandl.ApiConfig.api_key = os.environ.get("QUANDL_API_KEY")
# yahoo data
# !pip3 install yfinance  
#https://github.com/ranaroussi/yfinance
import yfinance as yf
# !pip install yahoofinancials
#https://github.com/JECSand/yahoofinancials
from yahoofinancials import YahooFinancials 

gme = yf.Ticker("GME")

# get stock info
# print(gme.info)
# print(gme.dividends)



gme2 = YahooFinancials('GME')
#print(gme2.get_financial_stmts('quarterly', 'balance'))