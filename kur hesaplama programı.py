# Kur Hesaplama Programı
# Bu program, Türk Lirası (TRY) cinsinden belirli bir miktarın çeşitli döviz kurlarına karşılık gelen değerini hesaplar.
# Gerekli kütüphane: requests (pip install requests)
# Kullanım: Programı çalıştırdığınızda, belirlenen miktarın farklı döviz kurlarındaki karşılıkları ekrana yazdırılır.
#kodlayan kişi : İbrahim Etem Boz


import requests

url = "https://api.exchangerate-api.com/v4/latest/TRY"
data = requests.get(url).json()

amount = 1000
currencies = ["EUR","USD","GBP","JPY","CHF","CNY","RUB","CAD","AUD"]

for c in currencies:
    print(f"{amount} TRY = {amount * data['rates'][c]:.2f} {c}")

print("\nKodlayan Kişi: İbrahim Etem Boz")