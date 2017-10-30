from zaifapi.impl import ZaifPublicApi

#ビットコインと日本円の終値を取得
zaif = ZaifPublicApi()
print(zaif.last_price('btc_jpy'))

