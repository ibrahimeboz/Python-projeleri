def kilo():
    kilo = float(input("kilonuzu giriniz:"))
    return kilo

def boy():
    boy = float(input("boyunuzu giriniz:"))
    return boy

def bki(kilo, boy):
    bki = kilo / (boy ** 2)
    return bki


k = kilo()
b = boy()
bki_değeri = bki(k, b)

if bki_değeri < 18.5:
    print("zayıf")
elif bki_değeri >= 18.5 and bki_değeri < 24.9:
    print("normal")
elif bki_değeri >= 25 and bki_değeri < 29.9:
    print("fazla kilolu")
elif bki_değeri >= 30 and bki_değeri < 34.9:
    print("obez")   
elif bki_değeri >= 35 and bki_değeri < 39.9:
    print("aşırı obez")
else:
    print("morbid obez")
