import requests

URL = 'https://api.coindesk.com/v1/bpi/currentprice.json'
CURRENCIES = ['EUR', 'USD', 'GBP']

def test_bpi_list():
    resp = requests.get(URL)
    assert resp.status_code == 200
    bpi = resp.json()['bpi']
    crs = list(bpi.keys())
    difference = set(CURRENCIES) ^ set(crs)
    assert not difference

def test_gbp_description():
    resp = requests.get(URL)
    assert resp.status_code == 200
    bpi = resp.json()['bpi']
    assert bpi['GBP']['description'] == 'British Pound Sterling'