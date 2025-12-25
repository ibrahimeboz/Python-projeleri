#İEB#
# Silindirin alanı ve hacmini hesaplayan program
# Gelişmiş özellikler eklenmiştir: kullanıcı dostu arayüz, hata kontrolü,
# sonuçların dosyaya kaydedilmesi ve önceki hesaplamaların görüntülenmesi

import math
import json
from datetime import datetime

def sicak_kontrol(deger, ad):
    """Giriş değeri kontrol ve doğrulama"""
    while True:
        try:
            sayi = float(deger)
            if sayi <= 0:
                print(f"Hata: {ad} pozitif bir sayı olmalıdır!")
                deger = input(f"Lütfen {ad} yeniden giriniz: ")
                continue
            return sayi
        except ValueError:
            print(f"Hata: Geçersiz giriş! {ad} için sayı giriniz.")
            deger = input(f"Lütfen {ad} yeniden giriniz: ")

def silindir_hesapla(r, h):
    """Silindir alan ve hacim hesapla"""
    taban_alan = math.pi * r ** 2
    yanal_alan = 2 * math.pi * r * h
    toplam_alan = 2 * taban_alan + yanal_alan
    hacim = taban_alan * h
    
    return {
        "taban_alan": taban_alan,
        "yanal_alan": yanal_alan,
        "toplam_alan": toplam_alan,
        "hacim": hacim
    }

def kure_hesapla(r):
    """Küre alan ve hacim hesapla"""
    alan = 4 * math.pi * r ** 2
    hacim = (4/3) * math.pi * r ** 3
    
    return {
        "alan": alan,
        "hacim": hacim
    }

def kup_hesapla(a):
    """Küp alan ve hacim hesapla"""
    alan = 6 * a ** 2
    hacim = a ** 3
    
    return {
        "alan": alan,
        "hacim": hacim
    }

def prizma_hesapla(taban_alan, cevre, yukseklik):
    """Dikdörtgen prizma alan ve hacim hesapla"""
    yanal_alan = cevre * yukseklik
    toplam_alan = 2 * taban_alan + yanal_alan
    hacim = taban_alan * yukseklik
    
    return {
        "taban_alan": taban_alan,
        "yanal_alan": yanal_alan,
        "toplam_alan": toplam_alan,
        "hacim": hacim
    }

