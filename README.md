# PyExchange - Fiat to USD

## Project Description
PyExchange is a python package to convert foreign currencies into US dollars. It uses the free API key from openexchangerates.org to get over 200 currencies. PyExchange allows you to perform as many currency conversions as you wish by caching the hourly exchange rates from openexchange.org in a python shelve.

 ## Usage
 ```python
import pyexchange

pyexchange.convert(100, 'EUR', 'Your APP_ID')
```

Get your app_id from https://openexchangerates.org/signup/free

## Notes
We welcome your feedback and support, raise github ticket if you want to report a bug. Need new features? Contact us on github