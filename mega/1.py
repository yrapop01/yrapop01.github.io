from datetime import datetime, timedelta
from xml.etree.ElementTree import fromstring
import requests
import gzip
from xmljson import Parker
from multiprocessing.dummy import Pool
import pandas as pd

DATES = [datetime.now() + timedelta(-i) for i in range(365, 0, -30)]
DATES = [d.strftime('%Y%m%d') for d in DATES]

STORE_ID = '7290055700007-1201-'
PREFIX = 'PriceFull' + STORE_ID
sample_postfix = '201809060010.gz'
PATH_LEN = len(PREFIX) + len(sample_postfix)

URL = 'http://publishprice.mega.co.il/'

def get_prices(date):
    html = requests.get(URL + date + '/').text
    i = html.find(PREFIX)
    if i < 0:
        return None
    
    link = html[i:i + PATH_LEN]
    r = requests.get(URL + date + '/' + link)
    
    xml = gzip.decompress(r.content)

    parker = Parker(dict_type=dict)
    return parker.data(fromstring(xml))

def get_price(date):
    return get_prices(date)['Items']['Item']

with Pool(len(DATES)) as pool:
    prices = pool.map(get_price, DATES)

for items_list, date in zip(prices, DATES):
    for item in items_list:
        item['Date'] = date

flat_prices = [price for subprices in prices for price in subprices]
df = pd.DataFrame(flat_prices)
