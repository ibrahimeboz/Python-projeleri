a=int(input("Bir sayı giriniz: "))
seç=input("seçiminizi yapınız 1=mm 2=cm 3=m 4=km: ")
print("seçiminiz:",seç)
if seç=="1":
   b=1000
   print("girdiğiniz sayı mm cinsindendir")
if seç=="2":
    b=100
    print("girdiğiniz sayı cm cinsindendir")
if seç=="3":
    b=10
    print("girdiğiniz sayı m cinsindendir")
if seç=="4":
    b=1
    print("girdiğiniz sayı km cinsindendir")

# Basit dönüşüm (girdiği birimi b ile çarpar)
c = a * b
print("Dönüşüm sonucu:", c)
if seç=="4":
    b=0.01
    print("girdiğiniz sayı km cinsindendir")