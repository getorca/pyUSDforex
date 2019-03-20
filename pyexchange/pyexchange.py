import requests
import json
import shelve
import time
from decimal import *

# define global vars
exchange_shelve = shelve.open('latest_exchange.db')


def convert(amount, to_currency, app_id):

    # first we need to check if the shelve exists
    if 'latest' not in exchange_shelve:
        get_rates(app_id)

    # check if the shelved result is from the past hour
    if (int(time.time()) - exchange_shelve['latest']['timestamp']) > 3900:
        get_rates(app_id)
        rates = exchange_shelve['latest']['rates']
    else:
        # get the result from the shelve
        rates = exchange_shelve['latest']['rates']

    # close the shelve
    exchange_shelve.close()

    # solve for the result
    result = (1 / Decimal(rates[to_currency]) * amount)

    return result


def get_rates(app_id):

    # get the json exchange rates to USD
    request_url = 'https://openexchangerates.org/api/latest.json?app_id='+app_id+'&base=USD&prettyprint=false'

    req_ob = requests.get(request_url)

    # save to shelve
    exchange_shelve['latest'] = req_ob.json()


if __name__ == '__main__':
    convert(10, 'EUR', '9bd615ffefe94f92990bc5f26f465ee5')
