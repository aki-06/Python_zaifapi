from zaifapi import *


btc_jpy = zaif.last_place('btc_jpy')
xem_jpy = zaif.last_place('xem_jpy')
btc_price_jpy = zaif.last_place('btc_jpy')['last_place']
xem_price_jpy = zaif.last_place('btc_jpy')['last_place']

print(btc_jpy)
print(xem_jpy)
print(btc_price_jpy)
print(xem_price_jpy)