def sonucu_dosyaya_kaydet(hesaplamalar):
    """Hesaplamaları JSON dosyasına kaydet"""
    dosya_adi = "hesaplamalar.json"
    
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            veri = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        veri = []
    
    hesaplamalar['tarih'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    veri.append(hesaplamalar)
    
    with open(dosya_adi, 'w', encoding='utf-8') as f:
        json.dump(veri, f, ensure_ascii=False, indent=2)
    
    print(f"✓ Sonuçlar '{dosya_adi}' dosyasına kaydedildi!")

def sonucu_goster(sonuc, sekil_adi, ozellikler):
    """Hesaplama sonuçlarını güzel şekilde göster"""
    print("\n" + "="*50)
    print(f"📊 {sekil_adi.upper()} HESAPLAMA SONUÇLARI")
    print("="*50)
    
    for ozellik, deger in ozellikler.items():
        print(f"{ozellik:.<30} {deger}")
    
    print("="*50 + "\n")
    
    return ozellikler

def menu():
    """Ana menü göster"""
    print("\n" + "*"*50)
    print("🎯 GEOMETRİK ŞEKİLLER ALAN VE HACİM HESAPLAMA")
    print("*"*50)
    print("1. Silindir")
    print("2. Küre")
    print("3. Küp")
    print("4. Dikdörtgen Prizma")
    print("5. Önceki Hesaplamaları Görüntüle")
    print("0. Çıkış")
    print("*"*50)
    return input("Seçiminiz: ")

def onceki_hesaplamalari_goster():
    """Daha önce yapılan hesaplamaları göster"""
    dosya_adi = "hesaplamalar.json"
    
    try:
        with open(dosya_adi, 'r', encoding='utf-8') as f:
            veri = json.load(f)
        
        if not veri:
            print("Henüz hesaplama kaydı yok!")
            return
        
        print("\n" + "="*50)
        print("📋 ÖNCEKİ HESAPLAMALAR")
        print("="*50)
        
        for i, hesap in enumerate(veri[-5:], 1):  # Son 5 kaydı göster
            print(f"\n{i}. {hesap.get('tarih', 'Tarih Yok')}")
            for anahtar, deger in hesap.items():
                if anahtar != 'tarih':
                    print(f"   {anahtar}: {deger}")
        
        print("="*50 + "\n")
    except FileNotFoundError:
        print("Henüz hesaplama kaydı yok!")

def main():
    """Ana program"""
    devam = True
    
    while devam:
        secim = menu()
        
        if secim == "1":
            # Silindir
            print("\n📐 SİLİNDİR HESAPLAMA")
            r = sicak_kontrol(input("Yarıçapı giriniz (cm): "), "Yarıçap")
            h = sicak_kontrol(input("Yüksekliği giriniz (cm): "), "Yükseklik")
            
            sonuc = silindir_hesapla(r, h)
            ozellikler = {
                "Yarıçap": f"{r:.2f} cm",
                "Yükseklik": f"{h:.2f} cm",
                "Taban Alanı": f"{sonuc['taban_alan']:.2f} cm²",
                "Yanal Alanı": f"{sonuc['yanal_alan']:.2f} cm²",
                "Toplam Alanı": f"{sonuc['toplam_alan']:.2f} cm²",
                "Hacim": f"{sonuc['hacim']:.2f} cm³"
            }
            
            sonucu_goster(sonuc, "Silindir", ozellikler)
            
            if input("Sonuçları kaydetmek ister misiniz? (e/h): ").lower() == 'e':
                sonucu_dosyaya_kaydet({"tip": "Silindir", **ozellikler})
        
        elif secim == "2":
            # Küre
            print("\n🔵 KÜRE HESAPLAMA")
            r = sicak_kontrol(input("Yarıçapı giriniz (cm): "), "Yarıçap")
            
            sonuc = kure_hesapla(r)
            ozellikler = {
                "Yarıçap": f"{r:.2f} cm",
                "Yüzey Alanı": f"{sonuc['alan']:.2f} cm²",
                "Hacim": f"{sonuc['hacim']:.2f} cm³"
            }
            
            sonucu_goster(sonuc, "Küre", ozellikler)
            
            if input("Sonuçları kaydetmek ister misiniz? (e/h): ").lower() == 'e':
                sonucu_dosyaya_kaydet({"tip": "Küre", **ozellikler})
        
        elif secim == "3":
            # Küp
            print("\n📦 KÜP HESAPLAMA")
            a = sicak_kontrol(input("Kenar uzunluğu giriniz (cm): "), "Kenar")
            
            sonuc = kup_hesapla(a)
            ozellikler = {
                "Kenar Uzunluğu": f"{a:.2f} cm",
                "Yüzey Alanı": f"{sonuc['alan']:.2f} cm²",
                "Hacim": f"{sonuc['hacim']:.2f} cm³"
            }
            
            sonucu_goster(sonuc, "Küp", ozellikler)
            
            if input("Sonuçları kaydetmek ister misiniz? (e/h): ").lower() == 'e':
                sonucu_dosyaya_kaydet({"tip": "Küp", **ozellikler})
        
        elif secim == "4":
            # Dikdörtgen Prizma
            print("\n📏 DİKDÖRTGEN PRİZMA HESAPLAMA")
            boy = sicak_kontrol(input("Boy (cm): "), "Boy")
            en = sicak_kontrol(input("En (cm): "), "En")
            yukseklik = sicak_kontrol(input("Yükseklik (cm): "), "Yükseklik")
            
            taban_alan = boy * en
            cevre = 2 * (boy + en)
            
            sonuc = prizma_hesapla(taban_alan, cevre, yukseklik)
            ozellikler = {
                "Boy": f"{boy:.2f} cm",
                "En": f"{en:.2f} cm",
                "Yükseklik": f"{yukseklik:.2f} cm",
                "Taban Alanı": f"{sonuc['taban_alan']:.2f} cm²",
                "Yanal Alanı": f"{sonuc['yanal_alan']:.2f} cm²",
                "Toplam Alanı": f"{sonuc['toplam_alan']:.2f} cm²",
                "Hacim": f"{sonuc['hacim']:.2f} cm³"
            }
            
            sonucu_goster(sonuc, "Dikdörtgen Prizma", ozellikler)
            
            if input("Sonuçları kaydetmek ister misiniz? (e/h): ").lower() == 'e':
                sonucu_dosyaya_kaydet({"tip": "Dikdörtgen Prizma", **ozellikler})
        
        elif secim == "5":
            onceki_hesaplamalari_goster()
        
        elif secim == "0":
            print("\n👋 Program kapatılıyor... Hoşça kalın!")
            devam = False
        
        else:
            print("❌ Geçersiz seçim! Lütfen tekrar deneyiniz.")

if __name__ == "__main__":
    main()


#İEB#
