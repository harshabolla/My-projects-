#pip install forex-python
#https://forex-python.readthedocs.io/en/latest/usage.html
from forex_python.converter import CurrencyCodes,CurrencyRates
from forex_python.bitcoin import BtcConverter

print('imported')

test = CurrencyCodes()
cur_symbol = test.get_symbol('INR')
cur_name = test.get_currency_name('INR')
print("the currency name is:= "+ cur_name)
#print(cur_symbol)
print(test.get_symbol('CHF'))
print(test.get_currency_name('CHF'))
c = CurrencyRates()
print(c.get_rates('INR'),'/n')

print('the cureency rate is ' , c.get_rate('USD','INR'))

print('the cureency converted rate is ' , c.convert('USD', 'INR',10))

b = BtcConverter() # force_decimal=True to get Decimal rates
print('the bitcon rate for usd is ',b.get_latest_price('USD'))