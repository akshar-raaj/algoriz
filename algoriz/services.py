import requests


def pull_close_prices(ticker):
    """
    Pulls daily close prices for `ticker` for last 1 year.
    """
    url = 'https://api.iextrading.com/1.0/stock/%s/chart/1y' % (ticker,)
    response = requests.get(url)
    js = response.json()
    return js
