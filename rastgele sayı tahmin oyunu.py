import random
sayı = random.randint(1,100)
tahmin = -1
while tahmin != sayı:
    tahmin = int(input("1 ile 100 arasında bir sayı tahmin edin: "))
    if tahmin < sayı:
        print("Daha büyük bir sayı deneyin.")
    elif tahmin > sayı:
        print("Daha küçük bir sayı deneyin.")
    else:
        print("Tebrikler! Doğru tahmin ettiniz.")   


#İEB#
