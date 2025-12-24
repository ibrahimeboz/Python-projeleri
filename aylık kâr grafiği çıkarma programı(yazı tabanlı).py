# Aylık kar grafiği çıkarma programı
# Özellikler:
# - İstenilen ay sayısı (default 12)
# - Ondalık için ',' veya '.' kabul eder
# - Pozitif/negatif değerleri gösterir (negatifler sola, pozitifler sağa)
# - Otomatik veya kullanıcı tanımlı ölçek (1 yıldız = X TL)
# - Basit giriş doğrulama ve çıktı kaydetme seçeneği

import math

def parse_number(s):
    try:
        return float(s.strip().replace(",", "."))
    except:
        raise ValueError

def get_profits(n_months=12):
    print(f"{n_months} aylık kar değerlerini girin. Her değeri Enter ile ayırın.")
    print("Tümünü tek satırda vermek isterseniz aralarında boşluk bırakın.")
    vals = []
    while len(vals) < n_months:
        try:
            remaining = n_months - len(vals)
            raw = input(f"{remaining} değer bekleniyor: ").strip()
            parts = raw.split()
            if not parts:
                print("Boş giriş, tekrar deneyin.")
                continue
            for p in parts:
                if len(vals) >= n_months:
                    break
                vals.append(parse_number(p))
        except ValueError:
            print("Geçersiz sayı girildi. Ondalık için '.' veya ',' kullanın.")
    return vals

def choose_scale(profits, max_width=50):
    abs_max = max(abs(x) for x in profits) if profits else 0
    if abs_max == 0:
        return 1000  # varsayılan
    # otomatik ölçek: hedef yıldız genişliği ~ max_width
    unit = max(1, math.ceil(abs_max / max_width / 1.0) * 100)  # yuvarla 100'ün katlarına
    # daha okunaklı birim önerileri
    suggestions = [1, 10, 50, 100, 500, 1000, 5000, 10000]
    # seçeneğe en yakın öneriyi al
    best = min(suggestions, key=lambda s: abs((abs_max / s) - max_width))
    return best

def draw_chart(profits, unit=None, max_width=50, show_values=True):
    if unit is None:
        unit = choose_scale(profits, max_width)
    left_width = max_width // 2
    right_width = max_width - left_width
    title = f"Yıllık Kar Grafiği (1 yıldız = {unit} TL)"
    print("\n" + title + "\n" + "-"*len(title))
    for i, val in enumerate(profits, start=1):
        stars = int(round(abs(val) / unit)) if unit > 0 else 0
        if val < 0:
            left = "-" * min(stars, left_width)
            right = " " * right_width
            bar = f"{left:>{left_width}}|{right}"
        else:
            left = " " * left_width
            right = "*" * min(stars, right_width)
            bar = f"{left}|{right}"
        label = f"{i:2}. Ay:"
        value_text = f" ({val:.2f} TL)" if show_values else ""
        print(f"{label} {bar}{value_text}")
    print("-" * (len(title)))

def main():
    try:
        raw = input("Kaç aylık veri gireceksiniz? (default 12, çıkmak için q): ").strip()
        if raw.lower() == "q":
            print("Çıkılıyor.")
            return
        n = int(raw) if raw else 12
    except:
        print("Geçersiz sayı, 12 kullanılıyor.")
        n = 12

    profits = get_profits(n)

    auto_unit = choose_scale(profits)
    print(f"Otomatik önerilen ölçek: 1 yıldız = {auto_unit} TL")
    u_in = input("Elle ölçek girmek ister misiniz? (örnek 1000) [Enter=otomatik]: ").strip()
    if u_in:
        try:
            unit = int(float(u_in))
            if unit <= 0:
                print("Olumsuz/0 ölçek kullanılamaz, otomatik seçildi.")
                unit = auto_unit
        except:
            print("Geçersiz ölçek, otomatik seçildi.")
            unit = auto_unit
    else:
        unit = auto_unit

    draw_chart(profits, unit=unit)

    save = input("Grafiği metin dosyasına kaydetmek ister misiniz? (e/h): ").strip().lower()
    if save == "e":
        path = input("Dosya adı (ör: grafik.txt): ").strip() or "grafik.txt"
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"1 yıldız = {unit} TL\n")
            for i, val in enumerate(profits, start=1):
                stars = int(round(abs(val) / unit))
                if val < 0:
                    line = f"{i:2}. Ay: {'-'*stars} ({val:.2f} TL)\n"
                else:
                    line = f"{i:2}. Ay: {'*'*stars} ({val:.2f} TL)\n"
                f.write(line)
        print(f"Kaydedildi: {path}")

if __name__ == "__main__":
    main()


#İEB#